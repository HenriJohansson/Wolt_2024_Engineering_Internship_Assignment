from src.request import RequestVerification

class TestRequests:
    correct_form = {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
    missing_key = {"cart_value": 790, "delivery_distance": 2235, "time": "2024-01-15T13:00:00Z"}

    def test_is_acceptable_fee(self):
        verifier = RequestVerification(self.correct_form)
        assert verifier.isAcceptableFee() is True
    def test_missing_key(self):
        verifier = RequestVerification(self.missing_key)
        assert verifier.isAcceptableFee() is False