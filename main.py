import cv2
from hand_detector import HandDetector


def main():

    cap = cv2.VideoCapture(0)

    detector = HandDetector()

    while True:

        success, frame = cap.read()

        if not success:
            print("Could not access camera.")
            break

        # Flip camera for natural movement
        frame = cv2.flip(frame, 1)

        # Detect hand
        results = detector.detect(frame)

        # Draw landmarks
        frame = detector.draw_landmarks(frame, results)

        cv2.imshow("Hand Gesture Mouse", frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()