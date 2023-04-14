import cv2 as cv

from vboa.loadres.image_loader import ImageLoader

ESC_KEY_CODE = 27


def run_app() -> None:
    raw_data_img = ImageLoader.load(
        '/home/andrwnv/workflow/vision-based-obstacle-avoidance-system/vboa/datasets/tree-500x500.jpeg')
    cv.imshow(winname='Image', mat=raw_data_img)

    key_code = cv.waitKey(0)
    if key_code == ESC_KEY_CODE:
        cv.destroyAllWindows()
