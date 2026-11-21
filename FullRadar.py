import requests
import json



def saveuserlanguage(language_choice):
          with(open("FullRadarSettings.json", "w", encoding="utf-8")) as f:
               data = {"language": language_choice}
               json.dump(data, f)

def loaduserlanguage():
     try:
          with(open("FullRadarSettings.json", "r", encoding="utf-8")) as f:
               return json.load(f).get("language", "en")
     except FileNotFoundError:
          return "en"
     except json.JSONDecodeError:
          return "en"
     
def load_favorites():
       try:
             with (open("FullRadar.json", "r", encoding ="utf-8")) as file:
                   return json.load(file)
       except FileNotFoundError:
             return []

def save_data(favoritescities):
    with (open("FullRadar.json", "w", encoding="utf-8")) as file:
                json.dump(favoritescities,file, indent=4, ensure_ascii= False)


def nextdays(weatherdata, temp_symbol):
     print("-----Forecast of the Weather to the next 7 Days-----")
     max_temp = weatherdata["daily"]["temperature_2m_max"]
     min_temp = weatherdata["daily"]["temperature_2m_min"]
     datatime = weatherdata["daily"]["time"]
     rain = weatherdata["daily"]["precipitation_probability_max"]
     
     
     for i in range(7):
          MaxTemp = max_temp[i]
          MinTemp = min_temp[i]
          Data = datatime[i]
          Rain = rain[i]
          print(f"Next 7 days: Day : {Data} | Max Temp: {MaxTemp} {temp_symbol} | Min Temp : {MinTemp} {temp_symbol} | Rain: {Rain}%")

                         

def recommendedactivity(weatherdata, temp_unit):
     currenttemperature = weatherdata["current"]["temperature_2m"]
     currenthumidity = weatherdata["current"]["relative_humidity_2m"]
     currentwindspeed = weatherdata["current"]["wind_speed_10m"]
     currentprecipitation = weatherdata["current"]["precipitation"]

     if temp_unit == "fahrenheit":
        temp_c = (currenttemperature - 32 ) * 5 / 9
     else:
        temp_c = currenttemperature
        


     print("=====Recommended Activity=====")

     if temp_c > 30:
          print("🌤️ Running right now isn´t a good choice to your health! Please reconsider the chance to go outside.")
     elif currenthumidity <= 30:
          print("🔅 The humidity is too low. Please reconsider the chance to go outside!")
     elif temp_c <= 10:
          print("❄️ It seems that it is too cold outside")
     elif currentwindspeed >= 10:
          print("🍃 The wind speed is too high. Please reconsider the chance to start running outside!")
     elif currentprecipitation > 0:
          print("🌧️ It seems that can start raining in your local! Please take care of yourself!")
     else:
          print("🏃 All fine to go!")

     if temp_c > 30:
          print("🏋️Go to the gym right now isn´t a good choice, but if you go, take care of you and drink plenty of water!")
     elif currenthumidity <= 30:
          print("🏋️ Going to the gym it can be a little bit more hard because of the currently humidity, but if you want to go there, take care of your health!")
     elif currentprecipitation > 0:
          print(" 🏋️  It may can rain, so it´s better to get ready for that!")
     else:
          print(" 🏋️ All good to go, let´s head for it!")
    


