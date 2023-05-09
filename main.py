#command to compile pyinstaller --noconfirm --onedir --windowed --add-data "<C:/Users/nancy/AppData/Local/Programs/Python/Python310/Lib/site-packages>/customtkinter;customtkinter/;customtkinter/"  "<C:/New Folder>"
#-add-data "C:/Users/<user_name>/AppData/Local/Programs/Python/Python310/Lib/site-packages/customtkinter;customtkinter/
import customtkinter
import random
import string
import pyperclip

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("350x500")

root.title("EZPass")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="My Passcodes", font=("Roboto", 24))
label.pack(pady=12, padx=10)

def getLength():
    global value
    length = customtkinter.CTkInputDialog(text="Length", title="EZPass")
    value = length.get_input()

def getPass():
    global fortext
    password = customtkinter.CTkInputDialog(text="What is the passcode for?", title="EZPass")
    fortext = password.get_input()

def copy():
    pyperclip.copy(code)
    label3 = customtkinter.CTkLabel(master=frame, text="Copied!")
    label3.pack()

def finish():
    generateCode(value)

button = customtkinter.CTkButton(master=frame, text="Set Length", command=getLength)
button2 = customtkinter.CTkButton(master=frame, text="What is the password is for?", command=getPass)
button3 = customtkinter.CTkButton(master=frame, text="Generate Code", command=finish)
button4 = customtkinter.CTkButton(master=frame, text="Copy Code", command=copy)
button.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)
button4.pack(pady=5)

useSpecialCharacters = True
useUpperCase = True
useLowerCase = True
usePunc = True
useNums = True

def generateCode(_length):
    global code
    # generate code
    code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation, k=int(_length)))
    print(code)
    label2 = customtkinter.CTkLabel(master=frame, text="Code: " + code)
    label2.pack(pady=5)
    writeToFile(code)

def writeToFile(text):
    with open("passcodes.txt", "a") as text_file:
       text_file.write("for: " + fortext + " " + "pass = " + text + ",\n")

root.mainloop()