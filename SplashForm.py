from customtkinter import *
from PIL import Image
import time

def load_data():
    for i in range(101):
        progress.set(i/100)
        label_var.set(f"Loading... {i}%")
        root.update_idletasks()
        time.sleep(0.05)  # Simulating a background task
    root.destroy()
    import LoginPage

root = CTk()
root.title("Splash Screen")
root.geometry("400x250+480+230")
# Remove/ hide the action bar or close/ minimize icons
root.overrideredirect(True)

# Background Image
image = CTkImage(Image.open("SplashImage.jpg"), size=(400, 250))
ImageLabel = CTkLabel(root, image=image, text='')
ImageLabel.place(x=0, y=0)

splash_Company_label = CTkLabel(root, text="Phil Inc.", bg_color='#333333', font=("Helvetica", 18), text_color='#E9C057')
splash_Company_label.place(x=50, y=30)
splash_label = CTkLabel(root, text="Hotel Billing System", font=("Helvetica", 30, 'bold'), text_color='#E9C057', bg_color='#333333')
splash_label.place(x=57, y=110)

label_var = StringVar()
progress_label = CTkLabel(root, textvariable=label_var, font=("Helvetica", 12), text_color='#E9C057', bg_color='#1B1B1B')
progress_label.place(x=150, y=190)

progress = CTkProgressBar(root, width=300, height=2, fg_color='#E9C057')
progress.place(x=50, y=220)
progress.set(0)  # Initialize the progress bar

# Start the loading process in the background
root.after(100, load_data)
root.mainloop()

