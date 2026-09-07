import math


class GestureRecognizer:

    def distance(self, p1, p2):
        return math.sqrt(
            (p1.x - p2.x) ** 2 +
            (p1.y - p2.y) ** 2
        )

    def is_finger_up(self, landmarks, tip, pip):
        return landmarks[tip].y < landmarks[pip].y

    def recognize(self, landmarks):

        index_up = self.is_finger_up(landmarks, 8, 6)
        middle_up = self.is_finger_up(landmarks, 12, 10)
        ring_up = self.is_finger_up(landmarks, 16, 14)
        pinky_up = self.is_finger_up(landmarks, 20, 18)

        # Thumb + Index = LEFT CLICK
        index_pinch = self.distance(
            landmarks[4],
            landmarks[8]
        )

        if index_pinch < 0.06:
            return "LEFT_CLICK"

        # Index + Middle = RIGHT CLICK
        if index_up and middle_up and not ring_up and not pinky_up:
            return "RIGHT_CLICK"

        # Index only = MOVE
        if index_up and not middle_up and not ring_up and not pinky_up:
            return "MOVE"

        # Fist = PAUSE
        if not index_up and not middle_up and not ring_up and not pinky_up:
            return "PAUSE"

        return "NONE"