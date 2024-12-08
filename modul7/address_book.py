
from datetime import datetime, timedelta

class AddressBook:
    def __init__(self):
        self.records = {}

    def add_record(self, record):
        self.records[record.name.value] = record

    def find(self, name: str):
        return self.records.get(name, None)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        result = []
        for record in self.records.values():
            if record.birthday:
                days_left = record.days_to_birthday()
                if days_left is not None and days_left <= 7:
                    result.append({
                        "name": record.name.value,
                        "birthday": record.birthday.value.strftime("%d.%m.%Y")
                    })
        return result
