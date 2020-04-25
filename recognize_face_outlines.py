import face_recognition
from PIL import Image, ImageDraw

def rfo():
  print(' ...Option Two...\n')

  image = face_recognition.load_image_file("./img/recognize_faces/known_faces/jopa.jpg")

  face_landmarks_list = face_recognition.face_landmarks(image)

  selected_image = Image.fromarray(image)

  for face_landmarks in face_landmarks_list:  
    drow_on_selected_img = ImageDraw.Draw(selected_image, 'RGBA')

    # Eyesbrow
    drow_on_selected_img.polygon(face_landmarks['left_eyebrow'], fill=(255,69,0, 128))
    drow_on_selected_img.polygon(face_landmarks['right_eyebrow'], fill=(255,69,0, 128))
    drow_on_selected_img.line(face_landmarks['left_eyebrow'], fill=(255,215,0, 150), width=6)
    drow_on_selected_img.line(face_landmarks['right_eyebrow'], fill=(255,215,0, 150), width=6)

    # Lips
    drow_on_selected_img.polygon(face_landmarks['top_lip'], fill=(30,144,255, 128))
    drow_on_selected_img.polygon(face_landmarks['bottom_lip'], fill=(30,144,255, 128))
    drow_on_selected_img.line(face_landmarks['top_lip'], fill=(0,0,205, 100), width=8)
    drow_on_selected_img.line(face_landmarks['bottom_lip'], fill=(0,0,205, 100), width=8)

    # Eyes
    drow_on_selected_img.polygon(face_landmarks['left_eye'], fill=(255,0,0, 80))
    drow_on_selected_img.polygon(face_landmarks['right_eye'], fill=(255,0,0, 80))
    drow_on_selected_img.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(139,0,0, 180), width=6)
    drow_on_selected_img.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(139,0,0, 180), width=6)

    # Chin
    drow_on_selected_img.line(face_landmarks['chin'], fill=(255,99,71), width=6)

    # Nose
    drow_on_selected_img.line(face_landmarks['nose_bridge'], fill=(255,0,255, 80), width=6)  
    drow_on_selected_img.polygon(face_landmarks['nose_tip'], fill=(138,43,226, 180))  
    
  selected_image.show()
  # selected_image.save('./img/face_landmarks.jpg')