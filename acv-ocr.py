from dotenv import load_dotenv              # Load env file
from os import getenv                       # Get env variables
from sys import argv                        # Argument vector
from requests import post                   # Post to endpoint
import json                                 # Transform respond to json format
from PIL import Image                       # Open image to display
import matplotlib.pyplot as plt             # Show image and extracted text
from matplotlib.patches import Rectangle    # Draw the rectangles

# Loading values of env file
load_dotenv(".env")
base_endpoint = getenv('base_endpoint')
subscription_key = getenv('subscription_key')

# Remote image
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/" + \
    "Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png"

# Local image
image_path = "input/atoms.png"
image_data = open(image_path, "rb").read()

# Constructing post request format
source = argv[1]
ocr_url = base_endpoint + "ocr"
params = {'language': 'unk', 'detectOrientation': 'true'}
if source == "local":
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    response = post(ocr_url, headers=headers, params=params, data=image_data)
else:
    headers = {'Ocp-Apim-Subscription-Key': subscription_key} 
    data = {'url': image_url}
    response = post(ocr_url, headers=headers, params=params, json=data)

# Printing response on JSON format
#print(json.dumps(analysis, indent=4, sort_keys=True))
    
# Extract the word bounding boxes and text
resp_json = response.json()
text = ''
line_infos = [region["lines"] for region in resp_json["regions"]]
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
output_file = "output/" + source + ".txt"
f = open(output_file,"w") 
f.write(text) 
f.close()

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