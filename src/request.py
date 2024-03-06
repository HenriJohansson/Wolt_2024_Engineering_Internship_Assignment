from src.utils.time import Time

class RequestVerification:
    request: dict
    def __init__(self, request):
        self.request = request
    
    required_keys = ["cart_value", "delivery_distance", "number_of_items", "time"]
    def isAcceptableFee(self):
        if not isinstance(self.request, dict):
            return False
        
        for key in self.required_keys:
            if key in self.request:
                self._key_is_time(key,self.request[key])
            else:
                return False
        return True
    
    def _key_is_time(self,key, value):
        if key is self.required_keys[-1]:
            try:
                Time(value)
            except: raise
        else:
            pass