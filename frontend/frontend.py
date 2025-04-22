import requests

backend_url = "http://backend-container:5000"

response = requests.get(backend_url)

while response.status_code == 200:
    print("Frontend received the following response from the backend:")
    print(response.text)
else:
    print("Failed to communicate with the backend.")
