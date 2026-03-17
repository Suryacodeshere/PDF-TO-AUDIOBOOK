import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter.filedialog import askopenfilename
import threading

pdf_text = ""
engine = None

def load_pdf():
    global pdf_text
    file = askopenfilename()
    if file:
        reader = PyPDF2.PdfReader(file)
        pdf_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pdf_text += text
        status_label.config(text="PDF Loaded")

def speak():
    global engine
    engine = pyttsx3.init()
    engine.say(pdf_text)
    engine.runAndWait()

def play_audio():
    if pdf_text:
        threading.Thread(target=speak).start()

def stop_audio():
    global engine
    if engine:
        engine.stop()
        engine = None
    status_label.config(text="Stopped")

root = tk.Tk()
root.title("PDF Audio Reader")
root.geometry("300x200")

tk.Button(root, text="Select PDF", command=load_pdf).pack(pady=10)
tk.Button(root, text="Play", command=play_audio).pack(pady=5)
tk.Button(root, text="Stop", command=stop_audio).pack(pady=5)

status_label = tk.Label(root, text="No PDF Selected")
status_label.pack(pady=10)

root.mainloop()