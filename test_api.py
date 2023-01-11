# %%
import io
import json
from pprint import pprint

import requests
from PIL import Image

# %%
response = requests.post("http://127.0.0.1:8000")
response.raise_for_status
# %%
pprint(json.loads(response.content.decode("utf8")))
# %%
file = {"img": open("sample.jpg", "rb")}
headers = {"type": "multipart/form-data"}
URL = "http://127.0.0.1:8000"
filter = "blur"

response = requests.post(f"{URL}/{filter}", headers=headers, files=file)
response.raise_for_status
# %%
image = Image.open(io.BytesIO(response.content))
image.save("response.jpg", "JPEG")
image
# %%
