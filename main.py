import cv2
import numpy as np

def nothing(x):
    pass

def mousecallback(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(f"H: %d | S: %d | V: %d" % (hsv_frame[y, x, 0], hsv_frame[y, x, 1], hsv_frame[y, x, 2]))


def main():
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

    cv2.namedWindow("CSV thresholds")
    cv2.createTrackbar("HUE min", "CSV thresholds", 0, 179, nothing)
    cv2.createTrackbar("HUE max", "CSV thresholds", 0, 179, nothing)
    cv2.createTrackbar("SATURATION min", "CSV thresholds", 0, 255, nothing)
    cv2.createTrackbar("SATURATION max", "CSV thresholds", 0, 255, nothing)
    cv2.createTrackbar("VALUE min", "CSV thresholds", 0, 255, nothing)
    cv2.createTrackbar("VALUE max", "CSV thresholds", 0, 255, nothing)

    cv2.namedWindow("Selected color")
    selected_color = np.zeros((300,300, 3), np.uint8)

    while True:
        check, original_frame = cam.read()

        global hsv_frame
        hsv_frame = cv2.cvtColor(original_frame, cv2.COLOR_BGR2HSV)


        #Displaying windows properly
        cv2.moveWindow("HSV", 0, 0)
        cv2.moveWindow("HUE", 0, 400)
        cv2.moveWindow("Saturation", 0, 800)
        cv2.moveWindow("Mask", 500, 0)
        cv2.moveWindow("Value", 500, 400)
        cv2.moveWindow("CSV thresholds", 1000, 0)

        cv2.imshow("HSV", hsv_frame)
        cv2.setMouseCallback("HSV", mousecallback)
        cv2.imshow("HUE", hsv_frame[:,:,0])
        cv2.imshow("Saturation", hsv_frame[:,:,1])
        cv2.imshow("Value", hsv_frame[:,:,2])

        h_min = cv2.getTrackbarPos("HUE min", "CSV thresholds")
        h_max = cv2.getTrackbarPos("HUE max", "CSV thresholds")
        s_min = cv2.getTrackbarPos("SATURATION min", "CSV thresholds")
        s_max = cv2.getTrackbarPos("SATURATION max", "CSV thresholds")
        v_min = cv2.getTrackbarPos("VALUE min", "CSV thresholds")
        v_max = cv2.getTrackbarPos("VALUE max", "CSV thresholds")

        lower_bound =  np.array([h_min, s_min, v_min])
        upper_bound = np.array([h_max, s_max, v_max])

        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

        cv2.imshow("Mask", mask)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cam.release()

if __name__ == "__main__":
    main()