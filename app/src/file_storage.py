import os
import json
from .models import Event


class EventFileManager:

    def __init__(self) -> None:
        self.FILE_PATH = "events.json"
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
        self.json_file_path = os.path.join(project_root, "event.json")

    def read_events_from_file(self):
        events = ""
        with open(self.json_file_path) as file:
            events = json.load(file)
        return events

    def get_events_by_id(self, id: int):
        events = self.read_events_from_file()
        for e in events:
            if e["id"] == id:
                return e
        return ""

    def get_filtered_events(
        self,
        date: str = None,
        organizer: str = None,
        status: str = None,
        event_type: str = None,
    ):
        events = self.read_events_from_file()
        return [
            e
            for e in events
            if (
                (date is None or e["date"] == date)
                and (status is None or e["status"] == status)
                and (event_type is None or e["type"] == event_type)
                and (organizer is None or e["organizer"]["name"] == organizer)
            )
        ]

    def create_event(self, e: Event):
        events = self.read_events_from_file()
        events.append(e.model_dump())
        with open(self.json_file_path, "w") as file:
            try:
                json.dump(events, file, indent=4)
            except Exception as e:
                print(e)
                return False
        return True

    def get_joiner_meetings(self, joiner: str):
        events = self.read_events_from_file()
        return [
            e
            for e in events
            if ([j for j in e["joiners"] if j["name"] == joiner]) != []
        ]

    def delete_by_id(self, id: int) -> bool:
        events = self.read_events_from_file()
        check = [e for e in events if e["id"] == id]
        if check == []:
            return False
        filtered = [e for e in events if e["id"] != id]
        with open(self.json_file_path, "w") as file:
            json.dump(filtered, file, indent=4)
        return True

    def update_by_id(self, id: int, event: Event) -> bool:
        events = self.read_events_from_file()
        check = [e for e in events if e["id"] == id]
        if check == []:
            return False
        filtered = [e for e in events if e["id"] != id]
        filtered.append(event.model_dump())
        with open(self.json_file_path, "w") as file:
            json.dump(filtered, file, indent=4)
        return True
