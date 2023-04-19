from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models


def read_all_events(db: Session):
    events = db.query(models.Event).all()
    return events


def read_player_by_type(db: Session, type: str):
    event = db.query(models.Event).filter(models.Event.type == type).all()
    allEvents = db.query(models.Event).filter(models.Event.type == type).first()
    if allEvents is None:
        raise HTTPException(status_code=400, detail='Bad Request')
    else:
        return event










def read_event_by_id(id: int, db: Session):
    rel = db.query(models.Event).filter(models.Event.id == id).first()
    if rel is None:
        raise HTTPException(status_code=404, detail='Events not found')
    return rel


def delete_event_by_id(id: int, db: Session):
    rel = db.query(models.Event).filter(models.Event.id == id).first()
    if rel is None:
        raise HTTPException(status_code=404, detail='Event not found')
    db.delete(rel)
    db.commit()
    return {'message': 'deleted'}