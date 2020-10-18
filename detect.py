import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    userFace = False
    userEyes = False
    distance = False

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) > 0:
        userFace = True

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        distance = 6421 / w

        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) > 0:
            userEyes = True


        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


    return [img, userFace, userEyes , distance]
    # return img
