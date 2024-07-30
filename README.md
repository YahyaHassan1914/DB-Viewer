# Flask Database Viewer

A simple Flask application that connects to a MySQL database, displays available databases, and allows users to navigate through tables and view their contents.

## Features

- Display a list of databases.
- Clickable links to view tables in each database.
- Clickable links to view the contents of each table.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- MySQL server
- A MySQL database to connect to

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd flask-database-viewer
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install Flask mysql-connector-python
   ```

4. **Create a JSON configuration file for database connection:**

   Create a file named `db_config.json` in the project root directory with the following content:

   ```json
   {
       "host": "localhost",
       "user": "your_username",
       "password": "your_password"
   }
   ```

   Replace `your_username` and `your_password` with your actual MySQL credentials.

## Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

2. **Open your web browser and go to:**

   ```
   http://127.0.0.1:5000/
   ```

3. **Navigate through the application:**

   - Click on a database name to view its tables.
   - Click on a table name to view its contents.

## Project Structure

```
flask-database-viewer/
├── app.py                # Main application file
├── db_config.json        # Database configuration file
├── static/               # Static files (CSS)
│   └── css/
│       └── styles.css    # CSS styles
└── templates/            # HTML templates
    ├── index.html        # Template for displaying databases
    ├── database.html     # Template for displaying tables in a database
    └── table.html        # Template for displaying table contents
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/) - MySQL database driver for Python.
```