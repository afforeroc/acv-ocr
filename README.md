---
topic: 
  - Sample
languages:
  - Python 
products:
  - Azure
---

# Sample Solution that uses OCR of Computer Vision
This python code is a quickstart that show how to use OCR of Computer Vision API for local and remote images

## Prerequisites
- [Python 3.7.4+](https://www.python.org/)
- [An Azure Subscription Key](https://portal.azure.com/#home)
- [A Computer Vision Instance](https://azure.microsoft.com/en-us/try/cognitive-services/?api=computer-vision)

## Setup
1. Clone or download this sample repository
2. Open your console on cloned folder
3. Install required libraries for python
```
pip install -r requirements.txt
```
4. Modify the *.env* file with your credentials of Computer Vision Service

## Running the sample
1. Run the sample using a local image: *atoms.png*
```
python acv-ocr-local.py
```
2. Run the sample using [this](https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png) remote image
```
python acv-ocr-local.py
```

## Documentation
* [Azure Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)
* [Quickstart: Extract printed text (OCR) using the Computer Vision REST API and Python](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-print-text)
* [Sample Solution that uses the Computer Vision SDK](https://github.com/Azure-Samples/cognitive-services-dotnet-sdk-samples/tree/master/samples/ComputerVision)