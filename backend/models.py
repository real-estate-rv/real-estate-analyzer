from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True)
    zillow_id = Column(String, unique=True, nullable=True)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    price = Column(Float)
    beds = Column(Integer)
    baths = Column(Float)
    sqft = Column(Float)
    section8_rent = Column(Float, nullable=True)
    crime_rate = Column(Float, nullable=True)
    tax_annual = Column(Float, nullable=True)
    kpis = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True)
    property_id = Column(Integer)
    analysis_type = Column(String)
    results = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
