import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from app.ai.chat_ai import chat_response
from app.ai.code_ai import generate_code
from app.ai.image_gen import generate_image
from app.ai.deblur_ai import deblur_image

def start_gui():
    root = tk.Tk()
    root.title("David AI 2B – Powered by Nexuzy Tech")
    root.geometry("800x600")
    root.configure(bg="#1e1e1e")

    # Header
    tk.Label(root, text="🧠 David AI 2B", font=("Arial", 20, "bold"),
             fg="orange", bg="#1e1e1e").pack(pady=10)

    # Mode Selector
    mode_var = tk.StringVar(value="chat")
    modes = [("Chat", "chat"), ("Code", "code"), ("Image", "image"), ("Deblur", "deblur")]

    frame_mode = tk.Frame(root, bg="#1e1e1e")
    frame_mode.pack()

    for text, mode in modes:
        tk.Radiobutton(frame_mode, text=text, variable=mode_var, value=mode,
                       bg="#1e1e1e", fg="white", selectcolor="#444").pack(side="left", padx=10)

    # Input Box
    input_box = tk.Text(root, height=8, font=("Arial", 12), wrap=tk.WORD, bg="#2e2e2e", fg="white")
    input_box.pack(padx=20, pady=10, fill="x")

    # Output Area
    output_label = tk.Label(root, text="Output will appear here.", wraplength=750,
                            justify="left", bg="#1e1e1e", fg="#90ee90", font=("Consolas", 12))
    output_label.pack(pady=10)

    # Image display (for image tasks)
    img_label = tk.Label(root, bg="#1e1e1e")
    img_label.pack()

    def run_ai():
        task = mode_var.get()
        input_text = input_box.get("1.0", tk.END).strip()

        if not input_text and task != "deblur":
            messagebox.showerror("Input Error", "Please enter a prompt.")
            return

        if task == "chat":
            result = chat_response(input_text)
            output_label.config(text=result)

        elif task == "code":
            result = generate_code(input_text)
            output_label.config(text=result)

        elif task == "image":
            output_path = generate_image(input_text)
            img = Image.open(output_path).resize((400, 400))
            img = ImageTk.PhotoImage(img)
            img_label.config(image=img)
            img_label.image = img
            output_label.config(text=f"🖼️ Image saved to: {output_path}")

        elif task == "deblur":
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
            if file_path:
                output_path = deblur_image(file_path)
                img = Image.open(output_path).resize((400, 400))
                img = ImageTk.PhotoImage(img)
                img_label.config(image=img)
                img_label.image = img
                output_label.config(text=f"🔧 Deblurred image saved to: {output_path}")
            else:
                output_label.config(text="No file selected.")

    # Run Button
    tk.Button(root, text="Run", command=run_ai, font=("Arial", 12, "bold"),
              bg="orange", fg="black", padx=20).pack(pady=10)

    root.mainloop()
