from fastapi import FastAPI
from .routes import router

app = FastAPI()

app.include_router(router, tags=["Event"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


"""
[
    {
        "id": 1,
        "name": "Test event 1",
        "date": "2024-03-06",
        "organizer": {
            "name": "fdev",
            "email": "fdev@example.com"
        },
        "status": "active",
        "type": "event",
        "joiners": [
            {
                "name": "Test User",
                "email": "test@test.com",
                "country": "Hungary"
            }
        ],
        "location": "Budapest, Hungary",
        "max_attendees": 100
    },
    {
        "id": 2,
        "name": "Test event 2",
        "date": "2024-03-06",
        "organizer": {
            "name": "fdev",
            "email": "fdev@example.com"
        },
        "status": "active",
        "type": "event",
        "joiners": [
            {
                "name": "Test User",
                "email": "test@test.com",
                "country": "Hungary"
            }
        ],
        "location": "Budapest, Hungary",
        "max_attendees": 50
    }
]

"""
