from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Tablolar için Base sınıfı oluşturuyoruz
Base = declarative_base()

class URL(Base):
    __tablename__ = 'urls'  # Tablomuzun adı
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, unique=True, nullable=False)
    shortened_url = Column(String, unique=True, nullable=False)
