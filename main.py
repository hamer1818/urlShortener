from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
from database import SessionLocal, init_db

# Uygulamayı başlatıyoruz
app = FastAPI()

# Uygulama ilk başladığında veritabanını başlat
@app.on_event("startup")
def startup_event():
    init_db()

# Veritabanı oturumu oluştur
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# URL kısaltma endpoint'i
@app.post("/shorten/")
def shorten_url(original_url: str, db: Session = Depends(get_db)):
    # Daha önce kısaltılmış mı kontrol et
    db_url = crud.get_url_by_original(db, original_url)
    if db_url:
        return {"shortened_url": db_url.shortened_url}
    
    # Yeni kısa URL oluştur
    db_url = crud.create_shortened_url(db, original_url)
    return {"shortened_url": db_url.shortened_url}

# Kısa URL'yi orijinaline yönlendirme endpoint'i
@app.get("/{shortened_url}")
def redirect_to_original(shortened_url: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_shortened(db, shortened_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"original_url": db_url.original_url}
