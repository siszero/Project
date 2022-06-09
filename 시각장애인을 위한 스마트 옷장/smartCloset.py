# Based on https://github.com/tensorflow/examples/blob/master/lite/examples/object_detection/raspberry_pi/README.md
#-*- coding: utf-8 -*-
import re
import cv2
import colorgram
from tflite_runtime.interpreter import Interpreter
import numpy as np
import webcolors
from gtts import gTTS
import os
import sys
import subprocess
import time
import speech_recognition as sr
from bluetooth import *

socket = BluetoothSocket(RFCOMM)
socket.connect(("98:D3:37:71:59:CF", 1))
print("bluetooth connected!")

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

def speak(temp):
    voice = gTTS(text = temp, lang ="ko")
    voice.save("/home/pi/Desktop/Project/tts.mp3")
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, "/home/pi/Desktop/Project/tts.mp3"])
    print("speaking------")
    time.sleep(1)

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]
def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def load_labels(path='/home/pi/Desktop/Project/TFODRPi/labels.txt'):
  """Loads the labels file. Supports files with or without index numbers."""
  with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    labels = {}
    for row_number, content in enumerate(lines):
      pair = re.split(r'[:\s]+', content.strip(), maxsplit=1)
      if len(pair) == 2 and pair[0].strip().isdigit():
        labels[int(pair[0])] = pair[1].strip()
      else:
        labels[row_number] = pair[0].strip()
  return labels

def set_input_tensor(interpreter, image):
  """Sets the input tensor."""
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = np.expand_dims((image-255)/255, axis=0)


def get_output_tensor(interpreter, index):
  """Returns the output tensor at the given index."""
  output_details = interpreter.get_output_details()[index]
  tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
  return tensor


def detect_objects(interpreter, image, threshold):
  """Returns a list of detection results, each a dictionary of object info."""
  image = cv2.resize(image, (320,320))
  set_input_tensor(interpreter, image)
  interpreter.invoke()
  # Get all output details
  boxes = get_output_tensor(interpreter, 0)
  classes = get_output_tensor(interpreter, 1)
  scores = get_output_tensor(interpreter, 2)
  count = int(get_output_tensor(interpreter, 3))

  results = []
  for i in range(count):
    if scores[i] >= threshold:
      result = {
          'bounding_box': boxes[i],
          'class_id': classes[i],
          'score': scores[i]
      }
      results.append(result)
  return results

