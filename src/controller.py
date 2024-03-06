from src.cart import Cart
from src.chargers import ValueCharger, ItemCharger, DistanceCharger, TimeCharger
def get_delivery_fee(data) -> int:
    request_data: dict = data
    cart = Cart()
    cart.attach(ValueCharger())
    cart.attach(ItemCharger())
    cart.attach(DistanceCharger())
    cart.attach(TimeCharger())
    cart.setCart(request_data["cart_value"], 
                 request_data["delivery_distance"], 
                 request_data["number_of_items"],
                 request_data["time"])
    return cart.fee.fee

