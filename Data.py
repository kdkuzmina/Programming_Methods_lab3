import datetime
class Data:
    def __init__(self, Date: datetime.datetime, Flight: int, FullName: str, Place: int):
        self.FullName = FullName
        self.Flight = Flight
        self.Date = Date
        self.Place = Place
        self.SimpleHash = None
        self.ComplexHash = None

    def set_simple_hash(self, value):
        self.SimpleHash = value

    def get_simple_hash(self):
        return self.SimpleHash

    def set_complex_hash(self, value):
        self.ComplexHash = value

    def get_complex_hash(self):
        return self.ComplexHash

    def __eq__(self, other):
        return self.FullName == other.FullName and self.Flight == other.Flight and \
               self.Date == other.Date and self.Place == other.Place

    def __gt__(self, other):  # >
        if self == other:
            return True
        if self.FullName == other.FullName:
            if self.Flight == other.Flight:
                if self.Date == other.Date:
                    return self.Place > other.Place
                else:
                    return self.Date < other.Date
            else:
                return self.Flight > other.Flight
        else:
            return self.FullName > other.FullName

    def __lt__(self, other):
        return not self > other

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return other > self or self == other

    def __repr__(self):
        string = str(self.Flight) + " " + str(self.Date) + " " + self.FullName + " " + str(self.Place)
        return string

    def __str__(self):
        string = str(self.Flight) + " " + str(self.Date) + " " + self.FullName + " " + str(self.Place)
        return string
    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return other > self or self == other

    def __repr__(self):
        string = str(self.Flight) + " " + str(self.Date) + " " + self.FullName + " " + str(self.Place)
        return string

    def __str__(self):
        string = str(self.Flight) + " " + str(self.Date) + " " + self.FullName + " " + str(self.Place)
        return string
