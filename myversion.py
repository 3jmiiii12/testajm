import requests

def run_code_from_pastebin(url):
    response = requests.get(url)
    if response.status_code == 200:
        code = response.text
        try:
            exec(code, globals())
        except Exception as e:
            print(f"An error occurred while running the code:\n{e}")
    else:
        print(f"Failed to fetch code from {url}. Status code: {response.status_code}")

# Replace this with the actual Pastebin URL
pastebin_url = "https://pastebin.com/raw/n1LUz905"

run_code_from_pastebin(pastebin_url)
