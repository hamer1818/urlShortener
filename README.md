# URL Shortener
A simple URL shortener using fastapi and sqlite3.

## Installation
1. Clone the repository
```bash
git clone https://github.com/hamer1818/urlShortener.git
```
2. Install the dependencies
```bash
pip install -r requirements.txt
```
3. Run the server
```bash
uvicorn main:app --reload
```

## Usage
1. Open the browser and go to `http://127.0.0.1:8000/docs`
2. Enter the URL you want to shorten in the `POST /shorten` section
3. Click on the `Try it out` button
4. Enter the URL in the `url` field and click on the `Execute` button
5. The shortened URL will be displayed in the `Response body` section

