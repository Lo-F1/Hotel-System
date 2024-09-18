from customtkinter import *
from PIL import Image
from tkinter import messagebox
# Functionality
def Login():
    if UserNameEntry.get()=="" or PassWordEntry=="":
        messagebox.showerror("Failed", "Username and or Password are not provided")
    elif UserNameEntry.get()=="Phil" and PassWordEntry.get()=="1234":
        messagebox.showinfo("Welcome", "Login Successful!")
        root.destroy()
        import Main
    else:
        messagebox.showerror("Error", "Invalid credentials")
# GUI
root = CTk()
root.geometry('930x478+220+150')
root.resizable(False, False)
root.title('Login Page')

image = CTkImage(Image.open("HotelLogin.jpg"), size=(930, 478))
ImageLabel = CTkLabel(root, image=image, text='')
ImageLabel.place(x=0, y=0)

HeadingLabel = CTkLabel(root, text='Hotel Management System', font=('Arial', 20, 'bold'), bg_color="#FEF481", text_color='#4B493F')
HeadingLabel.place(x=80, y=100)

UserNameEntry = CTkEntry(root, placeholder_text="Enter Your Username", width=180)
UserNameEntry.place(x=115, y=170)
PassWordEntry = CTkEntry(root, placeholder_text="Enter Your Password", width=180, show="*")
PassWordEntry.place(x=115, y=200)

LoginButton = CTkButton(root, text="    Login   ", cursor="hand2", command=Login)
LoginButton.place(x=135, y=270)

root.mainloop()