def favoritecity(city, temp_unit, temp_symbol):
    geo = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    answer = requests.get(geo)
    data = answer.json()

    if "results" in data and len(data["results"]) > 0:
          latitude = data["results"][0]["latitude"]
          longitude = data["results"][0]["longitude"]
          
          base_url = "https://api.open-meteo.com/v1/forecast"
          weatherapi = f"{base_url}?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_probability_max&temperature_unit={temp_unit}"
          weather2 = requests.get(weatherapi)
          weatherdata = weather2.json()
          
        
          currenttemperature = weatherdata["current"]["temperature_2m"]
          currenthumidity = weatherdata["current"]["relative_humidity_2m"]
          currentwindspeed = weatherdata["current"]["wind_speed_10m"]
          currentmaxtemperature = weatherdata["daily"]["temperature_2m_max"][0]
          currentmintemperature = weatherdata["daily"]["temperature_2m_min"][0]
          daysunrise = weatherdata["daily"]["sunrise"][0]
          currentprecipitation = weatherdata["current"]["precipitation"]
          apparenttemperature = weatherdata["current"]["apparent_temperature"]
          daysunset = weatherdata["daily"]["sunset"][0]
          maximumpossibleprecipitation = weatherdata["daily"]["precipitation_probability_max"][0]


          if temp_unit == "fahrenheit":
                temp_c = (currenttemperature - 32) * 5 / 9
                app_c = (apparenttemperature - 32) * 5 / 9
          else:
               temp_c = currenttemperature
               app_c = apparenttemperature
          
          print("-----Smart Warnings-----")
          if currentprecipitation > 0:
                print("High chances of rain, please take precautions.")
          else:
                print("No signal of rain right now, no need to worry")

          if currentwindspeed > 20:
                print("Warning: High wind speed detected (Above 20km/h), Please take care and avoid flat surface activities.")
          else:
                print("The wind speed is calm right now, no need to worry!")
                
          temperaturedifference = app_c - temp_c

          if temperaturedifference >= 2:
                print("HEAT STRESS WARNING: It seems that the apparent temperature is a little bit higher than the current temperature, please stay hydrated and avoid direct exposure to the sun.")

          if temp_c < 15:
                print("It seems the temperature is quite low, please make sure to wear jackets and coats to avoid it getting too cold.")

          if currenthumidity < 30:
                print("Oh, it seems the humidity is quite low, please make sure stay hydrated and avoid physical exercises for now!")
        

          print(f"Current Temperature: {currenttemperature} {temp_symbol}")
          print(f"Current Humidity: {currenthumidity}%")
          print(f"Current Wind Speed: {currentwindspeed}Km/h")
          print(f"Current Maximum Temperature: {currentmaxtemperature} {temp_symbol}")
          print(f"Current Minimum Temperature: {currentmintemperature} {temp_symbol}")
          print(f"Day Sunrise: {daysunrise}")
          print(f"Day Sunset: {daysunset}")
          print(f"Maximum Possible Precipitation: {maximumpossibleprecipitation}%")

          recommendedactivity(weatherdata, temp_unit)
          nextdays(weatherdata, temp_symbol)

    else:
        print("Oh, it seems that the city wasn´t found!")
       
                                

favoritiescities = load_favorites()
defaultlanguage = loaduserlanguage()


