from fastapi import HTTPException
from .schemas import PlayerBase, EventBase
from sqlalchemy.orm import Session
from . import models


def read_all_players(db: Session):
    return db.query(models.Player).all()


def read_player_by_id(db: Session, id: int):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(status_code=404, detail='player not found')
    return player


def read_player_by_name(db: Session, name: str):
    player = db.query(models.Player).filter(models.Player.name == name).all()
    if player is None:
        raise HTTPException(status_code=404, detail='player not found')
    return player


def save_player(player_in: PlayerBase, db: Session):
    player = models.Player(**player_in.dict())
    db.add(player)
    db.commit()
    db.refresh(player)
    return player


def save_event(id: int, event_in: EventBase, db: Session):
    rel = models.Event(**event_in.dict(), player_id=id)
    db.add(rel)
    db.commit()
    db.refresh(rel)
    return rel