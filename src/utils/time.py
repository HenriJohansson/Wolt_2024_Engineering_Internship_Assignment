from datetime import datetime

# "2024-01-16T14:00:00Z"
class Time:
    _def_time: str = "1900-01-01T00:00:00Z"
    def __init__(self, time: str = _def_time):
        if time[-1] is 'Z':
            time = time[:-1]
        self._time: datetime = datetime.fromisoformat(time)

    def get_default_time(self) -> str:
        return self._def_time

    @property
    def time(self) -> datetime:
        return self._time

    def __str__(self) -> str:
        return self._time.isoformat()
    
    def __repr__(self) -> str:
        return repr(self._time.isoformat())
    
    def __eq__(self, other): 
        if not isinstance(other, Time):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return str(self._time) == str(other._time)