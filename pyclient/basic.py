import requests 


endpoint = 'http://127.0.0.1:8000/'
get_responses = requests.get(endpoint, json={'abc': 123} )
print(get_responses.text)