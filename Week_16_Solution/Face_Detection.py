# Import nexessary Libraries
import cv2 
import sys

#Inpute image Path
imagePath = sys.argv[1]

#convert the input image to gray scale
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# faceCascade object will load the Haar Cascade file
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

print("Found {0} Faces!".format(len(faces)))

#Draw a rectangle around the detected faces:
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#imread -- write the new image to your local filesystem
status = cv2.imwrite('faces_detected.jpg', image)
print("Image faces_detected.jpg written to filesystem: ", status)
