from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog, font
from PyPDF2.pdf import PdfFileReader
import pyttsx3
import PyPDF2
import os
from tkPDFViewer import tkPDFViewer as pdf

win = tk.Tk()
win.title("Audiobook")
win.geometry("1050x650")
win.wm_iconbitmap("icons/main.ico")
# win.maxsize(800, 330)
# win.minsize(600, 380)
win.resizable(False, False)

def open_path():
    global pdfpath
    try:
        pdfpath = filedialog.askopenfilename(initialdir=os.getcwd(
        ), title='Select Path', filetypes=(('pdf File', '*.pdf'), ('All files', '*.*')))
        pathvar.set(pdfpath)
        txtbox1.config(foreground='green')
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(win,
                        pdf_location=pdfpath,
                        width=65, height=39)
        v2.place(x=0, y=2)
    except:
        messagebox.showerror('invalid page','select page')    

def conversion():
    try:
        page_num = pagevar.get()
        voicess = voicevar.get()
        speeds = speechvar.get()
        try:
            pathloc = open(pdfpath, 'rb')
            pdfreader = PyPDF2.PdfFileReader(pathloc)
            from_page = pdfreader.getPage(page_num)   
            text = from_page.extractText()

            speak = pyttsx3.init()

            # choosing the voice type
            if(voicess == values[0]):
                voices = speak.getProperty('voices')
                speak.setProperty('voice', voices[0].id)
            if(voicess == values[1]):
                voices = speak.getProperty('voices')
                speak.setProperty('voice', voices[1].id)

            # sets speech rate acc to user input
            if(speeds == valuess[0]):
                speech_rate = speak.getProperty('rate')
                speak.setProperty('rate', 100)
            if(speeds == valuess[1]):
                speech_rate = speak.getProperty('rate')
                speak.setProperty('rate', 150)
            if(speeds == valuess[2]):
                speech_rate = speak.getProperty('rate')
                speak.setProperty('rate', 200)
            if(speeds == valuess[3]):
                speech_rate = speak.getProperty('rate')
                speak.setProperty('rate', 250)
            if(speeds == valuess[4]):
                speech_rate = speak.getProperty('rate')
                speak.setProperty('rate', 300)

            speak.say(text)
            speak.runAndWait()
            speak.stop()
            pageno.delete(0, END)
        except:
            messagebox.showerror('path not found','select the path')    
    except:
        messagebox.showerror('page not found','please enter page number')

def conversion2():
    try:
        page_num = pagevar.get()
    except:
        messagebox.showerror('page not found','please enter page number')    
    voicess = voicevar.get()
    speeds = speechvar.get()
    try:
        pathloc = open(pdfpath, 'rb')
        pdfreader = PyPDF2.PdfFileReader(pathloc)
        from_page = pdfreader.getPage(page_num) 
        text = from_page.extractText()

        speak = pyttsx3.init()

        # choosing the voice type
        if(voicess == values[0]):
            voices = speak.getProperty('voices')
            speak.setProperty('voice', voices[0].id)
        if(voicess == values[1]):
            voices = speak.getProperty('voices')
            speak.setProperty('voice', voices[1].id)

        # sets speech rate acc to user input
        if(speeds == valuess[0]):
            speech_rate = speak.getProperty('rate')
            speak.setProperty('rate', 100)
        if(speeds == valuess[1]):
            speech_rate = speak.getProperty('rate')
            speak.setProperty('rate', 150)
        if(speeds == valuess[2]):
            speech_rate = speak.getProperty('rate')
            speak.setProperty('rate', 200)
        if(speeds == valuess[3]):
            speech_rate = speak.getProperty('rate')
            speak.setProperty('rate', 250)
        if(speeds == valuess[4]):
            speech_rate = speak.getProperty('rate')
            speak.setProperty('rate', 300)

        # speak.say(text)
        speak.save_to_file(text, f'page {page_num}.mp3 ')
        speak.runAndWait()
        speak.stop()
        pageno.delete(0, END)
    except:
        messagebox.showerror('path not found','select the path')


