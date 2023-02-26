import cv2
import numpy as np


def create_reset_frame(width, height):
    mat = cv2.cvtColor(np.zeros((height, width, 3), dtype=np.uint8), cv2.COLOR_RGB2BGR)
    mat = cv2.putText(mat, "Reset", (width // 2, height // 2), cv2.FONT_HERSHEY_COMPLEX, 2, 2)
    return mat
