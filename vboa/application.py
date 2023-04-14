import cv2 as cv

from vboa.loadres.image_loader import ImageLoader, ImagesLoader

ESC_KEY_CODE = 27


def run_app(img_file: str | None, imgs_dir: str | None) -> None:
    if img_file:
        raw_data_img = ImageLoader.load(img_file)
        cv.imshow(winname='Image', mat=raw_data_img)
    elif imgs_dir:
        raw_data_images = ImagesLoader.load(imgs_dir)
        for file_name, raw_data in raw_data_images.items():
            cv.imshow(winname=f'Image {file_name}', 
                      mat=raw_data)
    else:
        cv.namedWindow("Blank", cv.WINDOW_AUTOSIZE)

    key_code = cv.waitKey(0)
    if key_code == ESC_KEY_CODE:
        cv.destroyAllWindows()
