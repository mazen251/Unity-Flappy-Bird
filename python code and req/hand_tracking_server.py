
import cv2
import mediapipe as mp
import socket
import json

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

HOST = '127.0.0.1'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

client_socket, addr = server_socket.accept()

cap = cv2.VideoCapture(0)

try:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                data = {
                    'x': index_finger_tip.x,
                    'y': index_finger_tip.y,
                    'z': index_finger_tip.z
                }
                client_socket.sendall(json.dumps(data).encode('utf-8'))
        
        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break
finally:
    cap.release()
    server_socket.close()
    cv2.destroyAllWindows()
