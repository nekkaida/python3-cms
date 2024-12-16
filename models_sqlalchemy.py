# models_sqlalchemy.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Contact(Base):
    """
    Contact model mapped to the 'contacts' table.
    """
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Contact(id={self.id}, name='{self.name}', email='{self.email}', phone='{self.phone}')>"
