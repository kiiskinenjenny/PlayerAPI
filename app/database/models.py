from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    events = relationship('Event', back_populates='player')


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    year_published = Column(Integer, nullable=False)
    player_id = Column(Integer, ForeignKey('players.id'))

    player = relationship('Player', back_populates='events')