import requests
import json

def fetch_and_save_data(url, output_file, timeout=5):
    try:
        response = requests.get(url,timeout=timeout)
        
        if not response.ok:
            print(f"Request failed with erorr ${response.status_code}")
            return
        try:
            data = response.json()
        except json.JSONDecodeError:
            print("Failed to decode JSON")
            return
    
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {output_file}")

    except:
        print("Not valid url")



api_url = "https://api.github.com/users/swati9828"
output_path = "posts.json"

fetch_and_save_data(api_url, output_path)
