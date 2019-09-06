# Libraries for reading environment variables
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Libraries for post requesting and json manipulating 
import requests
import json

# Libraries for data visualization
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

# Using ".env" file to obtain credentials 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables
vision_base_url = os.getenv('vision_base_url')
subscription_key = os.getenv('subscription_key')
assert subscription_key

# Using OCR service
ocr_url = vision_base_url + "ocr"

# Set image_path that you want to analyze
image_path = "atoms.png"

# Read the image into a byte array
image_data = open(image_path, "rb").read()

# Set Content-Type to octet-stream
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
params = {'language': 'es', 'detectOrientation': 'true'}

# Put the byte array into your post request
response = requests.post(ocr_url, headers=headers, params=params, data=image_data)
response.raise_for_status()
analysis = response.json()
#print(json.dumps(analysis, indent=4, sort_keys=True))
    
# Extract the word bounding boxes and text
text = ''
line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        line_text = ''
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
            line_text += word_info['text'] + ' '
        text += line_text.rstrip() + '\n'
text = text[0:len(text)-1]
print(text)

# Write data in a file 
extracted = open("text-from-local.txt","w") 
extracted.write(text) 
extracted.close()

# Display the image and overlay it with the extracted text
plt.figure(figsize=(5, 5))
image = Image.open(image_path)
ax = plt.imshow(image, alpha=0.5)
for word in word_infos:
    bbox = [int(num) for num in word["boundingBox"].split(",")]
    text = word["text"]
    origin = (bbox[0], bbox[1])
    patch = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='y')
    ax.axes.add_patch(patch)
    plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
plt.show()