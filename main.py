import cv2
import pyautogui

from hand_detector import HandDetector
from gesture_recognizer import GestureRecognizer
from mouse_controller import MouseController


def main():

    # Camera
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Modules
    detector = HandDetector()
    recognizer = GestureRecognizer()
    mouse = MouseController()

    screen_width, screen_height = pyautogui.size()

    # Camera frame size
    frame_width = 1280
    frame_height = 720

    # Click control
    left_clicked = False
    right_clicked = False

    while True:

        success, frame = cap.read()

        if not success:
            print("Camera not available")
            break

        # Mirror camera
        frame = cv2.flip(frame, 1)

        # Detect hand
        results = detector.detect(frame)

        gesture = "NO HAND"

        if results.multi_hand_landmarks:

            # Get first hand
            hand = results.multi_hand_landmarks[0]

            # Draw landmarks
            detector.draw_landmarks(frame, results)

            # Recognize gesture
            gesture = recognizer.recognize(
                hand.landmark
            )

            # -------------------------
            # MOVE CURSOR
            # -------------------------

            if gesture == "MOVE":

                index = hand.landmark[8]

                # Convert camera coordinates → screen coordinates
                screen_x = int(
                    index.x * screen_width
                )

                screen_y = int(
                    index.y * screen_height
                )

                mouse.move(screen_x, screen_y)

            # -------------------------
            # LEFT CLICK
            # -------------------------

            elif gesture == "LEFT_CLICK":

                if not left_clicked:

                    mouse.left_click()

                    left_clicked = True

            else:

                left_clicked = False

            # -------------------------
            # RIGHT CLICK
            # -------------------------

            if gesture == "RIGHT_CLICK":

                if not right_clicked:

                    mouse.right_click()

                    right_clicked = True

            else:

                right_clicked = False

        else:

            left_clicked = False
            right_clicked = False

        # Display gesture
        cv2.putText(
            frame,
            f"Gesture: {gesture}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "Hand Gesture Mouse",
            frame
        )

        # Q → Exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()