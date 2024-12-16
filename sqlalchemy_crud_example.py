# sqlalchemy_crud_example.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError  # Correctly imported
import logging
from tabulate import tabulate
from exceptions import ContactNotFoundError  # Ensure this file exists with the defined exception

# Setup logging
logging.basicConfig(
    filename="contact_manager.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

Base = declarative_base()

class Contact(Base):
    """
    Contact model mapped to the 'contacts' table.
    """
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Contact(id={self.id}, name='{self.name}', email='{self.email}', phone='{self.phone}')>"

def setup_database(db_url):
    """
    Set up the database engine and session.

    Parameters:
    db_url (str): Database URL.

    Returns:
    Session, Engine: SQLAlchemy session and engine objects.
    """
    engine = create_engine(db_url, echo=False)  # Set echo=True to see SQL statements
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

def get_all_contacts(session):
    """
    Retrieve all contacts from the database.

    Parameters:
    session (Session): SQLAlchemy session object.

    Returns:
    list of Contact: List containing Contact objects.
    """
    try:
        contacts = session.query(Contact).all()
        logging.debug(f"Fetched contacts: {contacts}")
        return contacts
    except Exception as e:
        print(f"Error fetching contacts: {e}")
        logging.error(f"Error fetching contacts: {e}")
        return []

def display_contacts(contacts):
    """
    Display contact records in a formatted table.

    Parameters:
    contacts (list of Contact): List containing Contact objects.
    """
    if not contacts:
        print("No contacts found.")
        return
    table = []
    for contact in contacts:
        table.append([contact.id, contact.name, contact.email, contact.phone])
    headers = ["ID", "Name", "Email", "Phone"]
    print("\nList of Contacts:")
    print(tabulate(table, headers, tablefmt="grid"))

def update_contact_email(session, contact_id, new_email):
    """
    Update the email of a contact identified by contact_id.

    Parameters:
    session (Session): SQLAlchemy session object.
    contact_id (int): ID of the contact to update.
    new_email (str): New email address.
    """
    try:
        contact = session.query(Contact).filter(Contact.id == contact_id).one_or_none()
        if contact is None:
            print(f"No contact found with ID: {contact_id}")
            logging.warning(f"No contact found with ID: {contact_id} for email update.")
            return
        contact.email = new_email
        session.commit()
        print(f"Contact ID {contact_id}'s email updated to '{new_email}'.")
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

def search_contacts(session, keyword):
    """
    Search for contacts by name, email, or phone.

    Parameters:
    session (Session): SQLAlchemy session object.
    keyword (str): Search keyword.

    Returns:
    list of Contact: List containing matching Contact objects.
    """
    try:
        contacts = session.query(Contact).filter(
            (Contact.name.ilike(f"%{keyword}%")) |
            (Contact.email.ilike(f"%{keyword}%")) |
            (Contact.phone.ilike(f"%{keyword}%"))
        ).all()
        logging.debug(f"Search results for '{keyword}': {contacts}")
        return contacts
    except Exception as e:
        print(f"Error searching contacts: {e}")
        logging.error(f"Error searching contacts: {e}")
        return []

def main():
    db_url = "sqlite:///contacts.db"
    session, engine = setup_database(db_url)
    create_tables(engine)

    # Add Contacts
    add_contact(session, "Alice Smith", "alice@example.com", "555-1234")
    add_contact(session, "Bob Johnson", "bob@example.com", "555-5678")

    # Display Contacts
    contacts = get_all_contacts(session)
    display_contacts(contacts)

    # Update Contact Email
    update_contact_email(session, 1, "alice.smith@example.com")

    # Display Contacts After Update
    contacts = get_all_contacts(session)
    display_contacts(contacts)

    # Search Contacts
    keyword = "alice"
    search_results = search_contacts(session, keyword)
    print(f"\nSearch Results for '{keyword}':")
    display_contacts(search_results)

    # Delete a Contact
    delete_contact(session, 2)

    # Display Contacts After Deletion
    contacts = get_all_contacts(session)
    display_contacts(contacts)

    # Close Session and Engine
    session.close()
    engine.dispose()
    logging.info("Database session closed and engine disposed.")

if __name__ == "__main__":
    main()
