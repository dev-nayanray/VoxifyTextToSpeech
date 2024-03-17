import tkinter as tk
from tkinter import messagebox, filedialog
import pyttsx3

def speak():
    text = text_entry.get()
    if text.strip() == "":
        messagebox.showwarning("Warning", "Please enter some text.")
    else:
        lang = language_var.get()
        lang_code = language_codes[lang]
        voice_gender = voice_gender_var.get()
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('voice', voices[lang_code][voice_gender])
        engine.say(text)
        engine.runAndWait()
        download_button.config(state=tk.NORMAL)

def download_audio():
    text = text_entry.get()
    if text.strip() == "":
        messagebox.showwarning("Warning", "Please enter some text.")
    else:
        lang = language_var.get()
        lang_code = language_codes[lang]
        voice_gender = voice_gender_var.get()
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('voice', voices[lang_code][voice_gender])
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            engine.save_to_file(text, file_path)
            engine.runAndWait()
            messagebox.showinfo("Success", "Audio file saved successfully.")

# Define voice settings for English and Bangla languages
voices = {
    "en": {
        "male": r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_GeorgeM",
        "female": r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_HazelM"
    },
    "bn": {
        "male": r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_bnIN_ApurvaM",
        "female": r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_bnIN_MadhusreeM"
    }
}

def create_widgets(root):
    label = tk.Label(root, text="Enter text to convert to speech:")
    label.pack(pady=10)
    global text_entry
    text_entry = tk.Entry(root, width=50)
    text_entry.pack(pady=5)
    languages = ["English", "Bangla"]
    global language_var
    language_var = tk.StringVar(value="English")
    language_dropdown = tk.OptionMenu(root, language_var, *languages)
    language_dropdown.pack(pady=5)
    global voice_gender_var
    voice_gender_var = tk.StringVar(value="male")
    male_radio = tk.Radiobutton(root, text="Male", variable=voice_gender_var, value="male")
    female_radio = tk.Radiobutton(root, text="Female", variable=voice_gender_var, value="female")
    male_radio.pack()
    female_radio.pack()
    speak_button = tk.Button(root, text="Speak", command=speak)
    speak_button.pack(pady=5)
    global download_button
    download_button = tk.Button(root, text="Download Audio", command=download_audio, state=tk.DISABLED)
    download_button.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Text-to-Speech Converter")
    create_widgets(root)
    root.mainloop()
