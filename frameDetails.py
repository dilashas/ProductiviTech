import cv2



########################################################################################################################

class customFrame:
    def __init__(self, frameNumber, facePresent, eyesPresent, faceDist, videoFps):
        self.frameNumber = frameNumber
        self.facePresent = facePresent
        self.eyesPresent = eyesPresent
        self.faceDist    = faceDist
        self.videoSecond = int(self.frameNumber/videoFps)


        self.attentive = False
        if self.facePresent and self.eyesPresent and self.faceDist < 40:
            self.attentive = True

########################################################################################################################