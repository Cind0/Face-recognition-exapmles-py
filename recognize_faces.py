import face_recognition
from PIL import Image, ImageDraw, ImageFont

def rf():
    print(' ...Option Three...\n')

    cindo_image = face_recognition.load_image_file("./img/recognize_faces/known_faces/cindo.jpg")
    cindo_face_encoding = face_recognition.face_encodings(cindo_image)[0]
    
    viki_image = face_recognition.load_image_file("./img/recognize_faces/known_faces/viki.jpg")
    viki_face_encoding = face_recognition.face_encodings(viki_image)[0]

    jopa_image = face_recognition.load_image_file("./img/recognize_faces/known_faces/jopa.jpg")
    jopa_face_encoding = face_recognition.face_encodings(jopa_image)[0]

    franka_image = face_recognition.load_image_file("./img/recognize_faces/known_faces/franka.jpg")
    franka_face_encoding = face_recognition.face_encodings(franka_image)[0]

    unknown_image = face_recognition.load_image_file("./img/recognize_faces/kipa.jpg")

    face_locations = face_recognition.face_locations(unknown_image, model="cnn")
    
    unknown_face_encoding = face_recognition.face_encodings(unknown_image, known_face_locations=face_locations, num_jitters=1)
    
    selected_img = Image.fromarray(unknown_image)
    fnt = ImageFont.truetype("./font/OpenSans-Regular.ttf", 16)
    
    known_faces_encodings = [
        cindo_face_encoding,
        viki_face_encoding,
        jopa_face_encoding,
        franka_face_encoding
    ]

    known_face_names = [
        "cindo",
        "viki",
        "jopa",
        "franka"
    ]
                        # combine unknown fece encoding with thier location on the image
    for unknown_face in zip(unknown_face_encoding, face_locations):
        results = face_recognition.compare_faces(known_faces_encodings, unknown_face[0])

        name="Unknown"
        if True in results:
            first_match_index = results.index(True)
            name = known_face_names[first_match_index]
        
        y0, x1, y1, x0 = unknown_face[1]

        drow_on_selected_img = ImageDraw.Draw(selected_img)

        drow_on_selected_img.rectangle([(x0, y0), (x1, y1)], outline="#ffffff", width=2)
        drow_on_selected_img.text((x0, y1), name, (255, 255, 255), font=fnt)
  
    selected_img.show()
    # selected_img.save('./img/racognize_faces.jpg')