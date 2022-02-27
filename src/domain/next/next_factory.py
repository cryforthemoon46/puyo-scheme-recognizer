import numpy as np

from src.constant import *
from src.domain.service import predict_color


def create_next(frame: np.ndarray, player: int) -> str:
    n_axis_puyo_img = frame[
                      AREA[player]['next']['axis']['y1']:
                      AREA[player]['next']['axis']['y2'],
                      AREA[player]['next']['axis']['x1']:
                      AREA[player]['next']['axis']['x2'],
                      ]
    n_child_puyo_img = frame[
                       AREA[player]['next']['child']['y1']:
                       AREA[player]['next']['child']['y2'],
                       AREA[player]['next']['child']['x1']:
                       AREA[player]['next']['child']['x2'],
                       ]
    nn_axis_puyo_img = frame[
                       AREA[player]['next_next']['axis']['y1']:
                       AREA[player]['next_next']['axis']['y2'],
                       AREA[player]['next_next']['axis']['x1']:
                       AREA[player]['next_next']['axis']['x2'],
                       ]
    nn_child_puyo_img = frame[
                        AREA[player]['next_next']['child']['y1']:
                        AREA[player]['next_next']['child']['y2'],
                        AREA[player]['next_next']['child']['x1']:
                        AREA[player]['next_next']['child']['x2'],
                        ]
    n_axis_puyo_color = predict_color(n_axis_puyo_img)
    n_child_puyo_color = predict_color(n_child_puyo_img)
    nn_axis_puyo_color = predict_color(nn_axis_puyo_img)
    nn_child_puyo_color = predict_color(nn_child_puyo_img)
    return (n_axis_puyo_color + n_child_puyo_color +
            nn_axis_puyo_color + nn_child_puyo_color)
