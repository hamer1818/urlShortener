# URL Shortener
[TR](#Türkçe) | [EN](#English)

## English
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

## Türkçe
FastAPI ve SQLite3 ile oluşturulmuş basit bir URL kısaltma servisi.

## Özellikler
- Uzun URL'leri kısa, paylaşılabilir bağlantılara dönüştürme
- SQLite3 veritabanı kullanarak kalıcı depolama
- Swagger belgeleri ile RESTful API
- Basit web arayüzü

## Gereksinimler
- Python 3.7+
- pip (Python paket yöneticisi)

## Kurulum
1. Depoyu klonlayın
```bash
git clone https://github.com/hamer1818/urlShortener.git
cd urlShortener
```
2. Gerekli paketleri yükleyin
```bash
pip install -r requirements.txt
```
3. FastAPI sunucusunu çalıştırın
```bash
uvicorn main:app --reload
```
Sunucu `http://127.0.0.1:8000` adresinde başlayacaktır.

## Kullanım
### Web Arayüzü
1. Tarayıcınızı açın ve `http://127.0.0.1:8000` adresine gidin.
2. Uzun bir URL'yi giriş alanına girin ve `Kısalt` düğmesine tıklayın.
3. Kısaltılmış URL'yi kopyalayın ve başkalarıyla paylaşın.

### RESTful API
#### Bir URL'yi Kısaltma
```bash
curl -X POST "http://127.0.0.1:8000/shorten/" \
     -H "Content-Type: application/json" \
     -d '{"original_url":"https://your-long-url.com"}'
```
### Swagger UI Kullanımı
1. Swagger UI'ye erişmek için `http://127.0.0.1:8000/docs` adresine gidin.
2. `/shorten` uç noktasına tıklayın ve ardından `Try it out` düğmesine tıklayın.
3. `original_url` alanına uzun URL'yi girin ve `Execute` düğmesine tıklayın.
4. Kısaltılmış URL, `Response body` bölümünde görüntülenecektir.

## Proje Yapısı
```bash
├── main.py         # FastAPI uygulaması ve rotaları
├── crud.py        # Veritabanı işlemleri
├── database.py    # Veritabanı yapılandırması
├── models.py      # SQLAlchemy modelleri
├── static/        # Statik dosyalar
└── requirements.txt
```

## Teknolojiler
- [FastAPI](https://fastapi.tiangolo.com/): Python 3.7+ ile API'ler oluşturmak için modern web çatısı
- [SQLite3](https://www.sqlite.org/index.html): Sunucusuz SQL veritabanı motoru
- [Tailwind CSS](https://tailwindcss.com/): İşlevsel ilk CSS çerçevesi
- [Pydantic](https://pydantic-docs.helpmanual.io/): Veri doğrulama ve ayrıştırma kütüphanesi
- [SQLAlchemy](https://www.sqlalchemy.org/): SQL araç seti ve Nesne-İlişkisel Eşleme (ORM) kütüphanesi
- [Uvicorn](https://www.uvicorn.org/): ASGI sunucusu uygulaması

## Lisans
Bu proje, ayrıntılar için [LICENSE](LICENSE) dosyasına bakın, MIT Lisansı ile lisanslanmıştır.
