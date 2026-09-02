import requests
import sys

while True:
	if len(sys.argv) > 1:
		city = sys.argv[1]
	else :
		city = input("enter city name :")
		
	city_detail_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
	
	request1 = requests.get(city_detail_url)
	data1 = request1.json()
	try:
		if data1["results"][0]["feature_code"].startswith("P"):
			latitude = data1["results"][0]["latitude"]
			longitude = data1["results"][0]["longitude"]
			temp_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&timezone=auto"
			request2 = requests.get(temp_url)
			data2 = request2.json()
			current_info = data2["current"]
			units = data2["current_units"]
			
			weather_list = ["temperature_2m" , "relative_humidity_2m", "wind_speed_10m"]
			
			temprature = str(current_info[weather_list[0]])+ units[weather_list[0]]
			
			humidity= str(current_info[weather_list[1]])+ units[weather_list[1]]
			
			wind_speed = str(current_info[weather_list[2]]) + units[weather_list[2]]
			weather = {
			0: "Clear sky",
			1: "Mainly clear",
			2: "Partly cloudy",
			3: "Overcast",
			45: "Fog",
			51: "Drizzle",
			61: "Rain",
			71: "Snow",
			80: "Rain showers",
			95: "Thunderstorm"
			}
			
			for key , value in weather.items() :
				if key == current_info['weather_code']:
					weather_of_city = value
			   	
			country = data1["results"][0]["country"] 
			print(f"\n City -> {city}\n country -> {country}\n Temperature -> {temprature}\n humidity -> {humidity}\n Wind Speed -> {wind_speed} \n Weather -> {weather_of_city}\n ")
			
		else:
			print("City did not found")
		
	except KeyError:
		print("City did not found")
	except IndexError:
		print("city did not found")
	
	if len(sys.argv) > 1:
		sys.exit()