def exit():
    win.destroy()

def note():
    os.system("C:\\Windows\\notepad.exe")

# image 1
pdfimg = tk.PhotoImage(file='icons/pdficon.png')
image1 = tk.Label(win, image=pdfimg, borderwidth=0)
image1.place(x=625, y=25)

# image2
audioimg = tk.PhotoImage(file='icons/mp3icon.png')
image2 = tk.Label(win, image=audioimg, borderwidth=0)
image2.place(x=825, y=25)

# image3
arrowimg = tk.PhotoImage(file='icons/arrow.png')
image3 = tk.Label(win, image=arrowimg, borderwidth=0)
image3.place(x=725, y=25)

# label1
addfilelbl = tk.Label(win, text="Open File", font=(
    "Bahnschrift SemiBold", 12, "bold"), height=2)
addfilelbl.place(x=560, y=126)

# entry box for pdf path
pathvar = tk.StringVar()
txtbox1 = tk.Entry(win, width=35, textvariable=pathvar, font=(
    'verdana', 8), background="white")
txtbox1.place(x=645, y=139,height=23)
txtbox1.insert('end','select pdf file')

# label2
speechratelbl = tk.Label(win, text="Speech Rate", font=(
    "Bahnschrift SemiBold", 12, "bold"), height=2)
speechratelbl.place(x=560, y=175)

# label3
voicelbl = tk.Label(win, text="Voice Type", font=(
    "Bahnschrift SemiBold", 12, "bold"), height=2)
voicelbl.place(x=560, y=223)

# combobox to select the voice type
voicevar = tk.StringVar()
voice_combobox = ttk.Combobox(
    win, width=14, textvariable=voicevar, background='white', state='readonly')
values = voice_combobox['values'] = (
    'Male', 'Female')
voice_combobox.current(0)
voice_combobox.place(x=660, y=234)

# combobox to select the speech rate
speechvar = tk.StringVar()
speed_combobox = ttk.Combobox(
    win, width=14, textvariable=speechvar, background='white', state='readonly')
valuess = speed_combobox['values'] = (
    '-2.0x', '-1.25x', '1.00x', '1.25x', '2.0x')
speed_combobox.current(2)
speed_combobox.place(x=660, y=186)

# label4
pagelbl = tk.Label(win, text="Page no.", font=(
    "Bahnschrift SemiBold", 12, "bold"), height=2)
pagelbl.place(x=778, y=222)

# ---------
pagevar = tk.IntVar()
pageno = tk.Entry(win, width=6, textvariable=pagevar,
                  font=('Bahnschrift SemiBold', 10))
pageno.place(x=855, y=234)

separator = ttk.Separator(win, orient='horizontal')
separator.place(x=524, y=350, width=525, height=10)


# open file loaction button
openbtn = tk.Button(win, text="open", command=open_path,
                    relief=RIDGE, bg='#DBD8E3', fg='#352F44', font=('verdana', 9, 'bold'), width=10)
openbtn.place(x=910, y=136)

# pdf2audio coverter button
convertbtn = tk.Button(win, text="Only Read", command=conversion,
                       relief=RIDGE, bg='#DBD8E3', fg='#352F44', font=('verdana', 10, 'bold'), width=10)
convertbtn.place(x=614, y=300)

# read and save button
convertbtn = tk.Button(win, text="Save", command=conversion2,
                       relief=RIDGE, bg='#DBD8E3', fg='#352F44', font=('verdana', 10, 'bold'), width=10)
convertbtn.place(x=790, y=300)

# exit button
quitbtn = tk.Button(win, text="Exit", command=exit,
                    relief=RIDGE, bg='#DBD8E3', fg='#352F44', font=('verdana', 10, 'bold'), width=10)
quitbtn.place(x=664, y=360)

# for opening notepad button
quitbtn = tk.Button(win, text="Make a Note", command=note,
                    relief=RIDGE, bg='#DBD8E3', fg='#352F44', font=('verdana', 10, 'bold'), width=10)
quitbtn.place(x=854, y=360)

win.mainloop()
