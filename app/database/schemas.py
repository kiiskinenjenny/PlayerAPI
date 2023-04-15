from pydantic import BaseModel
import datetime


class EventBase(BaseModel):
    id: int
    type: str
    detail: str    
    timestamp: datetime.datetime
    player_id: int

    class Config:
        orm_mode = True


class EventIn(BaseModel):
    type: str
    detail: str 

    class Config:
        orm_mode = True


class EventPlayer(BaseModel):
    """Käytetään /events"""
    id: int
    name: str

    class Config:
        orm_mode = True


class EventDb(EventBase):
    id: int
    player: EventPlayer

    class Config:
        fields = {'player_id': {'exclude': True}}


class PlayerBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PlayerDb(PlayerBase):
    id: int
    events: list[EventBase]


class OnlyPlayerDb(PlayerBase):
    id: int


class PlayerAllListItem(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True      