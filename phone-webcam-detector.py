import tkinter as tk
import cv2
from tensorflow.python.keras.models import load_model
import numpy as np
from PIL import Image, ImageTk
import datetime

def show_frame():
    _, frame = cap.read()  
    check_phone(frame)
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def check_phone(frame):
#        _, frame = cap.read()
        im = Image.fromarray(frame, 'RGB')
        im = im.resize((240, 240))
        im = np.asarray(im)
        im = np.expand_dims(im, axis=0)
        result = model.predict(im)
        if result[0] >= const:
            now = datetime.datetime.now()
            label5['text']= label4['text']
            label4['text']= label3['text']
            label3['text']= label2['text']
            label2['text']= label1['text']
            label1['text']= f'На веб-камере обнаружен телефон! ({now.strftime("%d-%m-%Y %H:%M:%S")})'

model = load_model('model.h5')

# важная константа - определяет вероятность
# при которой выход нейронки декодируется как наличие телефона
# если часто не распознается телефон там где он есть можно понизить до 0.5
# если часто видит телефон там где его нет можно повысить до 0.95
const = 0.9

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()

label1 = tk.Label(fg='red')
label1.pack()
label2 = tk.Label(fg='red')
label2.pack()
label3 = tk.Label(fg='red')
label3.pack()
label4 = tk.Label(fg='red')
label4.pack()
label5 = tk.Label(fg='red')
label5.pack()

#button = tk.Button(
#    text="Проверить наличие телефона",
#    width = 25,
#    height = 5,
#    bg = 'blue',
#    fg = 'yellow',
#    command = check_phone
#    )
#button.pack()

show_frame()
root.mainloop()
