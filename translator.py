import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Create a reverse mapping: full language names (title-cased) to language codes.
languages = {value.title(): key for key, value in LANGUAGES.items()}


def translate_text():
    text = text_input.get("1.0", tk.END).strip()
    selected_language = language_var.get()

    if not text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    try:
        translator = Translator()
        dest_language_code = languages.get(selected_language)
        if dest_language_code is None:
            messagebox.showerror("Error", "Selected language is not supported.")
            return

        translated = translator.translate(text, dest=dest_language_code)
        translated_text = translated.text
        pronunciation = translated.pronunciation

        output = f"{translated_text} ({pronunciation})" if pronunciation else translated_text

        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, output)
        text_output.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")


# Create the main window
root = tk.Tk()
root.title("🌍 Language Translator")
root.geometry("600x500")
root.configure(bg="#e3f2fd")  # Light blue background

# Styling variables
FONT_TITLE = ("Arial", 20, "bold")
FONT_LABEL = ("Arial", 12, "bold")
FONT_TEXT = ("Arial", 12)
BUTTON_STYLE = {"font": ("Arial", 12, "bold"), "background": "#2196F3", "fg": "white"}

# Title label
title_label = tk.Label(root, text="🌍 Language Translator", font=FONT_TITLE, bg="#e3f2fd", fg="#0d47a1")
title_label.pack(pady=10)

# Input frame
input_frame = tk.Frame(root, bg="#e3f2fd")
input_frame.pack(pady=10, padx=20, fill="x")

input_label = tk.Label(input_frame, text="Enter text:", font=FONT_LABEL, bg="#e3f2fd")
input_label.pack(anchor="w")

text_input = tk.Text(input_frame, height=5, width=60, font=FONT_TEXT, wrap="word", relief="solid", bd=2)
text_input.pack()

# Language selection frame
lang_frame = tk.Frame(root, bg="#e3f2fd")
lang_frame.pack(pady=5, padx=20, fill="x")

language_label = tk.Label(lang_frame, text="Select target language:", font=FONT_LABEL, bg="#e3f2fd")
language_label.pack(anchor="w")

language_var = tk.StringVar()
language_dropdown = ttk.Combobox(lang_frame, textvariable=language_var, values=list(languages.keys()), state="readonly",
                                 font=FONT_TEXT)
language_dropdown.pack(fill="x")
language_dropdown.set("Select Language")

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text, **BUTTON_STYLE, padx=10, pady=5)
translate_button.pack(pady=10)

# Output frame
output_frame = tk.Frame(root, bg="#e3f2fd")
output_frame.pack(pady=10, padx=20, fill="both", expand=True)

output_label = tk.Label(output_frame, text="Translated text:", font=FONT_LABEL, bg="#e3f2fd")
output_label.pack(anchor="w")

text_output = tk.Text(output_frame, height=5, width=60, font=FONT_TEXT, wrap="word", relief="solid", bd=2,
                      state=tk.DISABLED)
text_output.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(output_frame, command=text_output.yview)
scrollbar.pack(side="right", fill="y")
text_output.config(yscrollcommand=scrollbar.set)

# Run the GUI event loop
root.mainloop()