if __name__ == "__main__":
    while True:
        print("=====Welcome to FullRadar=====")
        print("=====This program will help you to know the exactly forecast of the weather to your city!")
        print("==========MENU==========")
        
        menuchoice = input("What you would like to do? \n [1] Forecast of The Weather \n [2] Favorites Cities \n [3] Delete a Favorite City \n [4] Settings \n [5] Exit ").strip()
        
        try:
            if menuchoice == "4":
                 settingschoice = input("Choice the Language that you would like to have: English [en] or Portuguese [pt] ").strip().lower()
                 if settingschoice in ["en", "pt"]:
                      saveuserlanguage(settingschoice)
                      defaultlanguage = loaduserlanguage()
                      print(f"Language changed to: {settingschoice}")
                 else:
                      print("Invalid Choice, please try it again!")
                      continue

            elif menuchoice == "5":
                print("No worries then! Have a nice day!")
                break


            elif menuchoice == "3":
                if not favoritiescities:
                    print("Oh it seems you don´t have any favorite city added yet!")
                else:
                    for index, city in enumerate(favoritiescities, 1):
                        print(f"{index} | {city}")
                    deletecity = int(input("Please type the number of the city that you would like to delete from your favorites list: "))
                    removedcity = favoritiescities.pop(deletecity - 1)
                    save_data(favoritiescities)
                    print(f"The city {removedcity} got deleted from your favorites list!")
                continue

            elif menuchoice == "2":
                print("=====Favorites Cities=====")
                
                if len(favoritiescities) == 0:
                    print("Oh it seems you don´t have any favorite city added yet!")
                else:
                    unit_choice = input("Would you like to see the Forecast in Celsius or Fahrenheit? (C/F) " ).upper().strip()
                                    
                    if unit_choice == "C":
                        temp_unit = "celsius"
                        temp_symbol = "°C"
                    elif unit_choice == "F":
                        temp_unit = "fahrenheit"
                        temp_symbol = "°F"
                    else:
                        print("Ops, it seems you typed something wrong")
                        continue
                    for index, city in enumerate(favoritiescities, 1):
                        print(f"{index}, {city}")
                        favoritecity(city, temp_unit, temp_symbol)
                        
                continue

            elif menuchoice == "1":
                city_name = input("Please type the city´s name that you would like to know the weather forecast: ").strip().capitalize()

                geo = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
                answer = requests.get(geo)
                data = answer.json()

                if "results" in data and len(data["results"]) > 0:
                    
                    if city_name not in favoritiescities:
                        favoritiescities.append(city_name)
                        save_data(favoritiescities)
                    
                    latitude = data["results"][0]["latitude"]
                    longitude = data["results"][0]["longitude"]

                    print(f" {city_name} is located at latitude {latitude} and Longitude {longitude}")

                    userforecastanswer = input("Do you want to know the weather forecast to that local? (Yes/No): ").strip().capitalize()

                    
                    if userforecastanswer == "Yes":

                        unit_choice = input("Would you like to see the Forecast in Celsius or Fahrenheit? (C/F) " ).upper().strip()
                        
                        if unit_choice == "C":
                            temp_unit = "celsius"
                            temp_symbol = "°C"
                        elif unit_choice == "F":
                            temp_unit = "fahrenheit"
                            temp_symbol = "°F"
                        else:
                            print("Ops, it seems you typed something wrong")
                            continue
                            
                        base_url = "https://api.open-meteo.com/v1/forecast"
                        weatherapi = f"{base_url}?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_probability_max&temperature_unit={temp_unit}"
                        weather2 = requests.get(weatherapi)
                        weatherdata = weather2.json()
                        
                        

                        currenttemperature = weatherdata["current"]["temperature_2m"]
                        currenthumidity = weatherdata["current"]["relative_humidity_2m"]
                        currentwindspeed = weatherdata["current"]["wind_speed_10m"]
                        currentmaxtemperature = weatherdata["daily"]["temperature_2m_max"][0]
                        currentmintemperature = weatherdata["daily"]["temperature_2m_min"][0]
                        daysunrise = weatherdata["daily"]["sunrise"][0]
                        currentprecipitation = weatherdata["current"]["precipitation"]
                        apparenttemperature = weatherdata["current"]["apparent_temperature"]
                        daysunset = weatherdata["daily"]["sunset"][0]
                        maximumpossibleprecipitation = weatherdata["daily"]["precipitation_probability_max"][0]
                        
                        if temp_unit == "fahrenheit":
                                        temp_c = (currenttemperature - 32) * 5 / 9
                                        app_c = (apparenttemperature - 32) * 5 / 9
                        else:
                                    temp_c = currenttemperature
                                    app_c = apparenttemperature
                        

                        print("-----Smart Warnings-----")

                        if currentprecipitation > 0:
                            print("High chances of rain, please take precautions.")
                        else:
                            print("No signal of rain right now, no need to worry")

                        if currentwindspeed > 20:
                            print("Warning: High wind speed detected (Above 20km/h), Please take care and avoid flat surface activities.")
                        else:
                            print("The wind speed is calm right now, no need to worry!")

                        
                        temperaturedifference = app_c - temp_c

                        if temperaturedifference >= 2:
                            print("HEAT STRESS WARNING: It seems that the apparent temperature is a little bit higher than the current temperature, please stay hydrated and avoid direct exposure to the sun.")

                        if temp_c < 15:
                            print("It seems the temperature is quite low, please make sure to wear jackets and coats to avoid it getting too cold.")

                        if currenthumidity < 30:
                            print("Oh, it seems the humidity is quite low, please make sure stay hydrated and avoid physical exercises for now!")
                        

                        print(f"Current Temperature: {currenttemperature} {temp_symbol}")
                        print(f"Current Humidity: {currenthumidity}%")
                        print(f"Current Wind Speed: {currentwindspeed}Km/h")
                        print(f"Current Maximum Temperature: {currentmaxtemperature} {temp_symbol}")
                        print(f"Current Minimum Temperature: {currentmintemperature} {temp_symbol}")
                        print(f"Day Sunrise: {daysunrise}")
                        print(f"Day Sunset: {daysunset}")
                        print(f"Maximum Possible Precipitation: {maximumpossibleprecipitation}%")

                        recommendedactivity(weatherdata, temp_unit)
                        nextdays(weatherdata, temp_symbol)

                    elif userforecastanswer == "No":
                        print("Okay, no problem then!")
                        continue
            
                else:
                    print("Invalid answer! Please try it again")
                    continue
            
            else:
                print("Invalid Answer! Please try it again" )
                continue
    
        except Exception as e:
            print("Oh something werid happened! Please wait a little bit and try it again")
            continue
            
            

