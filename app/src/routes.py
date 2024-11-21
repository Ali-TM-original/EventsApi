from fastapi import APIRouter, HTTPException
from typing import List
from json import JSONDecodeError
from .models import Event
from .file_storage import EventFileManager
from .event_analyzer import EventAnalyzer

router = APIRouter()
events = EventFileManager()
analyzer = EventAnalyzer()

# done
@router.get("/events", response_model=List[Event])
async def get_all_events():
    try:
        return events.read_events_from_file()
    except JSONDecodeError:
        raise HTTPException(status_code=404, detail="Could not read data")


# done
@router.get("/events/filter", response_model=List[Event])
async def get_events_by_filter(
    date: str = None, organizer: str = None, status: str = None, event_type: str = None
):
    res = events.get_filtered_events(date, organizer, status, event_type)
    if res == []:
        raise HTTPException(status_code=404, detail="Could not find such event")
    return res


# done
@router.get("/events/{event_id}", response_model=Event)
async def get_event_by_id(event_id: int):
    event = events.get_events_by_id(event_id)
    if event == "":
        raise HTTPException(
            status_code=404, detail=f"Event with ID {event_id} not Found"
        )
    return event


@router.post("/events", response_model=Event)
async def create_event(event: Event):
    if not events.create_event(event):
        raise HTTPException(status_code=500, detail="Could not create event")
    return event


# done
@router.put("/events/{event_id}", response_model=Event)
async def update_event(event_id: int, event: Event):
    if not events.update_by_id(event_id, event):
        raise HTTPException(status_code=404, detail=f"Event with {event_id} not Found")
    return event


# done
@router.delete("/events/{event_id}")
async def delete_event(event_id: int):
    if not events.delete_by_id(event_id):
        raise HTTPException(status_code=404, detail=f"Event with {event_id} not Found")
    return {"details": f"Event {event_id} deleted"}


# ask professor
@router.get("/events/joiners/multiple-meetings")
async def get_joiners_multiple_meetings():
    allevents = events.read_events_from_file()
    return analyzer.get_joiners_multiple_meetings_method(allevents)
