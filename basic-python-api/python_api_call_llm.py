import requests
import json

#Populating the api url end point
url = "http://localhost:11434/api/generate"

# Popluating the API call data
data = {
    "model": "deepseek-r1:7b",
    "prompt": "Tell me a funny story"
}

# Storing the respose to the API call
response = requests.post(url, json=data, stream=True)

# Check for the response status
if(response.status_code == 200):
    # Iterate over the streaming response
    print("Generated Text:", end=" ", flush=True)
    for line in response.iter_lines():
        if line:
            #Decode the line and parse the JSON
            decoded_line = line.decode("utf-8")
            result = json.loads(decoded_line)

            #Get the text form the response
            generated_text = result.get("response", "")
            print(generated_text, end="", flush=True)

else:
    print("Error:". response.status_code, response.text)

