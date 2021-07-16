from tkinter import *
from PIL import ImageGrab, Image
import time
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\\Tesseract\\tesseract.exe'
class Snip:
    # defining methods
    # method to capture screen (left_x, top_y, right_x, bottom_y)
    def takeScreenshot(self,b_box=None):
        print(b_box)
        img = ImageGrab.grab(bbox=b_box)
        img = np.asarray(img)
        text = pytesseract.image_to_string(img)
        # img.show()
        # filename = "captured"
        # img.save(filename+".png")
        # time.sleep(2.0)
        self.master.destroy()
        output = Tk()
        output.resizable(height = False, width = False)
        # root window title and dimension 
        output.title("iSnip") 
        output.geometry('640x480')
        text_area = Text(output)
        text_area.pack(expand=1, fill="both")
        text_area.insert(END,text)
        output.mainloop()
    # defining on_button_release method
    def on_button_release(self, event):
        x = [self.start_x,self.cur_x]
        y = [self.start_y,self.cur_y]
        x.sort()
        y.sort()
        print(x)
        print(y)
        self.takeScreenshot((x[0],y[0], x[1],y[1]))
        # self.takeScreenshot((self.start_x,self.start_y,self.cur_x,self.cur_y))
        # self.master.destroy()
        
    # defining on_button_press method
    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.screenCanvas.create_rectangle(0, 0, 10, 10, outline='yellow', width=3, fill="blue")
        print("Left button pressed\n")

    # defining on_move_press method
    def on_move_press(self, event):
        self.cur_x , self.cur_y = event.x , event.y
        self.screenCanvas.coords(self.rect, self.start_x, self.start_y, self.cur_x, self.cur_y)
        # print(event.x,event.y)

    # Initialising constructor
    def __init__(self, master):
        self.master = master
        self.start_x = None
        self.start_y = None
        self.cur_x = None
        self.cur_y = None
        self.rect = None
        # configure the root widget
        self.master.title("Ck Snipper")
        self.master.attributes('-fullscreen', True)
        self.master.attributes('-alpha',.6)
        self.master.attributes("-transparent", "blue")
        # Creating canvas 
        self.screenCanvas = Canvas(self.master, cursor="cross", bg="grey11")
        self.screenCanvas.pack(fill=BOTH, expand=YES)

        # Binding the methods
        self.screenCanvas.bind("<ButtonPress-1>", self.on_button_press)
        self.screenCanvas.bind("<B1-Motion>", self.on_move_press)
        self.screenCanvas.bind("<ButtonRelease-1>", self.on_button_release)

if __name__ == '__main__':
    root = Tk()
    app = Snip(root)
    root.mainloop()
