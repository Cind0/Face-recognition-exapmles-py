print("Loading modules...")
from pynput.keyboard import Key, Listener
from detect_faces import df

detectFacesImgFolderLocation = "./img/detect_faces/"
detectFacesImg = "scientists.jpg"

recognizeFacesImgFolderLocation = "./img/recognize_faces/"

def print_options():
  print(
    "-------------Select option:-------------\n"
    "1 > Detect faces\n"
    "TODO: 2 > Recognize faces\n"
    "TODO: 3 > Recognize face outlines\n"
    "-------------To Exit pres ESC:----------\n"
  )

print_options()

def on_release(key):
  formatedKey = '{}'.format(key)
  
  if "1" in formatedKey:
    df(detectFacesImgFolderLocation, detectFacesImg)
    print_options()
    pass
  elif "2" in formatedKey:
    print("Nop!")
    print_options()
    pass
  elif "3" in formatedKey:
    print("Nop!")
    print_options()
    pass
  elif key == Key.esc:
    # Stop listener
    return False

# Collect events until released
with Listener(on_release=on_release) as listener:listener.join()
