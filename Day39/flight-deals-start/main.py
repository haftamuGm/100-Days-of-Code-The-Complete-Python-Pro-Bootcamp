import datetime
ORIGIN="LON"
from data_manager import Datamanager
data_manager = Datamanager()
sheet_data = data_manager.get_destination_data()
from flight_search import Flight_search
from flight_data import find_cheapest_flight
from notification_manager import Notification_managers
notification=Notification_managers()
flight_search=Flight_search()
# for row in sheet_data:
#     if row["iataCode"] == "":
#         row["iataCode"] = flight_search.get_destination(row["city"])
# print(f"sheet_data:\n {sheet_data}\n")
tommorow=datetime.datetime.now()+datetime.timedelta(days=1)
for_sixmonth=datetime.datetime.now()+datetime.timedelta(days=180)
data_manager.destination_data = sheet_data
#data_manager.update_destination()
a=0
the_cheapest_price=0
for destination in sheet_data:
    flight=(flight_search.get_city
            (ORIGIN,destination["iataCode"],
             tommorow,
             for_sixmonth))

    cheap=find_cheapest_flight (flight)
    if not cheap.price=="N/A" and cheap.price<destination["lowestPrice"]:
        message_body = f"Low price alert! Only £{cheap.price} to fly "
        f"from {cheap.origin_airport} to {cheap.destination_airport}, "
        f"on {cheap.out_date} until {cheap.return_date}."
        notification.send_message(message_body)






