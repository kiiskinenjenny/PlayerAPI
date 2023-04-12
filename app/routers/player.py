from fastapi import APIRouter, Depends
from ..database.players_crud import read_all_players, save_player, read_player_by_id, save_event, read_player_by_name
from ..database.schemas import PlayerBase, PlayerDb, PlayerAllListItem, EventDb, EventIn
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/players')

#DONE
@router.get('', response_model=list[PlayerAllListItem])
def read_players(name: str = '', db: Session = Depends(get_db)):
    if name != '':
        return read_player_by_name(db, name)
    return read_all_players(db)


@router.post('', response_model=PlayerDb)
def create_player(player_in: PlayerBase, db: Session = Depends(get_db)):
    return save_player(player_in, db)


@router.get('/{id}', response_model=PlayerDb)
def read_player_id(id: int, db: Session = Depends(get_db)):
    return read_player_by_id(db, id)


@router.post('/{id}/events', response_model=EventDb)
def add_event_for_player(id: int, event_in: EventIn, db: Session = Depends(get_db)):
    return save_event(id, event_in, db)