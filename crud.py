from sqlalchemy.orm import Session
from models import URL
import string, random

# Rastgele 6 karakterli bir kısa URL üretici
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# Veritabanına URL kaydetme
def create_shortened_url(db: Session, original_url: str):
    short_url = generate_short_url()
    db_url = URL(original_url=original_url, shortened_url=short_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

# Orijinal URL'yi getir
def get_url_by_shortened(db: Session, shortened_url: str):
    return db.query(URL).filter(URL.shortened_url == shortened_url).first()

# Orijinal URL'nin veritabanında olup olmadığını kontrol et
def get_url_by_original(db: Session, original_url: str):
    return db.query(URL).filter(URL.original_url == original_url).first()
