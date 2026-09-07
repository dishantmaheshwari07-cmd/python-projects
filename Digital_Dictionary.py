import requests
from spellchecker import SpellChecker

while True:
	word = input("Enter word: ").strip().lower()
	spell = SpellChecker()
	misspelled = spell.unknown(word)
	word = spell.correction(word)
	print(word)
		
		# Edge Case 0: Empty input
	if not word:
		print("Please enter a valid word.")
		exit()
		
	url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
		
	try:
		    # Set a timeout so the script doesn't hang forever if the API is down
		r = requests.get(url, timeout = 15)
		    
		if r.status_code == 200:
			data = r.json()
		        
		        # Safely drill down into the JSON structure
			if data and isinstance(data, list):
				meanings = data[0].get('meanings', [])
				if meanings:
					definitions = meanings[0].get('definitions', [])
					if definitions:
						print(f"\nDefinition: {definitions[0].get('definition')}")
					else:
						print("No definitions found for this part of speech.")
				else:
					print("No meanings found for this word.")
			else:
				print("Received unexpected data format from the server.")
		            
		elif r.status_code == 404:
			print(f"Error: The word '{word}' was not found in the dictionary.")
		else:
			print(f"Server error: Received status code {r.status_code}.")
		
		# Handle specific network/request exceptions
	except requests.exceptions.ConnectionError:
		print("Network Error: Please check your internet connection.")
	except requests.exceptions.Timeout:
		print("Timeout Error: The server took too long to respond. Try again later.")
	except requests.exceptions.RequestException as e:
		print(f"An unexpected network error occurred: {e}")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")
	
