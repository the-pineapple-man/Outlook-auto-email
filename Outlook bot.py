import os
import pyautogui
import time
from tkinter import *

def thiswaseasy(email, subject, text, repeat):
    if subject.strip() == "":
        thiswaseasywithoutsubject(email, text, repeat)
    else:
        os.startfile("Outlook")
        time.sleep(10)
        for _ in range(repeat):
            pyautogui.click(115, 102)
            time.sleep(0.5)
            pyautogui.write(email)
            time.sleep(0.5)
            pyautogui.press("ENTER")
            time.sleep(1)
            pyautogui.click(296, 330)
            time.sleep(0.5)
            pyautogui.write(subject)
            time.sleep(0.5)
            pyautogui.click(128, 380)
            pyautogui.write(text)
            pyautogui.click(113, 256)
            time.sleep(1)

def thiswaseasywithoutsubject(email, text, repeat):
    os.startfile("Outlook")
    time.sleep(10)
    for _ in range(repeat):
            pyautogui.click(115, 102)
            time.sleep(0.5)
            pyautogui.write(email)
            time.sleep(0.5)
            pyautogui.press("ENTER")
            time.sleep(1)
            pyautogui.click(128, 380)
            pyautogui.write(text)  
            pyautogui.click(113, 256)
            time.sleep(0.5)
            pyautogui.click(845, 501)
            time.sleep(1)

def start():
    repeat = int(repeat_entry.get())
    email = email_entry.get()
    subject = subject_entry.get()
    text = text_entry.get("1.0", END)
    thiswaseasy(email, subject, text, repeat)

# Create the main window
root = Tk()
root.title("Python Auto Email")

# Create input fields and labels
Label(root, text="Number of repeats:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
repeat_entry = Entry(root)
repeat_entry.grid(row=0, column=1, padx=5, pady=5)
Label(root, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
email_entry = Entry(root)
email_entry.grid(row=1, column=1, padx=5, pady=5)
Label(root, text="Subject (Optional):").grid(row=2, column=0, padx=5, pady=5, sticky=W)
subject_entry = Entry(root)
subject_entry.grid(row=2, column=1, padx=5, pady=5)
Label(root, text="Text:").grid(row=3, column=0, padx=5, pady=5, sticky=W)
text_entry = Text(root, height=5, width=30)
text_entry.grid(row=3, column=1, padx=5, pady=5)

# Create start button
start_button = Button(root, text="Start", command=start)
start_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()