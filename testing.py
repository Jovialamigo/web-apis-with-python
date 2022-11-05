# %%
import requests
import json

# %%
URL = "http://127.0.0.1:5000/"
word = "data"


response = requests.get(URL)
data = response.content.decode("utf-8")
data = json.loads(data)
data["usage"]
# %%
response = requests.get(f"{URL}dict?word={word}")
data = json.loads(response.content.decode("utf-8"))
data
# %%
