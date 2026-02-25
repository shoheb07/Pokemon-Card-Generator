import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Create main window
root = tk.Tk()
root.title("Pokemon Card Generator")
root.geometry("400x500")

selected_image_path = None

def select_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    messagebox.showinfo("Image Selected", "Image selected successfully!")

def generate_card():
    if not selected_image_path:
        messagebox.showerror("Error", "Please select a Pokemon image!")
        return

    name = name_entry.get()
    hp = hp_entry.get()
    ptype = type_entry.get()
    attack = attack_entry.get()
    damage = damage_entry.get()

    # Create blank card
    card = Image.new("RGB", (400, 600), "white")
    draw = ImageDraw.Draw(card)

    try:
        font_title = ImageFont.truetype("arial.ttf", 28)
        font_text = ImageFont.truetype("arial.ttf", 20)
    except:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()

    # Draw border
    draw.rectangle([10, 10, 390, 590], outline="black", width=5)

    # Draw name and HP
    draw.text((20, 20), f"{name}", fill="black", font=font_title)
    draw.text((300, 20), f"HP {hp}", fill="red", font=font_text)

    # Add Pokemon image
    img = Image.open(selected_image_path)
    img = img.resize((300, 200))
    card.paste(img, (50, 80))

    # Type
    draw.text((20, 300), f"Type: {ptype}", fill="blue", font=font_text)

    # Attack
    draw.text((20, 350), f"{attack}", fill="black", font=font_text)
    draw.text((300, 350), f"{damage}", fill="black", font=font_text)

    # Save file
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        card.save(save_path)
        messagebox.showinfo("Success", "Pokemon card saved successfully!")

# UI Labels and Entries
tk.Label(root, text="Pokemon Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="HP").pack()
hp_entry = tk.Entry(root)
hp_entry.pack()

tk.Label(root, text="Type").pack()
type_entry = tk.Entry(root)
type_entry.pack()

tk.Label(root, text="Attack Name").pack()
attack_entry = tk.Entry(root)
attack_entry.pack()

tk.Label(root, text="Damage").pack()
damage_entry = tk.Entry(root)
damage_entry.pack()

tk.Button(root, text="Select Image", command=select_image).pack(pady=10)
tk.Button(root, text="Generate Card", command=generate_card).pack(pady=10)

root.mainloop()