def main():
    pattern = ""
    labels = load_labels()
    interpreter = Interpreter('/home/pi/Desktop/Project/TFODRPi/detect.tflite')
    interpreter.allocate_tensors()
    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']
    while True:
        data = str(socket.recv(1024))
        print(data)
        if '0' in data:
            time.sleep(7)
            f = open("/home/pi/Desktop/Project/TFODRPi/start", 'r')
            start = f.read()
            speak(start)
            f.close()
            time.sleep(1)
            r = sr.Recognizer()
            
            with sr.Microphone() as source:
                print("Say something!")
                try:
                    audio = r.listen(source)
                    print("You said: " + r.recognize_google(audio, language = "ko-KR"))
                    f = open("/home/pi/Desktop/Project/TFODRPi/mic", 'w')
                    sttMic = str(r.recognize_google(audio, language ="ko-KR"))

                    f.write(sttMic)
                    f.close()
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
            f = open("/home/pi/Desktop/Project/TFODRPi/mic", 'r')
            mic = f.read()
            f.close()
            
            cap = cv2.VideoCapture(0)
   
            ret, frame = cap.read()
                      res = detect_objects(interpreter, frame, 0.8)
            print(res)
            cap.release()
            cv2.destroyAllWindows()

            for result in res:
                ymin, xmin, ymax, xmax = result['bounding_box']
                xmin = int(max(1,xmin * CAMERA_WIDTH))
                xmax = int(min(CAMERA_WIDTH, xmax * CAMERA_WIDTH))
                ymin = int(max(1, ymin * CAMERA_HEIGHT))
                ymax = int(min(CAMERA_HEIGHT, ymax * CAMERA_HEIGHT))
                
                cv2.rectangle(frame,(xmin, ymin),(xmax, ymax),(0,255,0),3)
                cv2.putText(frame,labels[int(result['class_id'])],(xmin, min(ymax, CAMERA_HEIGHT-20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA) 
                if labels[int(result['class_id'])] == "Graphic":
                    pattern = "그래픽"
                elif labels[int(result['class_id'])] == "noPattern":
                    pattern = "무지"
                elif labels[int(result['class_id'])] == "Stripe":
                    pattern = "스트라이프"
                elif labels[int(result['class_id'])] == "Dot":
                    pattern = "땡땡이"
                else :
                    pattern = "체크"
            #cv2.imshow('Pi Feed', frame)
            
                
            if "옷정보" in mic :
                cv2.imwrite('result.jpg', frame)
                src = cv2.imread('result.jpg')
                h, w, c = src.shape
                print(h, w, c)
                dst = src[int(h/2)-100:int(h/2) + 100, int(w/2)-100: int(w/2)+100]
                cv2.imwrite('source.jpg',dst)
                colors = colorgram.extract('source.jpg', 3)

                red = [ 'crimson', 'red', 'firebrick', 'darkred', 'mistyrose']
                pink = ['p','p1','p2','redpink', 'fuchsiii','fuchsia','pink', 'lightpink', 'hotpink', 'deeppink', 'mediumvioletred', 'palevioletred', 'lightcoral','indianred', 'darksalmon', 'lightsalmon', 'salmon', 'magenta']
                orange = ['o', 'o1', 'o2','o3','yelloworagne', 'verydarkoragne', 'orange1', 'lightsalmon', 'coral', 'tomato', 'orangered', 'darkorange', 'orange', 'sandybrown',  'chocolate']
                yellow = ['y','cornsilk','gold','yellow','lightyellow','lemonchiffon','lightgoldenrodyellow','papayawhip', 'moccasin', 'peachpuff']
                purple = ['pu', 'lightpurple', 'lavender', 'thistle',  'plum',  'violet',  'orchid', 'mediumorchid', 'mediumpurple', 'amethyst',   'blueviolet',   'darkviolet', 'darkorchid', 'darkmagenta',
                        'purple','indigo','mediumslateblue']
                green = ['g','g1','g2', 'g3', 'greenyellow','chartreuse', 'lawngreen',  'lime', 'limegreen', 'palegreen' , 'lightgreen', 'mediumspringgreen', 'springgreen','mediumseagreen' ,'seagreen',
                        'forestgreen','green', 'darkgreen','yellowgreen','olivedrab', 'olive', 'darkolivegreen', 'mediumaquamarine', 'darkseagreen', 'lightseagreen','darkcyan',
                        'teal','palegoldenrod','khaki', 'darkkhaki']
                blue = ['slateblue','b','b1','b2','bluegray', 'aqua', 'lightcyan','paleturquoise', 'aquamarine', 'turquoise', 'mediumturquoise',  'darkturquiose','cadetblue','steelblue','lightsteelblue','powderblue',
                        'lightblue', 'skyblue', 'lightskyblue', 'deepskyblue', 'dodgerblue', 'cornflowerblue', 'royalblue', 'blue','mediumblue' ,  'slategray']
                navy = ['n', 'darkblue','navy','midnightblue']
                brown = [ 'blanchedalmond', 'bisque', 'navajowhite',  'wheat', 'burlywood', 'tan',  'rosybrown',  'goldenrod', 'darkgoldenrod',  'peru', 'saddlebrown',  'sienna']
                white = ['w','w1','giansboro','white','snow', 'honeydew', 'mintcream', 'azure',  'aliceblue',  'ghostwhite', 'whitesmoke', 'seashell' , 'beige', 'oldlace', 'floralwhite',  'ivory', 
                        'antiquewhite',  'linen','lavenderblush' , 'lightgrey',  'silver', 'darkgray']
                grey = ['mygray','gr', 'dimgray' , 'gray', 'greey']
                black = [ 'black']

                colorProportion ={}
                
                for i in range(0, 3):
                    rgb = colors[i].rgb
                #hsv.append(rgb2hsv(rgb.r, rgb.g, rgb.b))
                    print(colors[i].rgb)
                    
                #print(hsv[i])
                    requested_colour = (rgb.r, rgb.g, rgb.b)
                    actual_name, closest_name = get_colour_name(requested_colour)
                    #print(closest_name)
                    if closest_name in red : 
                        closest_name = '빨간색'
                    elif closest_name in pink:
                        closest_name = '분홍색'
                    elif closest_name in orange:
                        closest_name = '주황색'
                    elif closest_name in yellow:
                        closest_name = '노란색'
                    elif closest_name in green:
                        closest_name = '초록색'
                    elif closest_name in blue:
                        closest_name = '파란색'
                    elif closest_name in navy:
                        closest_name = '남색'
                    elif closest_name in purple:
                        closest_name = '보라색'
                    elif closest_name in white:
                        closest_name = '하얀색'
                    elif closest_name in black:
                        closest_name = '검은색'
                    elif closest_name in brown:
                        closest_name = '갈색'
                    elif closest_name in grey:
                        closest_name = '회색'
            
                        
                    print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)
                    
                    if closest_name not in colorProportion:
                        colorProportion[closest_name] = colors[i].proportion
                    else :
                        colorProportion[closest_name] += colors[i].proportion
                    
                    
                f = open("/home/pi/Desktop/Project/TFODRPi/inform", 'w')
                inform = "이 옷의 패턴은 " + pattern + "이고" + "이 옷의 색상은 "
                for key, value in colorProportion.items():
                    inform += key
                inform += " 입니다"
                f.write(inform)
                f.close()
                
                f = open("/home/pi/Desktop/Project/TFODRPi/inform", 'r')
                text = f.read()
                speak(text)
                f.close()
                                                                                                                                                                                                           
                os.remove("/home/pi/Desktop/Project/TFODRPi/mic")
                cap.release()
                cv2.destroyAllWindows()
                time.sleep(10)
                data = str(socket.recv(1024))
                print(data)
                    
if __name__ == "__main__":
    main()
