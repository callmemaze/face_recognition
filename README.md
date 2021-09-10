# face_recognition

face recognition system using face_recognition.
face_recognition is a python library created by Adam Geitgey. The system encode the face of the image and store in a known face list. The system can identify three faces Bill gates, Elon Musk and Steve Jobs. 

- face_recognition
Recognize and manipulate faces from Python or from the command line with
the world’s simplest face recognition library.
Built using dlib’s state-of-the-art face recognition
built with deep learning. The model has an accuracy of 99.38% on the
Labeled Faces in the Wild benchmark.


The system has face encodings of three face Bill gates , Elon and steve jobs but we can add more face as we want by adding the image in the image folder and passing in into the face_encodings method
After the it is added into the known face the system can identify the face

I have provided the image folder which contain the face to encode and unknown_test_image folder to test if the system actually identify the face or not.

face_recognition library cannot detect the face taken by the mobile camera because of the EXIF tag so below code may help
```javascript
image = PIL.Image.open("imagePath")
image_exif = image._getexif()
image_orientation = image_exif[274]
if image_orientation == 2:
    print("2")
    image = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
if image_orientation == 3:
    print("3")
    image = image.transpose(PIL.Image.ROTATE_180)
if image_orientation == 4:
    print("4")
    image = image.transpose(PIL.Image.FLIP_TOP_BOTTOM)
if image_orientation == 5:
    print("5")
    image = image.transpose(PIL.Image.FLIP_LEFT_RIGHT).transpose(PIL.Image.ROTATE_90)
if image_orientation == 6:
    print("6")
    image = image.transpose(PIL.Image.ROTATE_270)
if image_orientation == 7:
    print("7")
    image = image.transpose(PIL.Image.FLIP_TOP_BOTTOM).transpose(PIL.Image.ROTATE_90)
if image_orientation == 8:
    print("8")
    image = image.transpose(PIL.Image.ROTATE_90)
image = np.array(image.convert('RGB'))
```


