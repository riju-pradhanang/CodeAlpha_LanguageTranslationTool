import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES


# Function to translate text
def translate_text():
    text = text_input.get("1.0", tk.END).strip()  # Get text from input box
    dest_language = language_var.get()  # Get selected target language

    if not text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    try:
        translator = Translator()
        translated = translator.translate(text, dest=dest_language)
        text_output.delete("1.0", tk.END)  # Clear previous text
        text_output.insert(tk.END, translated.text)  # Display translated text
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")


# Initialize Tkinter window
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x400")
root.resizable(False, False)

# Title label
tk.Label(root, text="Simple Translator", font=("Arial", 16, "bold")).pack(pady=10)

# Input text area
tk.Label(root, text="Enter text:", font=("Arial", 12)).pack()
text_input = tk.Text(root, height=5, width=50)
text_input.pack(pady=5)

# Language selection dropdown
tk.Label(root, text="Select target language:", font=("Arial", 12)).pack()
language_var = tk.StringVar()
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=list(LANGUAGES.keys()), state="readonly")
language_dropdown.pack(pady=5)
language_dropdown.set("es")  # Default to Spanish

# Translate button
translate_button = tk.Button(root, text="Translate", font=("Arial", 12, "bold"), command=translate_text, bg="#4CAF50",
                             fg="white")
translate_button.pack(pady=10)

# Output text area
tk.Label(root, text="Translated text:", font=("Arial", 12)).pack()
text_output = tk.Text(root, height=5, width=50)
text_output.pack(pady=5)

# Run the GUI
root.mainloop()
