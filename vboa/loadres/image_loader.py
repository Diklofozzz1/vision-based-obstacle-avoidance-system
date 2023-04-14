from os import path, walk
import re

from typing import Dict

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


class ImagesLoader:
    @staticmethod
    def load(dir_path: str) -> Dict[str, np.ndarray]:
        images = {}

        for root, _, f in walk(dir_path):
            for file in f:
                try:
                    filepath = path.join(root, file)
                    images[filepath] = ImageLoader.load(filepath)
                except:
                    continue

        return images
