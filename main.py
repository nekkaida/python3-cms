# main.py

import argparse
import logging
import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError  # Correctly imported
from models_sqlalchemy import Base, Contact
from exceptions import ContactNotFoundError
from tabulate import tabulate
from rich.table import Table
from rich.console import Console

def setup_logging(log_file, log_level):
    """Configure the logging settings."""
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        print(f"Invalid log level: {log_level}. Defaulting to INFO.")
        numeric_level = logging.INFO
    logging.basicConfig(
        filename=log_file,
        level=numeric_level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def read_config(config_file):
    """Read and validate the configuration from the config file."""
    config = configparser.ConfigParser()
    config.read(config_file)

    if not config.has_section("database"):
        raise ValueError("Missing 'database' section in config.ini.")
    if not config.has_section("logging"):
        raise ValueError("Missing 'logging' section in config.ini.")

    db_url = config.get("database", "db_url", fallback="sqlite:///contacts.db")
    log_file = config.get("logging", "log_file", fallback="contact_manager.log")
    log_level = config.get("logging", "log_level", fallback="INFO")

    # Validate log level
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    if log_level.upper() not in valid_levels:
        print(f"Invalid log level: {log_level}. Defaulting to INFO.")
        log_level = "INFO"

    return db_url, log_file, log_level

def setup_database(db_url):
    """
    Set up the database engine and session.

    Parameters:
    db_url (str): Database URL.

    Returns:
    Session, Engine: SQLAlchemy session and engine objects.
    """
    engine = create_engine(db_url, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine

def create_tables(engine):
    """
    Create all tables defined by the Base's subclasses.

    Parameters:
    engine (Engine): SQLAlchemy engine object.
    """
    Base.metadata.create_all(engine)
    logging.info("All tables created successfully.")

def add_contact(session, name, email, phone):
    """
    Add a new contact to the database.

    Parameters:
    session (Session): SQLAlchemy session object.
    name (str): Name of the contact.
    email (str): Email of the contact.
    phone (str): Phone number of the contact.
    """
    new_contact = Contact(name=name, email=email, phone=phone)
    session.add(new_contact)
    try:
        session.commit()
        print(f"Contact '{name}' added successfully with ID {new_contact.id}.")
        logging.info(f"Added contact: {new_contact}")
    except IntegrityError as e:
        session.rollback()
        print(f"Integrity Error: {e.orig}")
        logging.error(f"Integrity Error: {e.orig}")
    except Exception as e:
        session.rollback()
        print(f"Error adding contact: {e}")
        logging.error(f"Error adding contact: {e}")

def list_contacts(session, show_all=False, page=1, per_page=10):
    """
    List contacts. Optionally show all contacts including inactive ones.

    Parameters:
    session (Session): SQLAlchemy session object.
    show_all (bool): Flag to show all contacts.
    page (int): Page number for pagination.
    per_page (int): Number of contacts per page.
    """
    try:
        contacts = session.query(Contact).offset((page - 1) * per_page).limit(per_page).all()
        if not contacts:
            print("No contacts found on this page.")
            return
        display_contacts_rich(contacts, page)
    except Exception as e:
        print(f"Error listing contacts: {e}")
        logging.error(f"Error listing contacts: {e}")

def display_contacts_rich(contacts, page=None):
    """
    Display contact records using Rich for enhanced formatting.

    Parameters:
    contacts (list of Contact): List containing Contact objects.
    page (int, optional): Page number for display.
    """
    if not contacts:
        print("No contacts found.")
        return
    table = Table(title="List of Contacts")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Email", style="green")
    table.add_column("Phone", style="yellow")

    for contact in contacts:
        table.add_row(str(contact.id), contact.name, contact.email, contact.phone)

    console = Console()
    if page:
        table.title = f"Contacts - Page {page}"
    console.print(table)

def update_contact(session, contact_id, new_email=None, new_phone=None):
    """
    Update a contact's email and/or phone.

    Parameters:
    session (Session): SQLAlchemy session object.
    contact_id (int): ID of the contact to update.
    new_email (str, optional): New email address.
    new_phone (str, optional): New phone number.
    """
    try:
        contact = session.query(Contact).filter(Contact.id == contact_id).one_or_none()
        if contact is None:
            print(f"No contact found with ID: {contact_id}")
            logging.warning(f"No contact found with ID: {contact_id} for update.")
            return
        if new_email:
            contact.email = new_email
        if new_phone:
            contact.phone = new_phone
        session.commit()
        print(f"Contact ID {contact_id} has been updated.")
        logging.info(f"Updated contact: {contact}")
    except IntegrityError as e:
        session.rollback()
        print(f"Integrity Error: {e.orig}")
        logging.error(f"Integrity Error: {e.orig}")
    except Exception as e:
        session.rollback()
        print(f"Error updating contact: {e}")
        logging.error(f"Error updating contact: {e}")

def delete_contact(session, contact_id):
    """
    Delete a contact from the database by ID.

    Parameters:
    session (Session): SQLAlchemy session object.
    contact_id (int): ID of the contact to delete.
    """
    try:
        contact = session.query(Contact).filter(Contact.id == contact_id).one_or_none()
        if contact is None:
            print(f"No contact found with ID: {contact_id}")
            logging.warning(f"No contact found with ID: {contact_id} for deletion.")
            return
        session.delete(contact)
        session.commit()
        print(f"Contact with ID {contact_id} has been deleted.")
        logging.info(f"Deleted contact: {contact}")
    except Exception as e:
        session.rollback()
        print(f"Error deleting contact: {e}")
        logging.error(f"Error deleting contact: {e}")

def search_contacts(session, name=None, email=None, phone=None):
    """
    Search for contacts by name, email, or phone.

    Parameters:
    session (Session): SQLAlchemy session object.
    name (str, optional): Name to search for.
    email (str, optional): Email to search for.
    phone (str, optional): Phone number to search for.
    """
    try:
        query = session.query(Contact)
        if name:
            query = query.filter(Contact.name.ilike(f"%{name}%"))
        if email:
            query = query.filter(Contact.email.ilike(f"%{email}%"))
        if phone:
            query = query.filter(Contact.phone.ilike(f"%{phone}%"))
        contacts = query.all()
        if not contacts:
            print("No contacts found matching the criteria.")
            return
        display_contacts_rich(contacts)
        logging.debug(f"Search results: {contacts}")
    except Exception as e:
        print(f"Error searching contacts: {e}")
        logging.error(f"Error searching contacts: {e}")

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Contact Management System CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add Contact
    parser_add = subparsers.add_parser("add", help="Add a new contact")
    parser_add.add_argument("--name", required=True, help="Name of the contact")
    parser_add.add_argument("--email", required=True, help="Email of the contact")
    parser_add.add_argument("--phone", required=True, help="Phone number of the contact")

    # List Contacts
    parser_list = subparsers.add_parser("list", help="List all contacts")
    parser_list.add_argument("--all", action="store_true", help="Show all contacts")
    parser_list.add_argument("--page", type=int, default=1, help="Page number")
    parser_list.add_argument("--per_page", type=int, default=10, help="Number of contacts per page")

    # Update Contact
    parser_update = subparsers.add_parser("update", help="Update a contact's information")
    parser_update.add_argument("--id", type=int, required=True, help="ID of the contact to update")
    parser_update.add_argument("--email", help="New email address")
    parser_update.add_argument("--phone", help="New phone number")

    # Delete Contact
    parser_delete = subparsers.add_parser("delete", help="Delete a contact")
    parser_delete.add_argument("--id", type=int, required=True, help="ID of the contact to delete")

    # Search Contacts
    parser_search = subparsers.add_parser("search", help="Search for contacts")
    parser_search.add_argument("--name", help="Name to search for")
    parser_search.add_argument("--email", help="Email to search for")
    parser_search.add_argument("--phone", help="Phone number to search for")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    # Read configuration
    try:
        db_url, log_file, log_level = read_config("config.ini")
    except ValueError as e:
        print(e)
        return

    # Setup logging
    setup_logging(log_file, log_level)

    # Setup database
    session, engine = setup_database(db_url)
    create_tables(engine)

    # Execute commands
    if args.command == "add":
        add_contact(session, args.name, args.email, args.phone)
    elif args.command == "list":
        list_contacts(session, show_all=args.all, page=args.page, per_page=args.per_page)
    elif args.command == "update":
        if not args.email and not args.phone:
            print("Please provide at least one field to update (--email or --phone).")
        else:
            update_contact(session, args.id, new_email=args.email, new_phone=args.phone)
    elif args.command == "delete":
        delete_contact(session, args.id)
    elif args.command == "search":
        if not args.name and not args.email and not args.phone:
            print("Please provide at least one search criteria (--name, --email, or --phone).")
        else:
            search_contacts(session, name=args.name, email=args.email, phone=args.phone)

    # Close session and engine
    session.close()
    engine.dispose()
    logging.info("Database session closed and engine disposed.")

if __name__ == "__main__":
    main()
