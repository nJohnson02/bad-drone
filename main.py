from djitellopy import Tello
from multiprocessing import Process
import cv2
import time

def video_stream(tello):

    out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30,(648,488))

    while True:
        img = tello.get_frame_read().frame
        img = cv2.resize(img, (648,488))
        out.write(img)
        cv2.imshow("Image",img)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            tello.streamoff()
            break

    out.release()

def fly(tello):
    tello.takeoff()
    tello.move_up(60)
    tello.move_forward(300)
    tello.rotate_clockwise(90)
    tello.move_forward(150)
    tello.rotate_clockwise(90)
    tello.move_forward(300)
    tello.rotate_clockwise(90)
    tello.move_forward(150)
    tello.rotate_clockwise(90)
    tello.land()

if __name__ == '__main__':
    
    tello = Tello()
    tello.connect()
    print(tello.get_battery())

    tello.streamoff()
    tello.streamon()
    Process(target=video_stream, args=(tello,)).start()
    
    time.sleep(10)
    fly(tello)
