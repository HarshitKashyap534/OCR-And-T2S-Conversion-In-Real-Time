import cv2
import pytesseract
import pyttsx3

# Update this line with the path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to capture images from the webcam and extract text when a key is pressed
def capture_and_extract_text():
    cap = cv2.VideoCapture(0) # Initialize the webcam
    print("Press 's' to capture and extract text from the current frame. Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read() # Read frame from the webcam
        if not ret:
            print("Failed to capture image")
            break

        cv2.imshow("Press 's' to scan", frame) # Display the captured frame

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'): # 's' key to scan the text
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            text = pytesseract.image_to_string(frame_rgb)
            print("Extracted Text:", text.strip())
            if text.strip():
                convert_text_to_speech(text)
            else:
                print("No text extracted from image.")
        elif key == ord('q'): # 'q' key to quit
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to convert text to speech using pyttsx3
def convert_text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in converting text to speech: {e}")

if __name__ == "__main__":
    capture_and_extract_text()
