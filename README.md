# URL Shortener
A simple URL shortener service built with FastAPI and SQLite3.

## Features
- Shorten long URLs into compact, shareable links
- Persistent storage using SQLite3 database
- RESTful API with Swagger documentation
- Simple web interface

## Prerequisites
- Python 3.7+
- pip (Python package manager)

## Installation
1. Clone the repository
```bash
git clone https://github.com/hamer1818/urlShortener.git
cd urlShortener
```
2. Install the required packages
```bash
pip install -r requirements.txt
```
3. Run the FastAPI server
```bash
uvicorn main:app --reload
```
The server will be start at `http://127.0.0.1:8000`.

## Usage
### Web Interface
1. Open your browser and navigate to `http://127.0.0.1:8000`.
2. Enter a long URL in the input field and click on the `Shorten` button.
3. Copy the shortened URL and share it with others.

### RESTful API
#### Shorten a URL
```bash
curl -X POST "http://127.0.0.1:8000/shorten/" \
     -H "Content-Type: application/json" \
     -d '{"original_url":"https://your-long-url.com"}'
```
### Using Swagger UI
1. Navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI.
2. Click on the `/shorten` endpoint and then click on the `Try it out` button.
3. Enter the long URL in the `original_url` field and click on the `Execute` button.
4. The shortened URL will be displayed in the `Response body` section.

## Project Structure
```bash
├── main.py         # FastAPI application and routes
├── crud.py        # Database operations
├── database.py    # Database configuration
├── models.py      # SQLAlchemy models
├── static/        # Static files
└── requirements.txt
```

## Technologies
- [FastAPI](https://fastapi.tiangolo.com/): Modern web framework for building APIs with Python 3.7+
- [SQLite3](https://www.sqlite.org/index.html): Serverless SQL database engine
- [Tailwind CSS](https://tailwindcss.com/): Utility-first CSS framework
- [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation and parsing library
- [SQLAlchemy](https://www.sqlalchemy.org/): SQL toolkit and Object-Relational Mapping (ORM) library
- [Uvicorn](https://www.uvicorn.org/): ASGI server implementation

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
