import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Create a reverse mapping: full language names (title-cased) to language codes.
languages = {value.title(): key for key, value in LANGUAGES.items()}

def translate_text():
    """
    Retrieve text from the input box, determine the target language code from
    the selected full language name, translate the text using googletrans,
    and display the translated text along with its pronunciation in the output box.
    """
    text = text_input.get("1.0", tk.END).strip()  # Get text from input area
    selected_language = language_var.get()  # Get the selected language name

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

        text_output.config(state=tk.NORMAL)  # Enable editing to update text
        text_output.delete("1.0", tk.END)  # Clear previous output
        text_output.insert(tk.END, output)  # Insert translated text
        text_output.config(state=tk.DISABLED)  # Disable editing again
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

# Create the main window
root = tk.Tk()
root.title("🌍 Language Translator")
root.geometry("550x500")
root.configure(bg="#f0f0f0")  # Light grey background
root.resizable(False, False)

# Styling variables
FONT_TITLE = ("Arial", 18, "bold")
FONT_LABEL = ("Arial", 12, "bold")
FONT_TEXT = ("Arial", 12)
BUTTON_STYLE = {"font": ("Arial", 12, "bold"), "bg": "#4CAF50", "fg": "white", "activebackground": "#45a049", "cursor": "hand2"}

# Title label
title_label = tk.Label(root, text="🌍 Language Translator", font=FONT_TITLE, bg="#f0f0f0")
title_label.pack(pady=15)

# Input text label and text area
input_label = tk.Label(root, text="Enter text:", font=FONT_LABEL, bg="#f0f0f0")
input_label.pack(anchor="w", padx=20)
text_input = tk.Text(root, height=5, width=60, font=FONT_TEXT, wrap="word", relief="solid", bd=1)
text_input.pack(pady=5, padx=20)

# Language selection label and dropdown menu
language_label = tk.Label(root, text="Select target language:", font=FONT_LABEL, bg="#f0f0f0")
language_label.pack(anchor="w", padx=20)
language_var = tk.StringVar()
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=list(languages.keys()), state="readonly", font=FONT_TEXT)
language_dropdown.pack(pady=5, padx=20)
language_dropdown.set("Spanish")  # Default language

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text, **BUTTON_STYLE)
translate_button.pack(pady=15)

# Output text label
output_label = tk.Label(root, text="Translated text:", font=FONT_LABEL, bg="#f0f0f0")
output_label.pack(anchor="w", padx=20)

# Output text area with scrollbar
output_frame = tk.Frame(root)
output_frame.pack(pady=5, padx=20, fill="both", expand=True)

text_output = tk.Text(output_frame, height=5, width=60, font=FONT_TEXT, wrap="word", relief="solid", bd=1, state=tk.DISABLED)
text_output.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(output_frame, command=text_output.yview)
scrollbar.pack(side="right", fill="y")

text_output.config(yscrollcommand=scrollbar.set)

# Run the GUI event loop
root.mainloop()
