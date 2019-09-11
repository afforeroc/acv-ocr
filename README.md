---
topic: 
  - Sample
languages:
  - Python 
products:
  - Azure
---

# Sample Solution that uses OCR of Azure Computer Vision
This **Python** code is a quickstart that show how to use **OCR** of **Computer Vision API** for local and remote images

## Prerequisites
- [Python 3.7.4+](https://www.python.org/)
- [An Azure Subscription Key](https://portal.azure.com/#home)
- [A Computer Vision Instance](https://azure.microsoft.com/en-us/try/cognitive-services/?api=computer-vision)

## Setup
1. Clone or download this sample repository
2. Open your console on cloned folder
3. Install required libraries for **Python**
```
pip install -r requirements.txt
```
4. Modify the *.env* file with your **Computer Vision** credentials

## Running the sample
1. Run the sample using a local image
```
python acv-ocr.py local
```
2. Run the sample using a remote image
```
python acv-ocr.py remote
```

## Images Sources
* [Local image: Althea Gibson's quote](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Quote.JPG/320px-Quote.JPG)
* [Remote image: Democritus's quote](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Quote.JPG/320px-Quote.JPG)

## Documentation
* [Azure Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)
* [Quickstart: Extract printed text (OCR) using the Computer Vision REST API and Python](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-print-text)


