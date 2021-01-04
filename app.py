import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter import ttk
import json
from difflib import get_close_matches
from PyDictionary import PyDictionary


window = tk.Tk()


def MainWin(func):

    global window
    window.config(bg="#2B2D2F")
    window.title("Dictionary") 
    window.geometry("900x600+800+50")
    #pack(padx=2, pady=2, expand=True, fill='both')
    window.columnconfigure(0,weight=1)
    window.rowconfigure(2, weight=1)

    # TOP FRAME
    global frameTop
    frameTop = tk.LabelFrame(text="", bg="#2B2D2F", pady=5)
    frameTop.grid(row=0, column=0, columnspan=4, sticky="nsew")
    frameTop.columnconfigure(0, weight=1)
    frameTop.rowconfigure(0, weight=1)

    # Back Button
    """global btnBack
    btnBack = tk.Button(frameTop, text="\N{LEFTWARDS BLACK ARROW}", height=2, width=4)
    btnBack.grid(row=0, column=0, sticky="nw",padx=3, pady=4)"""
    

    # MIDDLE FRAME
    global frameMid
    frameMid = tk.LabelFrame(text="", bg="#2B2D2F", padx=5, pady=5)
    frameMid.grid(row=1, column=0, columnspan=3, rowspan=1, sticky="nsew")
    frameMid.columnconfigure(3, weight=1) 
    frameMid.rowconfigure(0, weight=1)

    # Search button
    click = Button(frameMid, text="SEARCH", fg="black", command=dictionary)
    click.config(height=2, width=15)
    click.grid(row=0, column=1, sticky="W", padx=2, pady=0)

    btnExit = Button(frameTop, text="EXIT", command= exit)
    btnExit.grid(row=0, column=1, padx=5)

    # BOTTOM FRAME
    global frameBtm
    frameBtm = tk.LabelFrame(text="", padx=5, pady=5, bg="#2B2D2F")
    frameBtm.grid(row=2, column=0, columnspan=4, sticky="nsew")
    frameBtm.columnconfigure(0, weight=1)   # Expand frame with resize
    frameBtm.rowconfigure(0, weight=1)    

    # Search Field 
    global entrySearch
    entrySearch = Entry(
        frameTop, 
        borderwidth=0, 
        relief=FLAT,
        justify=LEFT, 
        width=50,
        #insertbackground='#757575',
        #disableforeground='#757575'
        )
    entrySearch.insert(-1, "")
    entrySearch.grid(row=0, column=0, sticky="W", padx=5, pady=0)
    

    #Method to enter and retrieve word meaning
def dictionary():
    pydict = PyDictionary()
    word =entrySearch.get()
    try:
        result = pydict.meaning(word, disable_errors=True)
    except:
        return False
   
    textInfo = tk.Text(
        frameBtm,
        #text="\n\nType a word in to the search box above",
        #textvariablesearchText,
        #anchor="n",
        #justify="left",
        font=("bold", 18),
        height=25, 
        bg="#2B2D2F", 
        fg="#AEAEAE"
    )

    # Info Text Field
    textInfo.grid(row=2, column=0, sticky="nsew",columnspan=4)
    
    textInfo.insert(tk.END,result)

def exit():
    window.destroy()


if __name__ == '__main__':
    app = MainWin(dictionary)
    app2 = dictionary()
    window.mainloop()

