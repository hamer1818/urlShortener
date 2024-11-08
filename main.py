from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import crud
import models
from database import SessionLocal, init_db
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from pathlib import Path
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
class URLRequest(BaseModel):
    original_url: str

@app.post("/shorten/")
def shorten_url(request: URLRequest, db: Session = Depends(get_db)):
    original_url = request.original_url
    db_url = crud.get_url_by_original(db, original_url)
    if db_url:
        return {"shortened_url": db_url.shortened_url}
    db_url = crud.create_shortened_url(db, original_url)
    return {"shortened_url": db_url.shortened_url}

# Kısa URL'yi orijinaline yönlendirme endpoint'i
@app.get("/{shortened_url}")
def redirect_to_original(shortened_url: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_shortened(db, shortened_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=db_url.original_url)

# Statik dosyaları servis et
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(
        content=Path("static/index.html").read_text(encoding="utf-8"),
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
    )

# Statik dosyaları kök dizinde servis et
app.mount("/", StaticFiles(directory="static", html=True), name="static")
