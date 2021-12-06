import tkinter as tk
from tkinter.constants import CENTER, FLAT, RIDGE
from tkinter.font import BOLD
from PIL import ImageTk, Image
import os, os.path


class Gui:

    def __init__(self, w):
        self.window = w
        self.window.geometry("600x800")
        self.top = tk.Frame(self.window)
        self.input = {}
        self.top.pack(side="top")
        self.bottom = tk.Frame(self.window)
        self.bottom.pack(side="bottom")
        self.index = 0
        self.ImageList = []
        self.mainScreen()
        self.imageExtracter(self.ImageList,"C:\\Users\\agarw\\OneDrive\\Desktop\\NST GUI\\StyleImage")
    def imageExtracter(self,list,path):
        vaild_images =[".jpg",".gif",".png",".tga"]

        for f in os.listdir(path):
            ext = os.path.splitext(f)[1]
            if ext.lower() not in vaild_images:
                continue
            list.append(os.path.join(path,f))



    def styleDisplay(self):
        path = self.ImageList[0]
        img = ImageTk.PhotoImage(Image.open(path).resize((450, 350)))
        panel = tk.Label(self.window, image=img)
        contentPicture = tk.Label(
            self.window, text="Select The Style Image", bg="#292C6D", fg="white", font=("Helvetica", 25, BOLD))
        panel.image = img
        contentPicture.pack(side="top", fill="both",
                            expand="yes", padx=0, pady=0)
        panel.pack(side="top", expand="yes")
        self.backbuttonrender(panel)
        self.prevbuttonrender(panel)
        self.nextbuttonrender(panel)
        self.submitbuttonrenderStyle(panel)

    def nextbuttonrender(self, panel):
        next_button = tk.Button(self.window, text="Next >>", font=(
            "Hevlatica", 10, BOLD), background="#EC255A", fg="white", justify=CENTER, relief=RIDGE, width=10, height=1, command=lambda: self.next(panel))
        next_button.pack(in_=self.bottom, side="right")

    def prevbuttonrender(self, panel):
        prev_button = tk.Button(self.window, text=" << Previous",  font=(
            "Hevlatica", 10, BOLD), background="#EC255A", fg="white", justify=CENTER, relief=RIDGE, width=10, height=1, command=lambda: self.prev(panel))
        prev_button.pack(in_=self.bottom, side="left")

    def submitbuttonrenderStyle(self, panel):
        submit_button = tk.Button(self.window, text="Submit",  font=(
            "Hevlatica", 10, BOLD), background="#EC255A", fg="white", justify=CENTER, relief=RIDGE, width=10, height=1, command=lambda: self.submitStyle(panel, self.index))
        submit_button.pack(in_=self.bottom, side="right")

    def submitbuttonrenderContent(self, panel):
        submit_button = tk.Button(self.window, text="Submit",  font=(
            "Hevlatica", 10, BOLD), background="#EC255A", fg="white", justify=CENTER, relief=RIDGE, width=10, height=1, command=lambda: self.submitContent(panel, self.index))
        submit_button.pack(in_=self.bottom, side="right")

    def backbuttonrender(self, panel):
        back_button = tk.Button(self.window, text="Reset",  font=(
            "Hevlatica", 10, BOLD), background="#EC255A", fg="white", justify=CENTER, relief=RIDGE, width=10, height=1, command=lambda: self.mainScreenWrapper())
        back_button.pack(in_=self.bottom, side="left")

    def startbuttonrender(self, panel):
        back_button = tk.Button(self.window, text="Start",  font=(
            "Hevlatica", 20, BOLD), background="#EC255A", fg="white", justify=CENTER, relief=RIDGE, width=10, height=1, command=lambda: self.contentDisplayWraper())
        back_button.pack(in_=self.bottom, side="left")

    def contentDisplay(self):
        path = self.ImageList[0]
        print(path)
        img = ImageTk.PhotoImage(Image.open(path).resize((450, 350)))
        panel = tk.Label(self.window, image=img)
        contentPicture = tk.Label(
            self.window, text="SELECT THE CONTENT IMAGE", bg="#292C6D", fg="white", font=("Helvetica", 25, BOLD), pady=0)
        panel.image = img
        contentPicture.pack(side="top", fill="both",
                            expand="yes", padx=0, pady=0)
        panel.pack(side="top", expand="yes")
        self.prevbuttonrender(panel)
        self.nextbuttonrender(panel)
        self.submitbuttonrenderContent(panel)

    def contentDisplayWraper(self):
        self.clearFrame()
        self.window.geometry("600x800")
        self.top = tk.Frame(self.window)
        self.top.pack(side="top")
        self.bottom = tk.Frame(self.window)
        self.bottom.pack(side="bottom")
        self.contentDisplay()

    def next(self, panel):
        print(self.ImageList[self.index])
        img = ImageTk.PhotoImage(Image.open(
            self.ImageList[self.index]).resize((450, 350)))
        panel.configure(image=img)
        panel.image = img
        print(self.index)
        self.index += 1
        self.index %= len(self.ImageList)

    def prev(self, panel):
        img = ImageTk.PhotoImage(Image.open(
            self.ImageList[self.index]).resize((450, 350)))
        panel.configure(image=img)
        panel.img = img
        print(self.index)
        self.index -= 1
        self.index %= len(self.ImageList)

    def clearFrame(self):
        for w in self.window.winfo_children():
            w.destroy()

    def submitStyle(self, panel, index):
        print("Selected Image:"+str(index))
        self.input.update({"Style": index})
        self.clearFrame()
        self.window.geometry("600x800")
        self.top = tk.Frame(self.window)
        self.top.pack(side="top")
        self.bottom = tk.Frame(self.window)
        self.bottom.pack(side="bottom")
        self.styleDisplay()
        print(self.input)

    def submitContent(self, panel, index):
        print("Selected Image:"+str(index))
        self.input.update({"Content": index})
        self.clearFrame()
        self.window.geometry("600x800")
        self.top = tk.Frame(self.window)
        self.top.pack(side="top")
        self.bottom = tk.Frame(self.window)
        self.bottom.pack(side="bottom")
        self.styleDisplay()

    def mainScreen(self):
        img = ImageTk.PhotoImage(Image.open(
            "NEURAL STYLE TRANSFER.png").resize((600, 800)))
        panel = tk.Label(self.window, image=img)
        panel.image = img
        panel.pack(side="top", expand="yes")
        self.startbuttonrender(panel)

    def mainScreenWrapper(self):
        self.clearFrame()
        self.window.geometry("600x800")
        self.top = tk.Frame(self.window)
        self.top.pack(side="top")
        self.bottom = tk.Frame(self.window)
        self.bottom.pack(side="bottom")
        self.mainScreen()


if __name__ == "__main__":
    window = tk.Tk()
    mycolor = "#e9dbd5"
    window.title("Neural Style Transfer")
    window.configure(bg=mycolor)

    GUI = Gui(window)
    window.mainloop()
