# OCR-And-T2S-Conversion-In-Real-Time
# Real-Time OCR and Text-to-Speech Conversion

This project integrates Optical Character Recognition (OCR) with Text-to-Speech (TTS) technology to extract text from real-time webcam images and convert it into audible speech. It utilizes `pytesseract` for OCR, `OpenCV` for image capture and processing, and `pyttsx3` for converting the extracted text into speech.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher installed on your system.
- Access to a webcam for real-time image capture.

## Installation

To install the necessary libraries, run the following commands in your terminal or command prompt:
pip install opencv-python pytesseract pyttsx3 Pillow


Note: This project also requires the Tesseract-OCR engine to be installed on your system. Please refer to the [Tesseract OCR GitHub page](https://github.com/tesseract-ocr/tesseract) for installation instructions.

## Configuration

After installing Tesseract-OCR, you may need to update the script with the path to your Tesseract executable:
python pytesseract.pytesseract.tesseract_cmd = r'path_to_your_tesseract_executable'
Replace path_to_your_tesseract_executable with the actual path to the Tesseract executable on your machine.

## Usage
To use this project, run the script from your terminal or command prompt:


## python real_time_ocr_tts.py
Once the webcam window opens, position the text you wish to read aloud in front of the camera. Press 's' to capture the image and extract text for speech conversion. Press 'q' to quit the application.

## Contributing
Contributions to this project are welcome. Please fork the repository and open a pull request with your improvements.

## Acknowledgments
Thanks to the developers of pytesseract, OpenCV, and pyttsx3 for making their libraries available to the public.
Special thanks to Tesseract OCR for their powerful OCR engine.

