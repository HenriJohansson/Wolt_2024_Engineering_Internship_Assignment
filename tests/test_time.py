from src.utils import Time
import pytest

@pytest.fixture
def example_times():
    return {"monday": Time("2024-01-15T13:00:00Z").time,
            "thuesday": Time("2024-01-16T14:00:00Z").time, 
            "wednesday": Time("2023-12-06T19:00:00Z").time, 
            "thursday": Time("2024-01-18T13:00:00Z").time, 
            "friday": Time("2024-01-19T13:00:00Z").time, 
            "saturday": Time("2024-01-20T13:00:00Z").time, 
            "sunday": Time("2024-01-14T10:20:00Z").time}

class TestTime:

    def test_years(self, example_times: dict):
        assert example_times["monday"].year == 2024

    def test_months(self, example_times):
        assert example_times["wednesday"].month == 12
    
    def test_days(self, example_times):
        assert example_times["saturday"].day == 20
    
    def test_hours(self, example_times):
        assert example_times["sunday"].hour == 10
    
    def test_minutes(self, example_times):
        assert example_times["sunday"].minute == 20
    
    def test_weekdays(self, example_times):
        assert example_times["wednesday"].weekday() == 2