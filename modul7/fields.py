from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must be a 10-digit number.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        self.value = self._validate_birthday(value)
        
    def _validate_birthday(self, value):
        try:
            # Перевіряємо формат
            day, month, year = map(int, value.split("."))
            datetime(year=year, month=month, day=day)  # Перевірка валідності
            return value  # Повертаємо рядок у форматі DD.MM.YYYY
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY.")