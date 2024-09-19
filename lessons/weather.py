def get_weather_report() -> str:
    """Display instructions"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket")
    elif weather == "hot":
        print("Keep cool out there")
    else:
        print("I dont recognize this weather")
    return weather


get_weather_report()
