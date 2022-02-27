import numpy as np
import cv2

from src.constant import *


def predict_color(puyo_img: np.ndarray) -> str:
    height, width = puyo_img.shape[:2]
    circle_mask = np.zeros((height, width), np.uint8)
    cv2.circle(circle_mask, (width // 2, height // 2), height // 2,
               (255, 255, 255), -1)
    blue, green, red = cv2.mean(puyo_img, mask=circle_mask)[:3]
    for color, values in COLOR_RANGE.items():
        if not (values['blue']['lower'] < blue < values['blue']['upper']):
            continue
        if not (values['green']['lower'] < green < values['green']['upper']):
            continue
        if not (values['red']['lower'] < red < values['red']['upper']):
            continue
        return color
    return '_'
