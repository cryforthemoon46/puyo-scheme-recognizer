import argparse
import cv2
import numpy as np

from src.constant import *
from src.domain.next import create_next, NextObserver

parser = argparse.ArgumentParser()
parser.add_argument('--path')


def _parse_args():
    args = parser.parse_args()
    return args


def get_video_capture(path: str) -> cv2.VideoCapture:
    if path:
        cap = cv2.VideoCapture(path)
    else:
        cap = cv2.VideoCapture(1)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 270)

    return cap


def get_frame(cap: cv2.VideoCapture) -> np.ndarray:
    _, frame = cap.read()
    frame = cv2.resize(frame, (480, 270))
    return frame


def predict_puyo_scheme_number(tsumo: str) -> str:
    with open('assets/puyo_scheme_list.txt') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith(tsumo):
                return i + 1


class PuyoSchemeRecognizer:
    def __init__(self):
        self._args = _parse_args()
        self._cap = get_video_capture(self._args.path)
        self._next_observer = NextObserver()
        self._puyo_scheme_num = 0

    def run(self):
        while self._cap.isOpened():
            frame = get_frame(self._cap)
            if np.mean(frame) < 90:
                self._next_observer = NextObserver()
                with open("./output/puyo_scheme_number.txt", mode="w",
                          encoding='utf-8') as f:
                    f.write('解析中…')

            next_color = create_next(frame, PLAYER1)
            self._next_observer.forward(next_color)

            if len(self._next_observer.history) == 10:
                self._puyo_scheme_num = predict_puyo_scheme_number(
                    self._next_observer.history)
                with open("./output/puyo_scheme_number.txt", mode="w") as f:
                    f.write(str(self._puyo_scheme_num))


if __name__ == '__main__':
    puyo_scheme_recognizer = PuyoSchemeRecognizer()
    puyo_scheme_recognizer.run()
