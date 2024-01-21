import face_recognition
import cv2
import time  # Required to use delay functions
import numpy as np
from cvzone.SerialModule import SerialObject

ArduinoSerial = SerialObject('com8')  # Create Serial port object called arduinoSerialData
time.sleep(2)  # wait for 2 seconds for the communication to get established
video_capture = cv2.VideoCapture(0)

imgEsha = face_recognition.load_image_file('D:\Consaltation\Door Lock using Face Recognisation\Face_Recognition_System\Known_Face\Esha.jpg')
imgEsha_encoding = face_recognition.face_encodings(imgEsha)[0]

imgNadim = face_recognition.load_image_file('D:\Consaltation\Door Lock using Face Recognisation\Face_Recognition_System\Known_Face\Hossain .jpg')
imgNadim_encoding = face_recognition.face_encodings(imgNadim)[0]

imgSaif = face_recognition.load_image_file('D:\Consaltation\Door Lock using Face Recognisation\Face_Recognition_System\Known_Face\Saif.jpg')
imgSaif_encoding = face_recognition.face_encodings(imgSaif)[0]

imgShafayet = face_recognition.load_image_file('D:\Consaltation\Door Lock using Face Recognisation\Face_Recognition_System\Known_Face\Shafayet.jpg')
imgShafayet_encoding = face_recognition.face_encodings(imgShafayet)[0]

known_face_encodings = [
    imgEsha_encoding,
    imgNadim_encoding,
    imgSaif_encoding,
    imgShafayet_encoding,

]
known_face_names = [
    "Esha",
    "Nadim",
    "Saif",
    "Shafhyet",
]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                ArduinoSerial.sendData([1, 0])
                print(0)
            else:
                ArduinoSerial.sendData([0, 0])
                print(1)

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()