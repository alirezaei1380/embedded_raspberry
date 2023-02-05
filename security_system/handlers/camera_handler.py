from threading import Thread
import cv2

ip = "http://192.168.8.104:4747/video"

class CameraHandler(Thread):
    def __init__(self):
        super().__init__()
        self.current_frame = None

    def run(self):
        global ip
        vc = cv2.VideoCapture(ip)

        while True:
            ret, frame = vc.read()

            self.current_frame=frame
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite('test.jpg',frame)
                print('Successfully saved')


        vc.release()
        cv2.destroyAllWindows()

c = CameraHandler()
c.start()



def take_image():
    pass
