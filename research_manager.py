import json
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import quote
import sys
import os 
import requests

json_folder = "/storage/emulated/0/30 days of practice/json_folder"			

backup_folder = "/storage/emulated/0/30 days of practice/Backup_folder"

txt_folder = "/storage/emulated/0/30 days of practice/txt_folder"

accounts_file = "/storage/emulated/0/30 days of practice/accounts_json"

def int_input(message):
	while True:
		try:
			return int(input(message))
		except ValueError:
			print("Invalid Number")
	
async def web_data(topic):
	try:
		url1 = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
		
		headers1 = {
			"User-Agent": "SmartResearchManager/1.0"
		}
		r1 = requests.get(url1,  headers=headers1)
		data1 = r1.json()
		title = data1["title"] #= title cricket
		small_url = data1["content_urls"]["desktop"]["page"] #small url source
		description = data1["extract"] #-> description
		
		data = {"TITLE " : title , "URL" : small_url , "Extract" : description}
		
		#data_list[0] = data
		return data
	
	except Exception as e:
		return(f"Title : Error \n  Url : N/A \n Extract : Network Issue : {str(e)}")

async def duck(topic):
	try:
		sub_data_list =[]
		url = f"https://html.duckduckgo.com/html/?q={quote(topic)}"
		r = requests.get(
		url,
			headers={"User-Agent": "Mozilla/5.0"}
		)
		
		soup = BeautifulSoup(r.text, "html.parser")
		
		for result in soup.select(".result"):
		    title = result.select_one(".result__title")
		    link = result.select_one(".result__url")
		    snippet = result.select_one(".result__snippet")
		    data ={"TITLE" : title.get_text(" ", strip=True) if title else "N/A" , "URL" : link.get_text(" ", strip=True) if link else "N/A" , "SNIPPET": snippet.get_text(" ", strip=True) if snippet else "N/A"}
		    sub_data_list.append(data)
		    
		    if len(sub_data_list) == 3:
		    	break
		
		return sub_data_list
	
	except Exception as e:
		return(f"Title : Error \n  Url : N/A \n Extract : Network Issue : {str(e)}")

  	
async def main(topic):
	tasks = []
	tasks.append(web_data(topic))
	tasks.append(duck(topic))
	data = asyncio.gather(*tasks)
	return await data
	

def update_json_file(name , data):
	name = name.capitalize()
	if os.path.exists(f"{json_folder}/{name}.json"):
		with open(f"{json_folder}/{name}.json", "r") as file:
			existing_data= json.load(file)
		with open(f"{json_folder}/{name}.json", "w") as f:
			json.dump(existing_data + data , f , indent = 4)
		
	else:
		with open(f"{json_folder}/{name}.json", "w") as f:
			json.dump(data , f , indent = 4)
		
		
def load_data(name):
	try:
		name = name.capitalize()
		with open(f"{json_folder}/{name}.json", "r") as f:
			data = json.load(f)
			return data
			
	except FileNotFoundError:
		return None

def print_data(data , results =None):
    if results is None:
    	results = []
    	
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                results.append(key)
                print_data(value , results)
            else:
                results.append([key , value])

    elif isinstance(data, list):
        for i in data:
            print_data(i ,results)

    else:
    	results.append(data)
    return results
    
def simple_form(readable_data):
	for i  in readable_data:
		if isinstance(i,list):
			print(f"{i[0]} -> {i[1]}")
		else:
			print(i)
		
def save_pin(name , password):
	name_pin = {name.capitalize() : password}
	
	if os.path.exists(accounts_file):
		with open(f"{accounts_file}" , "r") as f:
			exists_data = json.load(f)
		with open (f"{accounts_file}" , "w")  as f:
			json.dump(exists_data|name_pin , f)
	else:
		with open (f"{accounts_file}" , "w")  as f:
			json.dump(name_pin , f)

def verify_pin(name , pin):
	with open (accounts_file , "r") as f:
		data = json.load(f)
	try:
		if data[name.capitalize()] == pin:
			return data
		return None
	except KeyError:
		return None
	
																	
