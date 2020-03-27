print("Loading modules...")
from pynput.keyboard import Key, Listener
from detect_faces import df
from recognize_faces import rf

detect_faces_img_folder_location = "./img/detect_faces/"
detect_faces_img = "scientists.jpg"

recognizeFacesImgFolderLocation = "./img/recognize_faces/"

def print_options():
  print(
    "-------------Select option:-------------\n"
    "1 > Detect faces\n"
    "2 > Recognize faces\n"
    "TODO: 3 > Recognize face outlines\n"
    "-------------To Exit pres ESC:----------\n"
  )

print_options()

def on_release(key):
  formated_key = '{}'.format(key)
  
  if "1" in formated_key:
    df(detect_faces_img_folder_location, detect_faces_img)
    print_options()
    pass
  elif "2" in formated_key:
    rf()
    print_options()
    pass
  elif "3" in formated_key:
    print(" ...Nop!...\n")
    print_options()
    pass
  elif key == Key.esc:
    # Stop listener
    return False

# Collect events until released
with Listener(on_release=on_release) as listener:listener.join()
