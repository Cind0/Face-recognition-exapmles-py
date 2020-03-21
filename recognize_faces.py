import face_recognition
from PIL import Image, ImageDraw, ImageFont


def rf():
    print(' ...Option Two...\n')

    # Load the jpg files into numpy arrays
    einstein_image = face_recognition.load_image_file("./img/recognize_faces/Einstein.jpg")
    unknown_image = face_recognition.load_image_file("./img/recognize_faces/einstein-birthday.jpg")

    face_locations = face_recognition.face_locations(unknown_image, model="cnn")
    
    try:
        einstein_face_encoding = face_recognition.face_encodings(einstein_image)[0]
        unknown_face_encoding = face_recognition.face_encodings(unknown_image, known_face_locations=face_locations, num_jitters=1)
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

    known_faces = [
        einstein_face_encoding
    ]

    selected_img = Image.open("./img/recognize_faces/einstein-birthday.jpg").convert("RGB")
    fnt = ImageFont.truetype("./font/OpenSans-Regular.ttf", 16)

    for unknown_face in zip(unknown_face_encoding, face_locations):
        results = face_recognition.compare_faces(known_faces, unknown_face[0])

        name="Unknown"
        if True in results:
            name="Einstein"
        
        y0, x1, y1, x0 = unknown_face[1]

        drow_on_selected_img = ImageDraw.Draw(selected_img)

        drow_on_selected_img.rectangle([(x0, y0), (x1, y1)], outline="#ffffff", width=2)
        drow_on_selected_img.text((x0, y1), name, (255, 255, 255), font=fnt)
  
    selected_img.show()
    # selected_img.save('wup.jpg')
rf()