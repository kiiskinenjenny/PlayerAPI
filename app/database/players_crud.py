from fastapi import HTTPException
from .schemas import PlayerBase, EventBase
from sqlalchemy.orm import Session
from . import models


def delete_player_by_id(id: int, db: Session):
    rel = db.query(models.Player).filter(models.Player.id == id).first()
    if rel is None:
        raise HTTPException(status_code=404, detail='Player not found')
    db.delete(rel)
    db.commit()
    return {'message': 'deleted'}

#DONE
def read_all_players(db: Session):
    return db.query(models.Player).all()

#DONE
def save_player(player_in: PlayerBase, db: Session):
    player = models.Player(**player_in.dict())
    if player is None:
        raise HTTPException(status_code=422, detail='player can not be created')
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

#DONE
def read_player_by_id(db: Session, id: int):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(status_code=404, detail='player not found')
    return player

#DONE
def read_event_by_player(db: Session, id: int):
    player = db.query(models.Event).filter(models.Event.player_id == id).all()
    allPlayers = db.query(models.Player).filter(models.Player.id == id).first()
    if allPlayers is None:
        raise HTTPException(status_code=404, detail='player not found')
    else:
        return player  

#DONE
def read_player_by_type(db: Session, type: str, id: int):
    event = db.query(models.Event).filter(models.Event.player_id == id, models.Event.type == type).all()
    allEvents = db.query(models.Event).filter(models.Event.type == type).first()
    if allEvents is None:
        raise HTTPException(status_code=400, detail='unknown event type')
    else:
        return event


def save_event(id: int, event_in: EventBase, db: Session):
    rel = models.Event(**event_in.dict(), player_id=id)
    allPlayers = db.query(models.Player).filter(models.Player.id == id).first()
    if allPlayers is None:
        raise HTTPException(status_code=404, detail='player not found')
    if rel.type is not str:
        raise HTTPException(status_code=422, detail='event can not be created')
    db.add(rel)
    db.commit()
    db.refresh(rel)
    return rel