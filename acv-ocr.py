from dotenv import load_dotenv              # Load env file
from os import getenv                       # Get env variables
from sys import argv                        # Argument vector
from requests import post, get              # Post to endpoint, get remote image
import json                                 # Transform respond to json format
from io import BytesIO                      # Convert bytes-like objects to bytes objects
from PIL import Image                       # Open image to display
import matplotlib.pyplot as plt             # Show image and extracted text
from matplotlib.patches import Rectangle    # Draw the rectangles

# Load values of env file
load_dotenv(".env")
base_endpoint = getenv('base_endpoint')
subscription_key = getenv('subscription_key')

# Local and remote images
local_image = "input/quote.jpg"
remote_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/" + \
    "Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png"

# Post request and response
source = argv[1]
ocr_url = base_endpoint + "ocr"
params = {'language': 'unk', 'detectOrientation': 'true'}
if source == "local":
    image_data = open(local_image, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    response = post(ocr_url, headers=headers, params=params, data=image_data)
else:
    data = {'url': remote_image}
    headers = {'Ocp-Apim-Subscription-Key': subscription_key} 
    response = post(ocr_url, headers=headers, params=params, json=data)
resp_json = response.json()

# Print response on JSON format
#print(json.dumps(resp_json, indent=4, sort_keys=True))
    
# Extract and print text
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

# Write output text
output_file = "output/" + source + ".txt"
f = open(output_file,"w") 
f.write(text) 
f.close()

# Display the image and overlay it with the extracted text
if source == "local":
    image = Image.open(local_image)
else:
    image = Image.open(BytesIO(get(remote_image).content))
plt.figure(figsize=(5, 5))
ax = plt.imshow(image, alpha=0.5)
for word in word_infos:
    bbox = [int(num) for num in word["boundingBox"].split(",")]
    text = word["text"]
    origin = (bbox[0], bbox[1])
    patch = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='y')
    ax.axes.add_patch(patch)
    plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
plt.show()