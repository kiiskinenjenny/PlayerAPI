from fastapi import APIRouter, Depends
from ..database.events_crud import read_all_events, delete_event_by_id, read_player_by_type
from ..database.database import get_db
from sqlalchemy.orm import Session
from ..database.schemas import EventAllListItem


router = APIRouter(prefix='/events')


@router.get('', response_model=list[EventAllListItem])
def read_events(type: str = '', db: Session = Depends(get_db)):
    if type != '':
        return read_player_by_type(db, type)
    else:
        return read_all_events(db)