class ResearchManager:
	def __init__(self , user_name):
		self.name = user_name
		
	def research(self , topic_name):
		final_data =[]
		return_data = asyncio.run(main(topic_name))
		
		for i in return_data:
			if isinstance(i , dict) and i:
				final_data.append(i)
				print(f"\n{'-' *15}Wikipedia{'-' *15}\n")
				for key , value in i.items():
					print(f"{key} -> {value}\n")
				
					
			elif isinstance(i , list) and i:
				final_data.append(i)
				print(f"\n{'-' *20}Duck{'-' *20}\n ")
				for elment in i:
					for key ,value in elment.items():
						print(f"{key} -> {value}\n")
			else:
				print(i)
		
		update_json_file(self.name , [{topic_name.capitalize() : final_data}])
		
	def search_keyword(self , num):
		data = load_data(self.name)
		
		if data:
			found = False
			for length , i in enumerate(data , start =1):
				for key , value in i.items():
					if num == 1:
						print(f"{length}. {key}")
						
			if num == 1:
				choose = int_input("Enter no. which data do u want : ")
				if 1 <= choose  <= len(data):
					data_to_print = print_data(data[choose-1])
					for i  in data_to_print:
						if isinstance(i,list):
							print(f"{i[0]} -> {i[1]}\n")
						else:
							print(i)
				else:
					print("No number found")
							
			else:
				choose = input("Enter keyword : ")
				
				
				for i in data:
					readable_data = print_data(i)
					for  single_data in readable_data:
						if isinstance(single_data,list):
							for word in single_data :
								if choose.lower() in word.lower():
									simple_form (readable_data)
									return True										
						else:		
							if single_data.lower() == choose.lower():
									simple_form(readable_data)
									return True
					
				print("No keyword found")
				
		else:
			print("No file found")		
			
	def statics(self):
		data = load_data(self.name)
		if data:
			total_researches = len(data)
			
			wiki = 0
			duck = 0
			
			for i in data:
				for key , value in i.items():
					for elements in value:
						if isinstance(elements , dict) and elements:
							wiki+=1
						if isinstance (elements, list) and elements:
							duck+=1
							
			succesful = wiki + duck
			failed = (len(data)*2) - succesful
			
			print(f"Total Reserches : {total_researches}\n Wikipedia Succesful : {wiki}\n DuckDuckGo Succesful -> {duck}\n Total succesful Research -> {succesful}\n Failed research -> {failed}\n")
			
			for i in data:
				wiki_data = {}
				duck_data = {}
				
				for key , value in i.items():
					for elements in value:
						if isinstance(elements , dict):
							wiki_data = {"Wikepidiea" : 1}
						elif isinstance (elements , list):
							duck_data = {"DuckDuckGo" : len(elements)}
					data_dict = {key : wiki_data| duck_data}
					for key , value in data_dict.items():
						print(key)
						for sub_key , sub_value in value.items():
							print(f"{sub_key} -> {sub_value}")
		
		else:
			print("No account found")		
				
	def export_research(self):
		data = load_data(self.name)
		
		if data:
			for index , i in enumerate(data , start =1):
				for keys, values in i.items():
					print(f"{index}.  {keys}")
					
			index_list =[]		
			while True:
				choose = int_input("enter number whose data to export in .txt file and 0 to break :")	
				found = False
				if choose == 0:
					break
				else:
					if 1<= choose <= len(data):
						for i in index_list:
							if i == choose-1:
								print(f"{choose} no data already in export search ")
								found = True
						if not found:
							index_list.append(choose -1)
					else:
						print(f"Enter Number btw 1 to {len(data)}")
			
			for num in index_list:
				user_data = data[num]
				return_data = print_data(user_data)
				
				simple_data = f"\n{'-'*30}  {return_data[0]} {'-'*30}\n"
				del return_data[0]
				
				for i in return_data:
					if isinstance(i,list):
						simple_data+= f"{i[0]} -> {i[1]}\n"
					else:
						simple_data+=f"{i}\n"
						
				if os.path.exists(f"{txt_folder}/{self.name}.txt"):
					with open(f"{txt_folder}/{self.name}.txt", "r") as file:
						existing_data= file.read()
					with open(f"{txt_folder}/{self.name}.txt", "w") as f:
						f.write(existing_data +simple_data)				
				
				else:
					with open(f"{txt_folder}/{self.name}.txt", "w") as f:
						f.write(simple_data)		
				print("Data saved succesfully in txt file")		
		else:
			print("No account found")		
			
	def delete_research(self):
		data = load_data(self.name)
		if data:
			for index, i in enumerate(data , start =1):
				for keys , value in i.items():
					print(f"{index}. {keys}")
			
			choose = int_input("Enter which number wants to delete : ")
			
			if 1<= choose <= len(data):
				simple_form(print_data(data[choose-1]))
				conformation = input("Y/N :")
					
				if conformation.lower() == "y":
	
					del data[choose-1]
						
					with open(f"{json_folder}/{self.name}.json", "w") as f:
						json.dump(data,f)
						
						print("data deleted succesfully")
				else:
					print("Data did not deleted")
					
			else:
				print(f"Enter no. btw 1 to {len(data)}")
				
		else:
			print("No account found")
	
	def backup(self):
		data = load_data(self.name)
		
		if data:
			with open (f"{backup_folder}/{self.name}_backup_file.json" , "w") as f:
				json.dump(data, f)
			print("Data backuped succesfully")
			
		else:
			print("No account found to backup")
			
	def restore(self):
		json_file = f"{json_folder}/{self.name}.json"
		backup_file = f"{backup_folder}/{self.name}_backup_file.json"
		
		if os.path.exists(backup_file):
			
			with open(backup_file, "r") as f:
				transfer_data = json.load(f)
				
			with open(json_file , "w") as f:
				json.dump(transfer_data , f)
			print("Data restored succesfully")
			
		else:
			print("No backup file found")
