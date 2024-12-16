# Contact Management System

*An efficient and user-friendly Contact Management System built with Python 3 and SQLAlchemy, featuring a Command-Line Interface (CLI) for seamless operations.*

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Demo](#demo)
4. [Technologies Used](#technologies-used)
5. [Prerequisites](#prerequisites)
6. [Installation](#installation)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Navigate to the Project Directory](#2-navigate-to-the-project-directory)
    - [3. Set Up a Virtual Environment](#3-set-up-a-virtual-environment)
    - [4. Activate the Virtual Environment](#4-activate-the-virtual-environment)
    - [5. Install Dependencies](#5-install-dependencies)
7. [Configuration](#configuration)
    - [1. `config.ini` File](#1-configini-file)
8. [Usage](#usage)
    - [Running the CLI](#running-the-cli)
    - [Available Commands](#available-commands)
        - [Add a Contact](#add-a-contact)
        - [List All Contacts](#list-all-contacts)
        - [List Contacts with Pagination](#list-contacts-with-pagination)
        - [Update a Contact](#update-a-contact)
        - [Delete a Contact](#delete-a-contact)
        - [Search Contacts](#search-contacts)
9. [Project Structure](#project-structure)
10. [Testing](#testing)
    - [Running Unit Tests](#running-unit-tests)
11. [Logging](#logging)
12. [Contributing](#contributing)
13. [License](#license)
14. [Acknowledgments](#acknowledgments)
15. [Contact](#contact)

---

## Project Overview

The **Contact Management System** is a robust application designed to help users efficiently manage their contacts through a Command-Line Interface (CLI). Leveraging the power of **Python 3** and **SQLAlchemy**, this system allows for seamless Create, Read, Update, and Delete (CRUD) operations, ensuring data integrity and ease of use.

**Key Objectives:**

- **Simplicity:** Provide an intuitive CLI for managing contacts without the need for a graphical interface.
- **Efficiency:** Utilize SQLAlchemy's ORM capabilities for effective database interactions.
- **Scalability:** Design the system to accommodate future enhancements and integrations.
- **Maintainability:** Ensure clean, modular, and well-documented code for easy maintenance and collaboration.

---

## Features

- **Add Contacts:** Create new contact entries with essential details.
- **List Contacts:** View all contacts in a structured and readable format.
- **Update Contacts:** Modify existing contact information as needed.
- **Delete Contacts:** Remove contacts from the database effortlessly.
- **Search Contacts:** Quickly find contacts using various criteria.
- **Pagination:** Handle large datasets by viewing contacts page by page.
- **Input Validation:** Ensure data integrity through robust input validation.
- **Logging:** Maintain detailed logs of all operations and errors for monitoring and debugging.

---

## Demo

*While a live demo is not available, here's a walkthrough of typical CLI interactions:*

```bash
# Adding a new contact
$ python3 main.py add --name "John Doe" --email "john.doe@example.com" --phone "555-1234"
Contact 'John Doe' added successfully with ID 1.

# Listing all contacts
$ python3 main.py list
╭────────────────────────────────────────────────────────────────────────╮
│                             List of Contacts                            │
├────┬───────────┬───────────────────────────┬───────────┤
│ ID │ Name      │ Email                     │ Phone     │
├────┼───────────┼───────────────────────────┼───────────┤
│ 1  │ John Doe  │ john.doe@example.com      │ 555-1234  │
│ 2  │ Jane Smith│ jane.smith@example.com    │ 555-5678  │
╰────┴───────────┴───────────────────────────┴───────────╯

# Updating a contact's email
$ python3 main.py update --id 1 --email "john.new@example.com"
Contact ID 1 has been updated.

# Deleting a contact
$ python3 main.py delete --id 2
Contact with ID 2 has been deleted.

# Searching for a contact
$ python3 main.py search --name "John"
╭────────────────────────────────────────────────────────────────────────╮
│                             Search Results                              │
├────┬───────────┬───────────────────────────┬───────────┤
│ ID │ Name      │ Email                     │ Phone     │
├────┼───────────┼───────────────────────────┼───────────┤
│ 1  │ John Doe  │ john.new@example.com      │ 555-1234  │
╰────┴───────────┴───────────────────────────┴───────────╯
```

---

## Technologies Used

- **Python 3:** The core programming language used for developing the application.
- **SQLAlchemy:** An ORM (Object Relational Mapper) facilitating database interactions.
- **SQLite:** A lightweight, file-based relational database system.
- **Argparse:** A module for parsing command-line options, arguments, and sub-commands.
- **Rich:** A Python library for rich text and beautiful formatting in the terminal.
- **Tabulate:** A library to display tabular data in a visually appealing format.
- **Unittest:** Python's built-in testing framework for writing and running tests.

---

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- **Python 3.6 or higher:** Verify your Python version by running:
  
  ```bash
  python3 --version
  ```
  
  *Expected output:*
  
  ```
  Python 3.8.10
  ```

- **pip:** Python's package installer. It typically comes bundled with Python 3. If not, you can install it following [pip's official installation guide](https://pip.pypa.io/en/stable/installation/).

- **Git:** For version control and committing to GitHub. Verify by running:
  
  ```bash
  git --version
  ```
  
  *If Git is not installed, download and install it from [git-scm.com](https://git-scm.com/downloads).*

---

## Installation

Follow these steps to set up the **Contact Management System** on your local machine.

### 1. Clone the Repository

Start by cloning the repository from GitHub to your local machine.

```bash
git clone https://github.com/nekkaida/contact_manager.git
```

### 2. Navigate to the Project Directory

Change your current directory to the project's root directory.

```bash
cd contact_manager
```

### 3. Set Up a Virtual Environment

Creating a virtual environment ensures that project dependencies are isolated from other Python projects on your system.

```bash
python3 -m venv venv
```

*This command creates a virtual environment named `venv` inside your project directory.*

### 4. Activate the Virtual Environment

- **On Unix or MacOS:**

  ```bash
  source venv/bin/activate
  ```

- **On Windows:**

  ```cmd
  venv\Scripts\activate
  ```

*After activation, your terminal prompt will typically be prefixed with `(venv)`, indicating that the virtual environment is active.*

### 5. Install Dependencies

With the virtual environment activated, install the required Python packages using `pip`.

```bash
pip install -r requirements.txt
```

*This command reads the `requirements.txt` file and installs all listed dependencies.*

---

## Configuration

Proper configuration is essential for the application to function correctly. This involves setting up the `config.ini` file with appropriate settings.

### 1. `config.ini` File

The `config.ini` file contains configuration settings for the database and logging. Here's how to set it up:

1. **Create and Open `config.ini`:**

   If the file doesn't already exist, create it:

   ```bash
   nano config.ini
   ```

2. **Add the Following Content:**

   ```ini
   [database]
   db_url = sqlite:///contacts.db

   [logging]
   log_file = contact_manager.log
   log_level = DEBUG
   ```

   **Explanation:**

   - **`[database]` Section:**
     - **`db_url`**: Specifies the database connection URL. Here, `sqlite:///contacts.db` indicates a SQLite database named `contacts.db` located in the project directory.

   - **`[logging]` Section:**
     - **`log_file`**: The file where logs will be stored.
     - **`log_level`**: The logging level, determining the verbosity of logs. Common levels include `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

3. **Save and Close the File:**

   - **In Nano:** Press `Ctrl + X`, then `Y`, and hit `Enter`.
   - **In Other Editors:** Save the file as per the editor's instructions.

---

## Usage

Interact with the Contact Management System using the Command-Line Interface (CLI). The CLI provides various commands to manage your contacts effectively.

### Running the CLI

Ensure your virtual environment is activated. Then, use the `main.py` script to perform operations.

```bash
python3 main.py [command] [options]
```

### Available Commands

The application supports the following commands:

1. **Add a Contact**

   **Description:** Create a new contact entry with name, email, and phone number.

   **Usage:**

   ```bash
   python3 main.py add --name "John Doe" --email "john.doe@example.com" --phone "555-1234"
   ```

   **Options:**

   - `--name`: (Required) The full name of the contact.
   - `--email`: (Required) The email address of the contact.
   - `--phone`: (Required) The phone number of the contact.

   **Example:**

   ```bash
   python3 main.py add --name "Alice Smith" --email "alice@example.com" --phone "555-5678"
   ```

2. **List All Contacts**

   **Description:** Display all contacts in a formatted table.

   **Usage:**

   ```bash
   python3 main.py list
   ```

   **Options:**

   - `--page`: (Optional) The page number to display. Default is `1`.
   - `--per_page`: (Optional) Number of contacts per page. Default is `10`.

   **Example:**

   ```bash
   python3 main.py list --page 2 --per_page 5
   ```

3. **Update a Contact**

   **Description:** Modify the email and/or phone number of an existing contact by specifying their ID.

   **Usage:**

   ```bash
   python3 main.py update --id 1 --email "new.email@example.com" --phone "555-9876"
   ```

   **Options:**

   - `--id`: (Required) The unique ID of the contact to update.
   - `--email`: (Optional) The new email address.
   - `--phone`: (Optional) The new phone number.

   **Note:** At least one of `--email` or `--phone` must be provided.

   **Example:**

   ```bash
   python3 main.py update --id 2 --email "jane.new@example.com"
   ```

4. **Delete a Contact**

   **Description:** Remove a contact from the database using their unique ID.

   **Usage:**

   ```bash
   python3 main.py delete --id 1
   ```

   **Options:**

   - `--id`: (Required) The unique ID of the contact to delete.

   **Example:**

   ```bash
   python3 main.py delete --id 3
   ```

5. **Search Contacts**

   **Description:** Find contacts based on name, email, or phone number.

   **Usage:**

   ```bash
   python3 main.py search --name "John" --email "example.com" --phone "555"
   ```

   **Options:**

   - `--name`: (Optional) Search by contact name.
   - `--email`: (Optional) Search by email address.
   - `--phone`: (Optional) Search by phone number.

   **Note:** At least one of `--name`, `--email`, or `--phone` must be provided.

   **Example:**

   ```bash
   python3 main.py search --email "alice@example.com"
   ```

---

## Project Structure

Understanding the project structure aids in navigation and maintenance. Here's an overview of the project's directory and file organization:

```
contact_manager/
├── config.ini
├── exceptions.py
├── models_sqlalchemy.py
├── sqlalchemy_crud_example.py
├── main.py
├── requirements.txt
├── test_contact_manager.py
├── contact_manager.log
└── contacts.db
```

**Description of Files:**

- **`config.ini`**: Configuration file containing database URL and logging settings.
- **`exceptions.py`**: Defines custom exception classes for specific error handling.
- **`models_sqlalchemy.py`**: Contains SQLAlchemy ORM models representing database tables.
- **`sqlalchemy_crud_example.py`**: Demonstrative script showcasing CRUD operations using SQLAlchemy.
- **`main.py`**: The primary CLI script for interacting with the Contact Management System.
- **`requirements.txt`**: Lists all Python dependencies required for the project.
- **`test_contact_manager.py`**: Contains unit tests to verify the functionality of the application.
- **`contact_manager.log`**: Log file recording all operations and errors (generated after running the application).
- **`contacts.db`**: SQLite database file storing all contact information (generated after running the application).

---

## Testing

Ensuring your application works as intended is crucial. Unit tests help verify that individual components function correctly and aid in maintaining code reliability.

### Running Unit Tests

1. **Ensure the Virtual Environment is Activated:**

   ```bash
   source venv/bin/activate  # On Unix or MacOS
   # or
   venv\Scripts\activate     # On Windows
   ```

2. **Run the Tests:**

   ```bash
   python3 test_contact_manager.py
   ```

   **Expected Output:**

   ```
   ....
   ----------------------------------------------------------------------
   Ran 4 tests in 0.005s

   OK
   ```

   *Each dot (`.`) represents a passed test.*

### Understanding the Tests

The `test_contact_manager.py` file contains tests for the primary functionalities:

- **Adding a Contact**
- **Updating a Contact's Email**
- **Deleting a Contact**
- **Handling Deletion of a Non-existent Contact**

These tests ensure that the CRUD operations perform as expected and that the application gracefully handles error scenarios.

---

## Logging

The application maintains a detailed log of all operations and errors, aiding in monitoring and debugging.

- **Log File:** `contact_manager.log`
  
  **Location:** Located in the project's root directory.

- **Log Levels:**
  
  - **DEBUG:** Detailed information, typically of interest only when diagnosing problems.
  - **INFO:** Confirmation that things are working as expected.
  - **WARNING:** An indication that something unexpected happened, or indicative of some problem in the near future.
  - **ERROR:** Due to a more serious problem, the software has not been able to perform some function.
  - **CRITICAL:** A serious error, indicating that the program itself may be unable to continue running.

- **Configuration:**
  
  The log level and log file are configurable via the `config.ini` file under the `[logging]` section.

  ```ini
  [logging]
  log_file = contact_manager.log
  log_level = DEBUG
  ```

  *Adjust the `log_level` as needed to control the verbosity of the logs.*

- **Viewing Logs:**
  
  Use any text editor or command-line tools to view the log file.

  ```bash
  cat contact_manager.log
  ```

  *Or for real-time monitoring:*

  ```bash
  tail -f contact_manager.log
  ```

---

## Contributing

Contributions are welcome! Whether it's fixing bugs, improving documentation, or adding new features, your input is valuable.

### How to Contribute

1. **Fork the Repository:**

   Click the **"Fork"** button at the top-right corner of the repository page on GitHub.

2. **Clone Your Fork:**

   ```bash
   git clone https://github.com/nekkaida/contact_manager.git
   cd contact_manager
   ```

3. **Create a New Branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes:**

   Implement your feature or fix the bug. Ensure that you follow the project's coding standards and include relevant documentation.

5. **Add and Commit Changes:**

   ```bash
   git add .
   git commit -m "Add feature: your feature description"
   ```

6. **Push to Your Fork:**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request:**

   - Navigate to your fork on GitHub.
   - Click the **"Compare & pull request"** button.
   - Provide a clear and descriptive title and description for your PR.
   - Submit the pull request.

### Code of Conduct

Please adhere to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/) in all interactions with the project.

---

## License

This project is licensed under the [MIT License](LICENSE).

**Summary:**

- **Permission** is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

- **Conditions:** The above copyright notice and this permission notice shall be
  included in all copies or substantial portions of the Software.

- **Disclaimer:** THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
  OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
  IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
  WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## Acknowledgments

- **[SQLAlchemy](https://www.sqlalchemy.org/):** A powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **[Rich](https://github.com/Textualize/rich):** A Python library for rich text and beautiful formatting in the terminal.
- **[Tabulate](https://github.com/astanin/python-tabulate):** A library to display tabular data in a visually appealing format.
- **[Argparse](https://docs.python.org/3/library/argparse.html):** A module for parsing command-line options, arguments, and sub-commands.
- **[Unittest](https://docs.python.org/3/library/unittest.html):** Python's built-in testing framework.
- **[Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/):** Code of Conduct for open-source projects.

---

## Contact

For any inquiries, suggestions, or support, please reach out:

- **Kenneth Riadi Nugroho**
- **Email:** nekkaida@gmail.com
- **GitHub:** [github.com/nekkaida](https://github.com/nekkaida)

*Alternatively, you can open an issue on the GitHub repository to discuss any aspect of the project.*

---
