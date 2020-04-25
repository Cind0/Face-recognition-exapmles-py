import face_recognition
from PIL import Image, ImageDraw, ImageFont

def rf():
    print(' ...Option Three...\n')

    print('Load known image 1')
    cindo_image = face_recognition.load_image_file("./img/recognize_faces/known_faces/cindo.jpg")
    print('Get known image 1 encoding!')
    cindo_face_encoding = face_recognition.face_encodings(cindo_image)[0]
    print('Image encoding example \n', cindo_face_encoding)
    
    print('Load known image 2')
    viki_image = face_recognition.load_image_file("./img/recognize_faces/known_faces/viki.jpg")
    print('Get known image 2 encoding!')
    viki_face_encoding = face_recognition.face_encodings(viki_image)[0]

    print('Load known image 3')
    jopa_image = face_recognition.load_image_file("./img/recognize_faces/known_faces/jopa.jpg")
    print('Get known image 3 encoding!')
    jopa_face_encoding = face_recognition.face_encodings(jopa_image)[0]

    print('Load known image 4')
    franka_image = face_recognition.load_image_file("./img/recognize_faces/known_faces/franka.jpg")
    print('Get known image 4 encoding!')
    franka_face_encoding = face_recognition.face_encodings(franka_image)[0]

    print('Load unknown image')
    unknown_image = face_recognition.load_image_file("./img/recognize_faces/kipa.jpg")

    print('Get all face location in the unknown image')
    face_locations = face_recognition.face_locations(unknown_image, model="cnn")

    print('Get all face encodings from the unknown image')
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
    print('Matching face encodings and face locations, drawing rectangles and names on the image!')
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