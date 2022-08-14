import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        
        # Wrist (O)
        wrist = 0
        wrist_normalizedLandmark = hand_landmarks.landmark[wrist]
        wrist_pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(wrist_normalizedLandmark.x, wrist_normalizedLandmark.y, frameWidth, frameHeight)

        # cv2.circle(frame, wrist_pixelCoordinatesLandmark, 5, (255, 255, 0), -1)

        # Thumb tip (A)
        thumbtip = 4
        thumbtip_normalizedLandmark = hand_landmarks.landmark[thumbtip]
        thumbtip_pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(thumbtip_normalizedLandmark.x, thumbtip_normalizedLandmark.y, frameWidth, frameHeight)

        # cv2.circle(frame, thumbtip_pixelCoordinatesLandmark, 5, (0, 255, 0), -1)

        # Index finger tip (B)
        index_fingertip = 8
        index_fingertip_normalizedLandmark = hand_landmarks.landmark[index_fingertip]
        index_fingertip_pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(index_fingertip_normalizedLandmark.x, index_fingertip_normalizedLandmark.y, frameWidth, frameHeight)

        # cv2.circle(frame, index_fingertip_pixelCoordinatesLandmark, 5, (0, 255, 0), -1)

        # Middle finger tip (C)
        mid_fingertip = 12
        mid_fingertip_normalizedLandmark = hand_landmarks.landmark[mid_fingertip]
        mid_fingertip_pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(mid_fingertip_normalizedLandmark.x, mid_fingertip_normalizedLandmark.y, frameWidth, frameHeight)

        # cv2.circle(frame, mid_fingertip_pixelCoordinatesLandmark, 5, (0, 255, 0), -1)

        # Ring finger tip (D)
        ring_fingertip = 16
        ring_fingertip_normalizedLandmark = hand_landmarks.landmark[ring_fingertip]
        ring_fingertip_pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(ring_fingertip_normalizedLandmark.x, ring_fingertip_normalizedLandmark.y, frameWidth, frameHeight)

        # cv2.circle(frame, ring_fingertip_pixelCoordinatesLandmark, 5, (0, 255, 0), -1)

        # Pinky tip (E)
        pinkytip = 20
        pinkytip_normalizedLandmark = hand_landmarks.landmark[pinkytip]
        pinkytip_pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(pinkytip_normalizedLandmark.x, pinkytip_normalizedLandmark.y, frameWidth, frameHeight)

        # cv2.circle(frame, pinkytip_pixelCoordinatesLandmark, 5, (0, 255, 0), -1)
        
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()