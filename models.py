from sqlalchemy import Column, Integer, Float, String, Date, Boolean, DateTime
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///test.db')

Base = declarative_base()

Session = sessionmaker(bind=engine)
db = Session()


class ModelMixin:
    def __getitem__(self, key):
        return getattr(self, key)

    def keys(self):
        return inspect(self).attrs.keys()


class Place(Base, ModelMixin):
    __tablename__ = 'place'
    PlaceId = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    PlaceName = Column(String)
    PlaceLocation = Column(String)

    @staticmethod
    def get_or_create(id):
        asset = db.query(Place).filter_by(PlaceId=id).first()
        if asset is None:
            entry = Place(PlaceId=id)
            db.add(entry)
            db.commit()
        return db.query(Place).filter_by(PlaceId=id).first()


class Event(Base, ModelMixin):
    __tablename__ = 'event'
    PlaceId = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    EventName = Column(String)
    Since = Column(DateTime)
    Until = Column(DateTime)
    EventTicketCount = Column(Integer)
    AvailableTicketCount = Column(Integer)

    @staticmethod
    def get_or_create(id):
        asset = db.query(Event).filter_by(PlaceId=id).first()
        if asset is None:
            entry = Event(PlaceId=id)
            db.add(entry)
            db.commit()
        return db.query(Event).filter_by(PlaceId=id).first()


class Booking(Base, ModelMixin):
    __tablename__ = 'booking'
    BookingId = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    EventId = Column(Integer)
    TicketCount = Column(Integer)
    Name = Column(String)

    @staticmethod
    def get_or_create(id):
        asset = db.query(Booking).filter_by(BookingId=id).first()
        if asset is None:
            entry = Booking(BookingId=id)
            db.add(entry)
            db.commit()
        return db.query(Booking).filter_by(BookingId=id).first()


Base.metadata.create_all(engine)
