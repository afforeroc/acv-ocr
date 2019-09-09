# Libraries getting the value of the environment variables
from dotenv import load_dotenv
from os import getenv, path

# Libraries for post requesting and json manipulating 
import requests
import json

# Libraries for data visualization
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

# Loading values of env file
dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
base_endpoint = getenv('base_endpoint')
subscription_key = getenv('subscription_key')

# Loading image to analyze
image_path = "atoms.png"
image_data = open(image_path, "rb").read()

# Constructing post request format
ocr_endpoint = base_endpoint + "ocr"
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
params = {'language': 'es', 'detectOrientation': 'true'}
response = requests.post(ocr_endpoint, headers=headers, params=params, data=image_data)
analysis = response.json()

# Printing response on JSON format
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

# Writting output text
filename = path.splitext(image_path)[0]
output_text = "output/" + filename + ".txt"
extracted = open(output_text,"w") 
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