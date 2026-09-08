import json
import requests

while True:
	food = input("enter food name : ")
	url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query={food}"
	r = requests.get(url)
	data = r.json()
	#nutrient_data = data["foods"][0]["foodNutrients"]
	
	if "foods" in data and len(data["foods"]) > 0:
		print("Food found")
		print("-----------Per 100 Gram --------------")
		nutrient_data = data["foods"][0]["foodNutrients"]
		for i in nutrient_data:
			name = i.get('nutrientName')
			value = i.get('value')
			unit = i.get('unitName')
			
			print(f"{name} -> {value}{unit}")
	else:
		print("food did not found")
