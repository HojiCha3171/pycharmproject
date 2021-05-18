import cv2
import mediapipe as mp

import os

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
path_input = "C:\\Users\\tuzuk\\Desktop\\AboutCV\\BodyDitection_in"
path_output = "C:\\Users\\tuzuk\\Desktop\\AboutCV\\BodyDitection_out"
file_list = []
LEFT_INDEX_LIST = []
RIGHT_INDEX_LIST = []
mp_holistic = mp.solutions.holistic
num = 0

for file in os.listdir(path_input):
    if os.path.isfile(os.path.join(path_input, file)):
        file_list.append(path_input + "\\" + file)

print(file_list)

# For static images:
with mp_pose.Pose(
    static_image_mode=True,
    model_complexity=2,
    min_detection_confidence=0.5) as pose:
  for idx, file in enumerate(file_list):
    image = cv2.imread(file)
    image_height, image_width, _ = image.shape
    # Convert the BGR image to RGB before processing.
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.pose_landmarks:
      continue


    #print(num)


    LEFT_INDEX_x = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_INDEX].x * image_width
    LEFT_INDEX_y = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_INDEX].y * image_height

    RIGHT_INDEX_x = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_INDEX].x * image_width
    RIGHT_INDEX_y = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_INDEX].y * image_height

    LEFT_INDEX_LIST.append([int(LEFT_INDEX_x),int(LEFT_INDEX_y)])
    RIGHT_INDEX_LIST.append([int(RIGHT_INDEX_x),int(RIGHT_INDEX_y)])

    if len(LEFT_INDEX_LIST) >= 40:
      del LEFT_INDEX_LIST[0]

    if len(RIGHT_INDEX_LIST) >= 40:
      del RIGHT_INDEX_LIST[0]



    print(
        #f'Nose coordinates: ('
        #f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x * image_width}, '
        #f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].y * image_height})'
    )


    # Draw pose landmarks on the image.
    annotated_image = image.copy()
    mp_drawing.draw_landmarks(annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    if len(RIGHT_INDEX_LIST) == len(LEFT_INDEX_LIST):
        for i in range(len(RIGHT_INDEX_LIST)):
          cv2.circle(annotated_image,(LEFT_INDEX_LIST[i]),5,(255,0,0),-1)
          cv2.circle(annotated_image,(RIGHT_INDEX_LIST[i]), 5, (255, 0, 0), -1)
          i += 1

    else:
      print("err")

    cv2.imwrite(path_output + "\\" + str(idx) + '.png', annotated_image)
    num += 1

print("fin")

"""
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imshow('MediaPipe Pose', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
"""