current_acc = None		

menu = "\nEnter:\n1 for seeing menu\n2 for Create Account\n3 for Change/login Account\n4 for Delete Account\n5 for Research Topic\n6 for Saved Research\n7 for Search Saved Data\n8 for Delete Research\n9 for see Statistics\n10 for Export Research\n11 for Backup & Restore\n12 for exit\n"
print(menu)

while True:
	if len(sys.argv) > 1:
		try:
			user = int(sys.argv[1])
		except ValueError:
			print("Enter a no at last")
	else:
		user = int_input("Enter no. according to menu :")
	
	if 0 < user < 13:
		if user == 1:
			print(menu)
			
		elif user == 2:	
			name = input("Enter your name:")
			found = False
			for i in os.listdir(json_folder):
				if i == f"{name.capitalize()}.json":
					found = True
					print(f"Account of name {name} already exists")
			if not found:
				pin = input("Create account password :")
				current_acc = ResearchManager(name.capitalize())
				save_pin(name , pin)
				
		elif user == 3:
			change_name = input("Enter name of existing account :")
			found = False
			for i in os.listdir(json_folder):
				if i == f"{change_name.capitalize()}.json":
					pin = input("Enter account pin:")
					check = verify_pin(change_name.capitalize() , pin)
					if check:
						current_acc = ResearchManager (change_name.capitalize())
						found = True
					else:
						print("Pin is wrong")
					
			if not found:
				print("No account found")
		
		elif user == 4:
			if current_acc :
				del_acc = input("Enter account name to delete :")
				found = False
				for i in os.listdir(json_folder):
					if i == f"{del_acc.capitalize()}.json":
						pin = input("enter account pin :")
						check = verify_pin(del_acc , pin)
						
						if check:
							found = True
							conform = input("Y/N")
							if conform.lower() == "y":
								os.remove(f"{json_folder}/{del_acc.capitalize()}.json")
								del check[del_acc.capitalize()]
								with open (f"{accounts_file}" , "w")  as f:
									json.dump(check , f)
								print("Account Deleted Succesfully")
								if current_acc.name.capitalize() == del_acc.capitalize():
									current_acc = None
									break
							else:
								print("Account Did not Deleted")
								break
				if not found:
					print("No account found")
			else:
				print("No account is currently logged in.")
		
		elif user == 5:
			if current_acc:
				topic = input("Enter topic to search about : ")
				current_acc.research(topic)
			else:
				print("No account is currently logged in.")
		elif user == 6:
			if current_acc:
				current_acc.search_keyword(1)
			else:
				print("No account is currently logged in.")
		elif user == 7:
			if current_acc:
				current_acc.search_keyword(0)
			else:
				print("No account is currently logged in.")
		elif user == 8:
			if current_acc:
				current_acc.delete_research()
			else:
				print("No account is currently logged in.")
				
		elif user == 9:
			if current_acc:
				current_acc.statics()
			else:
				print("No account is currently logged in.")
				
		elif user == 10:
			if current_acc:
				current_acc.export_research()
			else:
				print("No account is currently logged in.")
		
		elif user == 11:
			if current_acc:
				sub_choice = int_input("Enter \n 1 for backup data \n 2  for restoring data")
				if sub_choice in (1,2):
					if sub_choice == 1:
						current_acc.backup()
					else:
						current_acc.restore()
				else:
					print("Enter 1 or 2")
			else:
				print("No account is currently logged in.")
					
		else:
			current_acc = None
			sys.exit()
	else:
		print("Enter no. btw 1 to 12 as shown in Menu")
