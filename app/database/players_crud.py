from fastapi import HTTPException
from .schemas import PlayerBase, EventBase
from sqlalchemy.orm import Session
from . import models


def read_all_players(db: Session):
    player = db.query(models.Player).all()
    return player


def save_player(player_in: PlayerBase, db: Session):
    player = models.Player(**player_in.dict())
    if player is None:
        raise HTTPException(status_code=422, detail='Player can not be created')
    db.add(player)
    db.commit()
    db.refresh(player)
    return player


def read_player_by_id(db: Session, id: int):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(status_code=404, detail='Player not found')
    return player


def read_event_by_player(db: Session, id: int):
    player = db.query(models.Event).filter(models.Event.player_id == id).all()
    allPlayers = db.query(models.Player).filter(models.Player.id == id).first()
    if allPlayers is None:
        raise HTTPException(status_code=404, detail='Player not found')
    else:
        return player  


def read_player_by_type(db: Session, type: str, id: int):
    event = db.query(models.Event).filter(models.Event.player_id == id, models.Event.type == type).all()
    allEvents = db.query(models.Event).filter(models.Event.type == type).first()
    if allEvents is None:
        raise HTTPException(status_code=400, detail='Bad Request')
    else:
        return event


def save_event(id: int, event_in: EventBase, db: Session):
    rel = models.Event(**event_in.dict(), player_id=id)
    allPlayers = db.query(models.Player).filter(models.Player.id == id).first()
    if allPlayers is None:
        raise HTTPException(status_code=404, detail='Player not found')
    db.add(rel)
    db.commit()
    db.refresh(rel)
    return rel


def type_error():
    raise HTTPException(status_code=404, detail='Type must be either level_started or level_solved')