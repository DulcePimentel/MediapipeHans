import cv2 
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# webcam input
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
     
     while True:
          ret, frame = cap.read()
          if ret == False:
              break
          height, width, _ = frame.shape
          frame = cv2.flip(frame,1)
          frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          results = hands.process(frame_rgb)
          # HANDEDNESS
          print("Handedness: ", results.multi_handedness)
          #HAND LANDMARKS
          #print("Hand landmarks: ", results.multi_hand_landmarks)
          if results.multi_hand_landmarks is not None:
               for hand in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                         frame, hand, mp_hands.HAND_CONNECTIONS,
                         mp_drawing.DrawingSpec(color=(255,0,255),thickness=3),
                         mp_drawing.DrawingSpec(color=(255,255,0),thickness=3))
          
          
          cv2.imshow("Frame", frame)
          if cv2.waitKey(1) & 0xFF == 27:
               break
cap.release()
cv2.destroyAllWindows()
     