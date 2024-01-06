import cv2
import pyautogui
import mediapipe as mp
from ultralytics import YOLO

results = ""
model = ""



def objectDetector():
    global results
    global model
    model = YOLO("yolov8n.pt")
    results = model.predict(source="0", show=True)
    model.train()


def shutDownConfirmer():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5,
                           min_tracking_confidence=0.5)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        pyautogui.FAILSAFE = False
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                index_finger_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                thumb_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                middle_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                middle_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                if 0.02 > thumb_x - index_finger_x > -0.02 and 0.02 > thumb_y - index_finger_y > -0.02 and 0.02 > thumb_x - middle_x > -0.02 and 0.02 > thumb_y - middle_y > -0.02:
                    cap.release()
                    cv2.destroyAllWindows()
                    return True
                if 0.02 > thumb_x - index_finger_x > -0.02 and 0.02 > thumb_y - index_finger_y > -0.02 and thumb_x - middle_x > 0.02 and thumb_y - middle_y > 0.02:
                    cap.release()
                    cv2.destroyAllWindows()
                    return False


def handWithCursor():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5,
                           min_tracking_confidence=0.5)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        pyautogui.FAILSAFE = False
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                index_finger_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                thumb_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                middle_finger_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                middle_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                print(1920 - (index_finger_x * 1920), index_finger_y * 1080)
                pyautogui.moveTo(1920 - (index_finger_x * 1920), index_finger_y * 1080)
                if 0.02 > index_finger_x - middle_finger_x > -0.02 and 0.02 > index_finger_y - middle_finger_y > -0.02:
                    pyautogui.click(1920 - (index_finger_x * 1920), index_finger_y * 1080)
                if 0.02 > thumb_x - index_finger_x > -0.02 and 0.02 > thumb_y - index_finger_y > -0.02:
                    cap.release()
                    cv2.destroyAllWindows()
                    break


def handDetectionFunc():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5,
                           min_tracking_confidence=0.5)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                index_finger_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                thumb_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                # print(0.02 > thumb_x - index_finger_x > -0.02)
                print(thumb_x - index_finger_x)
                if index_finger_y < thumb_y:
                    hand_gesture = "up"
                elif index_finger_y > thumb_y:
                    hand_gesture = "down"
                else:
                    hand_gesture = "other"
                if 0.02 > thumb_x - index_finger_x > -0.02 and 0.02 > thumb_y - index_finger_y > -0.02:
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                if hand_gesture == "up":
                    pyautogui.press("volumeup")
                elif hand_gesture == "down":
                    pyautogui.press("volumedown")
