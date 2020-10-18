# ProductiviTech

#####Transforming Online Meetings Through Computer Vision

### `Deployment Status`
#### This project is deployed at [productivitech.herokuapp.com](https://productivitech.herokuapp.com/)

## Project Setup

In the project directory, you can run:

### `For Windows`
##### In your Command Prompt enter:

`python -m pip install virtualenv`

~~~~
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python -m flask run
~~~~

### `For Mac and Linux`
##### In your Command Prompt enter:

`python3 -m pip install virtualenv`

~~~~
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m flask run
~~~~

## Tesseract Binary Setup (Text Extraction)

### `On Linux`
~~~~
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
~~~~
### `On Mac`
~~~~
brew install tesseract
~~~~
