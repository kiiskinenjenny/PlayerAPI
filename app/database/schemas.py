from pydantic import BaseModel


class EventBase(BaseModel):
    name: str
    year_published: int
    player_id: int

    class Config:
        orm_mode = True


class EventIn(BaseModel):
    name: str
    year_published: int

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


class EventInPlayer(BaseModel):
    """Käytetään pelaajan tietojen yhteydessä."""
    name: str
    year_published: int
    id: int

    class Config:
        orm_mode = True


class PlayerDb(PlayerBase):
    id: int
    events: list[EventInPlayer]


class PlayerAllListItem(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True