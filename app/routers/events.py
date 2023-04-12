from fastapi import APIRouter, Depends
from ..database import events_crud as crud
from ..database.database import get_db
from sqlalchemy.orm import Session
from ..database.schemas import EventDb


router = APIRouter(prefix='/events')


@router.get('', response_model=list[EventDb])
def read_events(db: Session = Depends(get_db)):
    return crud.read_all_events(db)


@router.get('/{id}', response_model=EventDb)
def read_by_id(id: int, db: Session = Depends(get_db)):
    return crud.read_event_by_id(id, db)


@router.delete('/{id}')
def delete_by_id(id: int, db: Session = Depends(get_db)):
    return crud.delete_event_by_id(id, db)