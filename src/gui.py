import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog

import pamphlet_maker as maker

class App:
    def __init__(self, root):
        #setting title
        self.root = root
        root.title("Pamphlet Maker")
        #setting window size
        width=600
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        button_file_select=tk.Button(root)
        button_file_select["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        button_file_select["font"] = ft
        button_file_select["fg"] = "#000000"
        button_file_select["justify"] = "center"
        button_file_select["text"] = "Select File"
        button_file_select.place(x=30,y=30,width=540,height=30)
        button_file_select["command"] = self.button_file_select_command

        check_pages=tk.Checkbutton(root, state = "disabled")
        ft = tkFont.Font(family='Times',size=10)
        check_pages["font"] = ft
        check_pages["fg"] = "#333333"
        check_pages["justify"] = "center"
        check_pages["text"] = "All Pages"
        check_pages.place(x=30,y=100,width=70,height=25)
        check_pages["offvalue"] = "0"
        check_pages["onvalue"] = "1"
        check_pages["command"] = self.check_pages_command

        GLineEdit_529=tk.Entry(root, state="disabled")
        GLineEdit_529["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_529["font"] = ft
        GLineEdit_529["fg"] = "#333333"
        GLineEdit_529["justify"] = "center"
        GLineEdit_529["text"] = ""
        GLineEdit_529.place(x=30,y=140,width=72,height=30)


        GLineEdit_958=tk.Entry(root, state="disabled")
        GLineEdit_958["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_958["font"] = ft
        GLineEdit_958["fg"] = "#333333"
        GLineEdit_958["justify"] = "center"
        GLineEdit_958["text"] = ""
        GLineEdit_958.place(x=170,y=140,width=72,height=30)

        GLabel_141=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_141["font"] = ft
        GLabel_141["fg"] = "#333333"
        GLabel_141["justify"] = "center"
        GLabel_141["text"] = "to"
        GLabel_141.place(x=100,y=140,width=70,height=25)

        button_make=tk.Button(root)
        button_make["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        button_make["font"] = ft
        button_make["fg"] = "#000000"
        button_make["justify"] = "center"
        button_make["text"] = "Make"
        button_make.place(x=30,y=200,width=70,height=25)
        button_make["command"] = self.button_make_command

        GLabel_147=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_147["font"] = ft
        GLabel_147["fg"] = "#333333"
        GLabel_147["justify"] = "center"
        GLabel_147["text"] = "No File Selected"
        GLabel_147.place(x=10,y=60,width=561,height=30)
        self.file_path_label = GLabel_147

    def button_file_select_command(self):
        self.file_path = filedialog.askopenfilename(initialdir="~")
        self.file_path_label["text"] = self.file_path



    def check_pages_command(self):
        print("check_clicked")


    def button_make_command(self):
        make_pdf(self.file_path)
        self.root.destroy()


def make_pdf(path):
    pdf = maker.rearange_pdf(path)
    f = filedialog.asksaveasfile(mode='wb', defaultextension=".pdf")
    pdf.write(f)
    f.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
