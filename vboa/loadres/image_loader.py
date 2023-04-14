from os import path
import re

import cv2 as cv
import numpy as np


class ImageLoader:
    @staticmethod
    def load(file_path: str) -> np.ndarray:
        image_file_pattern = re.compile('.(jpeg|png|jpg|tiff|bmp)$')

        if not image_file_pattern.search(file_path):
            raise RuntimeError(
                f'Incorrect loader select! {file_path} isn\'t image!')

        if not path.isfile(file_path):
            raise RuntimeError(f'{file_path} doesn\'t exists!')

        return cv.imread(file_path, 0)
