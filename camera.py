from cv2 import cv2

from detect import detect


class Camera(object):

    def __init__(self):
        # self.video = cv2.VideoCapture('SampleVideo.mp4')
        self.video = cv2.VideoCapture('ZoomCall_SS.png')

        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        if int(major_ver) < 3:

            fps = self.video.get(cv2.CV_CAP_PROP_FPS)
            print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
        else:
            self.fps = self.video.get(cv2.CAP_PROP_FPS)
            print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(self.fps))

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, img = self.video.read()

        frame, userFace, userEyes, distance = detect(img)

        ret, img = cv2.imencode('.jpg', frame)

        return [img.tobytes(), userFace, userEyes, distance]
