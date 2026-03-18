import cv2
import mediapipe as mp
import pyautogui

# Screen size
screen_w, screen_h = pyautogui.size()

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    h, w, _ = img.shape

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lm_list = []

            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            if len(lm_list) != 0:
                # Index finger tip (id=8)
                x1, y1 = lm_list[8][1], lm_list[8][2]

                # Middle finger tip (id=12)
                x2, y2 = lm_list[12][1], lm_list[12][2]

                # Convert to screen coordinates
                screen_x = int((x1 / w) * screen_w)
                screen_y = int((y1 / h) * screen_h)

                # 👉 Mouse Movement (Index finger)
                pyautogui.moveTo(screen_x, screen_y)

                # 👉 Scroll Control
                # If index finger is up and middle is down → Scroll UP
                if y1 < y2 - 40:
                    pyautogui.scroll(20)

                # If middle finger is up and index is down → Scroll DOWN
                elif y2 < y1 - 40:
                    pyautogui.scroll(-20)

    cv2.imshow("Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()