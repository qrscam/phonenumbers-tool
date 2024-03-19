import phonenumbers, os, time
from phonenumbers import carrier, geocoder, timezone

class Numbers:
  def __init__(self):
    super().__init__()

  def carrier(self, number: str):
    clixy = phonenumbers.parse(number)
    result = carrier.name_for_number(clixy, "en")
    try:
      print(result)
    except phonenumbers.is_valid_number:
      print("Invalid number")

  def geocoder(self, number: str):
    idk = phonenumbers.parse(number)
    result = geocoder.description_for_number(idk, "en")
    try:
      print(result)
    except phonenumbers.is_valid_number:
      print("Invalid number")

  def timezone(self, number: str):
    idk = phonenumbers.parse(number)
    result = timezone.time_zones_for_number(idk)
    try:
      print(result)
    except phonenumbers.is_valid_number:
      print("Invalid number")

  def start(self):
    os.system("cls")
    choice = input("1) Carrier\n2) Location\n3) Timezone\n")

    match choice:
      
      case "1":
        number = input("Phone number: ")
        self.carrier(number)
        time.sleep(3)
        return self.start()
      
      case "2":
        number = input("Phone number: ")
        self.geocoder(number)
        time.sleep(3)
        return self.start()
      
      case "3":
        number = input("Phone number: ")
        self.timezone(number)
        time.sleep(3)
        return self.start()
      
      case _:
        return self.start()
      
t = Numbers()
t.start()