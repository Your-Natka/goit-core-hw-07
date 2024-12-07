from .record import Record
from datetime import datetime, timedelta

class AddressBook:
    def __init__(self):
        self.records = {}

    def add_record(self, record: Record):
        self.records[record.name.value] = record

    def find(self, name: str):
        return self.records.get(name)

    def get_upcoming_birthdays(self):
        today = datetime.now().date()
        week_later = today + timedelta(days=7)
        upcoming = []

        for record in self.records.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year <= week_later:
                    upcoming.append({
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime("%d.%m.%Y")
                    })
        return upcoming
