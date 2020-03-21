import face_recognition
from PIL import Image, ImageDraw

def df(imgFolderLocation, img):
  print(' ...Option One...\n')

  image = face_recognition.load_image_file(imgFolderLocation + img)
  print('Image {} imported...'.format(img))
  
  print('Procesing image > detecting faces!...')
  # This metod returns a list of face coordiantes 
  face_locations = face_recognition.face_locations(image, model="cnn")

  # Load the same image to Pillow.py to draw on
  selected_img = Image.open(imgFolderLocation + img)

  print('Drawing rectangles...')
  for face_location in face_locations:

    y0, x1, y1, x0 = face_location

    # Init draw on img
    drow_on_selected_img = ImageDraw.Draw(selected_img)

    # (x0,y0)------
    # |           |
    # |           |
    # |           |
    # |           |
    # ------(x1,y1)
    drow_on_selected_img.rectangle([(x0, y0), (x1, y1)], outline="#ffffff", width=3)

  print('Show image...\n\n')
  selected_img.show()