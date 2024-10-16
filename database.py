from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# SQLite veritabanı bağlantısı
DATABASE_URL = "sqlite:///./url_shortener.db"

# Veritabanı motoru oluşturuyoruz
engine = create_engine(DATABASE_URL)

# Oturum (session) oluşturucu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Veritabanındaki tabloları oluşturuyoruz
def init_db():
    Base.metadata.create_all(bind=engine)
