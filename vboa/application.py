import cv2

ESC_KEY_CODE = 27

def run_app() -> None:
    cv2.namedWindow("Display", cv2.WINDOW_AUTOSIZE)

    key_code = cv2.waitKey(0)
    if key_code == ESC_KEY_CODE:
        cv2.destroyAllWindows()
