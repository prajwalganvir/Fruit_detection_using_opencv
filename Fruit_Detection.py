from PIL import Image,ImageTk
import tkinter
import cv2
import tkinter as tk
r = tkinter.Tk()
r.geometry("900x700")

h12=tkinter.Label(text=" ",bg="black",height=45,width=103)
h12.place(x=80,y=40)
h12=tkinter.Label(text=" ",bg="#FFFACD",height=43,width=100)
h12.place(x=90,y=50)

thres = 0.45  # Threshold to detect object

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(10, 70)

classNames = []
classFile = 'coco.names'

img=Image.open("fruitfull.png")
rimg=img.resize((700,200),Image.ANTIALIAS)
pimg=ImageTk.PhotoImage(rimg)
l=tkinter.Label(image=pimg)
l.place(x=90,y=50)

img1=Image.open("Detection.png")

rimg1=img1.resize((80,80),Image.ANTIALIAS)

pimg1=ImageTk.PhotoImage(rimg1)

l=tkinter.Label(image=pimg1)
l.place(x=160,y=100)
h1=tkinter.Label(text="FRUIT DETECTION AND\n IDENTIFICATION ",font=("arial",26,'bold'),fg="black")
h1.place(x=280,y=100,height=83)


def apple():
    h12.config(bg="#FF5C5C")


def mango():
    h12.config(bg="#fdbe02")


def banana():
    h12.config(bg="yellow")


def orange():
    h12.config(bg="#F88017")


def mix():
    with open(classFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

        configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        weightsPath = 'frozen_inference_graph.pb'

        net = cv2.dnn_DetectionModel(weightsPath, configPath)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        while True:
            success, img = cap.read()
            classIds, confs, bbox = net.detect(img, confThreshold=thres)
            print(classIds, bbox)

            if len(classIds) != 0:
                for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                    # cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                    #            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('Output', img)
            cv2.waitKey(1)


b1 = tkinter.Button(text = "APPLE",bg="lightseagreen",fg="white",height=4,width=17,font=("viking",12,'bold'),command=apple)
b1.place(x=200,y=300)
b2 = tkinter.Button(text = "MANG0",bg="lightseagreen",fg="white",height=4,width=17,font=("viking",12,'bold'),command=mango)
b2.place(x=560,y=300)
b1 = tkinter.Button(text = "BANANA",bg="lightseagreen",fg="white",height=4,width=17,font=("viking",12,'bold'),command=banana)
b1.place(x=200,y=450)
b1 = tkinter.Button(text = "ORANGE",bg="lightseagreen",fg="white",height=4,width=17,font=("viking",12,'bold'),command=orange)
b1.place(x=560,y=450)
bmix = tkinter.Button(text = "MIX FRUITS",bg="lightseagreen",fg="white",height=4,width=50,font=("viking",12,'bold'),command=mix)
bmix.place(x=210,y=580)


r.mainloop()
