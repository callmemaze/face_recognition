import face_recognition
import os
import cv2
# Load the known images
path = "image"
images = []
known_face = []
dir = os.listdir(path)
for img in dir:
    image = cv2.imread(f'{path}/{img}')
    images.append(image)

for img in images:
    faces_encoding = face_recognition.face_encodings(img)[0]
    known_face.append(faces_encoding)

def rectangle(image, name):
    unknown_face_location = face_recognition.face_locations(image)[0]
    x1, y1, x2, y2 = unknown_face_location
    cv2.rectangle(image, (y2,x1), (y1,x2), (255,0,255), 2)
    cv2.rectangle(image, (y2,x2-35), (y1, x2), (0,255,0), cv2.FILLED)
    cv2.putText(image, name, (y2+6,x2-6), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255),2)
    cv2.imshow(name, image)
    cv2.waitKey(0)  

unknown_image = cv2.imread("unknown_test_image/unknown.jpg")
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

for unknown_face_encoding in unknown_face_encodings:
    results = face_recognition.compare_faces(known_face, unknown_face_encoding, tolerance=0.6)
    name = "Unknown"
    if results[0]:
        name = "Bill Gates" 
        rectangle(unknown_image, name)
    elif results[1]:
        name = "Elon Musk"
        rectangle(unknown_image, name)
    elif results[2]:
        name = "Steve Jobs"
        rectangle(unknown_image, name)
    if name == "Unknown":
        rectangle(unknown_image, name)
    print(f"Found {name} in the photo!")
    