from picamera import PiCamera
from time import sleep
# Import OpenCV library
import cv2

# Load a cascade file for detecting faces
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml");

# Load image
camera = PiCamera()
camera.rotation = 180
camera.resolution = (620, 480)
camera.framerate = 15
camera.start_preview()
#sleep(0.075)
camera.capture('/home/pi/Downloads/code/max.jpg')
camera.stop_preview()

image = cv2.imread("max.jpg")

# Convert into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Look for faces in the image using the loaded cascade file
faces=faceCascade.detectMultiScale(gray, 1.2, 5)
for (x,y,w,h) in faces:
        # Create rectangle around faces
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

# Create the resizeable window
cv2.namedWindow('myphoto', cv2.WINDOW_NORMAL)

# Display the image
cv2.imshow('myphoto', image)

# Wait until we get a key
k=cv2.waitKey(0)

# If pressed key is 's'
if k == ord('s'):
    # Save the image
    cv2.imwrite('convertedimage.jpg', image)
    # Destroy all windows
    cv2.destroyAllWindows()
# If pressed key is ESC
elif k == 27:
    # Destroy all windows
    cv2.destroyAllWindows()