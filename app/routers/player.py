from fastapi import APIRouter, status, Depends
from ..database.players_crud import read_all_players, save_player, read_player_by_id, save_event, read_player_by_type, read_event_by_player, type_error
from ..database import players_crud as crud
from ..database.schemas import PlayerBase, PlayerDb, OnlyPlayerDb, PlayerAllListItem, EventDb, EventIn, EventBase
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/players')


@router.get('', response_model=list[PlayerAllListItem])
def read_players(db: Session = Depends(get_db)):
    return read_all_players(db)


@router.post('', response_model=OnlyPlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerBase, db: Session = Depends(get_db)):
    return save_player(player_in, db)


@router.get('/{id}', response_model=PlayerDb)
def read_player_id(id: int, db: Session = Depends(get_db)):
    return read_player_by_id(db, id)


@router.get('/{id}/events', response_model=list[EventBase])
def read_event_by_id(id: int, type: str = '', db: Session = Depends(get_db)):
    if id != '' and type == '':
        return read_event_by_player(db, id)
    if id != '' and type != '':
        return read_player_by_type(db, type, id)


@router.post('/{id}/events', response_model=EventDb, status_code=status.HTTP_201_CREATED)
def create_event_for_player(id: int, event_in: EventIn, db: Session = Depends(get_db)):
    if event_in.type == 'level_started' or event_in.type == 'level_solved':
        return save_event(id, event_in, db)
    return type_error()
    