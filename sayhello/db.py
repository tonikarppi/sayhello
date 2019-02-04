import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Unicode, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


class Message(Base):
    """
    This model represents a `message` in the database.
    """
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    date_posted = Column(DateTime, nullable=False)
    text = Column(Unicode(300))

    def __repr__(self):
        return f'Message({self.id}, {self.date_posted})'


# Connects to the database.
db_url = os.environ.get('DB_URL', default='sqlite:///dev.db')
engine = create_engine(db_url)

# Creates the scoped session factory.
Session = scoped_session(sessionmaker(bind=engine))


def create_tables():
    Base.metadata.create_all(engine)


__all__ = ['Session', 'Message', 'create_tables']
