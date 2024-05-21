import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog
import customtkinter
import random
import string
import os
import shutil
import PyPDF2
import docx
from implementation import *
from implementation_neighbour import *
import time


# creating splash screen
def create_splash_screen(splash_screen):
    # defining dimensions
    width_of_window = 427
    height_of_window = 250
    screen_width = splash_screen.winfo_screenwidth()
    screen_height = splash_screen.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    splash_screen.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
    
    splash_screen.overrideredirect(1) #for hiding titlebar

    # creating a frame containing the animation and title of the program
    Frame(splash_screen, width=427, height=250, bg='#040405').place(x=0,y=0)
    label1=Label(splash_screen, text='ENCRYPTIFY', fg='white', bg='#3047ff') #decorate it 
    label1.configure(font=("Game Of Squids", 24, "bold"))  
    label1.place(x=100,y=90)

    label2=Label(splash_screen, text='Loading...', fg='white', bg='#040405') #decorate it 
    label2.configure(font=("Calibri", 11))
    label2.place(x=10,y=215)

    lock_icon = Image.open('images\\lock.png')
    width = 80
    height = 60
    resized_image = lock_icon.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    side_image_label = Label(splash_screen, image=photo, bg='#040405')
    side_image_label.image = photo
    side_image_label.place(x=345, y=190)

    #making animation

    image_a=ImageTk.PhotoImage(Image.open('images\c2.png'))
    image_b=ImageTk.PhotoImage(Image.open('images\c1.png'))

    #  we iterate five times to perform the animation sequence. 
    # For each iteration, one label will show image_a while the others show image_b, giving the illusion of movement. 
    for i in range(4): 
        l1=Label(splash_screen, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        splash_screen.update_idletasks()      # to ensure that any pending GUI events are processed and the window is updated with the new label images.
        time.sleep(0.3)     # a short delay of 0.3 seconds

        l1=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(splash_screen, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        splash_screen.update_idletasks()      # to ensure that any pending GUI events are processed and the window is updated with the new label images.
        time.sleep(0.3)     # a short delay of 0.3 seconds

        l1=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(splash_screen, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        splash_screen.update_idletasks()      # to ensure that any pending GUI events are processed and the window is updated with the new label images.
        time.sleep(0.3)     # a short delay of 0.3 seconds

        l1=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3=Label(splash_screen, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4=Label(splash_screen, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
        splash_screen.update_idletasks()      # to ensure that any pending GUI events are processed and the window is updated with the new label images.
        time.sleep(0.3)     # a short delay of 0.3 seconds


# creating tkinter screen
def main(window):
    window.title("Cryptographers")
    window.geometry("1166x718")         # defining size
    window.resizable(0, 0)              # ensuring that the screen is resizeable
    window.state("zoomed")
    front_page(window)                  # calling function that adds frames to the main window
    window.mainloop()                   # called to start the event loop


# creating the front page of the application 
def front_page(window):
    global front_frame
    # adding the background image
    bg_image = Image.open('images\\bg2.jpg')
    label_width = 1500
    label_height = 750
    bg_image = bg_image.resize((label_width, label_height))
    photo = ImageTk.PhotoImage(bg_image)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')
    
    #=============================== creating the front page and its widgets========================
    # placing the frame
    front_frame = Frame(window, bg='#040405', width=950, height=600)
    front_frame.place(x=200, y=70)

    # adding the welcome text
    heading_txt = "HeLLo EncrYPterS!"
    heading = Label(front_frame, text = heading_txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
    heading.place(x=80, y=30, width=300, height=30)

    # adding image on the side of the page
    side_image = Image.open('images\\vector.png')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(front_frame, image=photo, bg='#040405')
    side_image_label.image = photo
    side_image_label.place(x=5, y=100)

    # adding user icon
    user_image = Image.open('images\\hyy.png')
    photo = ImageTk.PhotoImage(user_image)
    user_image_label = Label(front_frame, image=photo, bg='#040405')
    user_image_label.image = photo
    user_image_label.place(x=620, y=130)

      
    # asking for username
    name_label = Label(front_frame, text="Welcome", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
    name_label.place(x=650, y=240)

    username_label = Label(front_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
    username_label.place(x=550, y=300)

    # taking input from the user using Entry function
    username_entry = Entry(front_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
    username_entry.place(x=580, y=335, width=270)

    username_line = Canvas(front_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    username_line.place(x=550, y=359)
    
    # adding username icon
    username_icon = Image.open('images\\username_icon.png')
    photo = ImageTk.PhotoImage(username_icon)
    username_icon_label = Label(front_frame, image=photo, bg='black')
    username_icon_label.image = photo
    username_icon_label.place(x=550, y=332)

    # using a combobox to allow user to select an encryption method
    combo_box= customtkinter.CTkComboBox(front_frame, values=["Encrypt Data", "Encrypt Text File"],
    height=30, width=250, font=("Consolas", 16),
	dropdown_font=("Consolas", 15),
	corner_radius=50,
	border_width=2, border_color="white", button_color="#3047ff", button_hover_color = "#3047ff",
	dropdown_hover_color = "#3047ff", dropdown_fg_color = "white", dropdown_text_color="black",
	text_color="black",
	hover=True,
	state="readonly")

    # Set the default value
    combo_box.set("Select Feature")
    combo_box.place(x=580, y=400)

    # continue button to change to another page
    front_button = Image.open('images\\btn1.png')
    photo = ImageTk.PhotoImage(front_button)

    continue_btn = Button(front_frame, text='Continue', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', 
                            command=lambda : feature_selection(window, front_frame, username_entry, combo_box))
    continue_btn.place(x=580, y=500)

# function that handles cases where user doesnot give an input. When we do get a selection, it calls the relavant create frame function.
def feature_selection(window, frame, data_entry, combo_box):
    selected_option = combo_box.get()
    if data_entry.get() == "":
        error_msg = Label(frame, text= "Please enter valid username.",bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 10, "bold"))
        error_msg.place(x=550, y=365)
    elif selected_option == "Select Feature":
        error_msg = Label(frame, text= "Select A valid feature.",bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 10, "bold"))
        error_msg.place(x=580, y=440)
    elif selected_option == "Encrypt Data":
        # Show text encryption options
        info_page(window)
    elif selected_option == "Encrypt Text File":
        # Show filename encryption options
        file_page(window)


# creating a page to handle encrypt and decrypt data feature 
def info_page(window):
    global info_frame
    # adding the background image
    bg_image = Image.open('images\\bg2.jpg')
    label_width = 1500
    label_height = 750
    bg_image = bg_image.resize((label_width, label_height))
    photo = ImageTk.PhotoImage(bg_image)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')
    
    #====================== creating the info page and its widgets ==========================
    # placing the frame
    info_frame = Frame(window, bg='#040405', width=950, height=600)
    info_frame.place(x=170, y=70)

    # adding the heading text
    heading_txt = f"Ready To Encrypt!"
    heading = Label(info_frame, text = heading_txt, font=('yu gothic ui', 25, "bold"), bg="#040405", fg='white', bd=5, relief=FLAT)
    heading.place(x=350, y=30, width=300, height=50 )

    # adding the text box to take input of the text to be encrypted from the user
    data_label = Label(info_frame, text="Enter Plain Text", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
    data_label.place(x=110, y=150)

    data_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69", font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
    data_entry.place(x=130, y=180, width=270)

    data_line = Canvas(info_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    data_line.place(x=110, y=210)

    
    #hide the text that needs to be encrypted
    show_image = ImageTk.PhotoImage(file='images\\show.png')
    hide_image = ImageTk.PhotoImage(file='images\\hide.png')

    hide_button = Button(info_frame, image=hide_image, command=lambda:hide(info_frame, hide_image, show_image, data_entry), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
    hide_button.place(x=390, y=180)


    # using a combobox to allow user to select an encryption method
    combo_box= customtkinter.CTkComboBox(info_frame, values=["Character Shuffling", "Height Encryption", "Neighbour Encryption", "Mirror Encryption", "Node Encryption"],
    height=35, width=285, font=("Consolas", 14),
	dropdown_font=("Consolas", 15),
	corner_radius=50,
	border_width=2, border_color="white", button_color="#3047ff", button_hover_color = "black",
	dropdown_hover_color = "#3047ff", dropdown_fg_color = "white", dropdown_text_color="black",
	text_color="black",
	hover=True,
	state="readonly")

    # Set the default value
    combo_box.set("Choose Encryption Method")
    combo_box.place(x=120, y=250)

    # adding buttons
    continue_btn = Button(info_frame, text='Encrypt', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', 
                            command=lambda : valid_data(window, info_frame, combo_box, data_entry))
    continue_btn.place(x=130, y=460)

    back_button = Button(info_frame, text="Go Back", font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: reload_front_page(front_frame))
    back_button.place(x=70, y =535)    

    # adding image on the side of the page
    side_image = Image.open('images\\boy.jpg')
    width = 380
    height = 400
    resized_image = side_image.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    side_image_label = Label(info_frame, image=photo, bg='#040405')
    side_image_label.image = photo
    side_image_label.place(x=500, y=130)


# creating a page to handle encrypt and decrypt text file feature
def file_page(window):
    global file_frame
    # adding the background image
    bg_image = Image.open('images\\bg2.jpg')
    label_width = 1500
    label_height = 750
    bg_image = bg_image.resize((label_width, label_height))
    photo = ImageTk.PhotoImage(bg_image)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')
    
    #====================== creating the file page and its widgets ==========================

    # placing the frame
    file_frame = Frame(window, bg='#040405', width=950, height=600)
    file_frame.place(x=170, y=70)

    # adding the heading text
    heading_txt = f"Ready To Encrypt!"
    heading = Label(file_frame, text = heading_txt, font=('yu gothic ui', 25, "bold"), bg="#040405", fg='white', bd=5, relief=FLAT)
    heading.place(x=350, y=30, width=300, height=50 )


    # adding buttons
    insert_file_button = Button(file_frame, text='Insert File', font=("yu gothic ui", 13, "bold"), width=15, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', 
                            command=lambda : insert_file(window, avl_tree))

    insert_file_button.place(x=155, y=150)


    back_button = Button(file_frame, text="Go Back", font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: reload_front_page(front_frame))
    back_button.place(x=75, y =520)

    # adding image on the side of the page
    side_image = Image.open('images\\boy.jpg')
    width = 380
    height = 400
    resized_image = side_image.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    side_image_label = Label(file_frame, image=photo, bg='#040405')
    side_image_label.image = photo
    side_image_label.place(x=500, y=130)

    # adding image on the side of the page
    file_image = Image.open('images\\file.png')
    width = 200
    height = 180
    resized_image = file_image.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    file_image_label = Label(file_frame, image=photo, bg='#040405')
    file_image_label.image = photo
    file_image_label.place(x=130, y=200)


# creating a page to show the output of the encryption of data
def output_page(window, option, lst, txt):
    global output_frame, info_frame

    # =============creating the page which shows the output of encryption ==================
    # adding the background image
    bg_image = Image.open('images\\bg2.jpg')
    label_width = 1500
    label_height = 750
    bg_image = bg_image.resize((label_width, label_height))
    photo = ImageTk.PhotoImage(bg_image)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')

    # placing the frame
    output_frame = Frame(window, bg='#040405', width=950, height=600)
    output_frame.place(x=170, y=70)

    # adding the heading text
    heading_txt = "Ready To Decrypt!"
    heading = Label(output_frame, text = heading_txt, font=('yu gothic ui', 25, "bold"), bg="#040405", fg='white', bd=5, relief=FLAT)
    heading.place(x=330, y=30, width=300, height=50)  
    
    # adding the label for the text box.
    data_label = Label(output_frame,wraplength=500, text=' ENCRYPTED TEXT', bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 20, "bold"))
    data_label.place(x=340, y=150)

    # creating custom text box to display the output of encryption
    result_textbox = customtkinter.CTkTextbox(output_frame, width=320, height=130, corner_radius=1,
	border_width=10, border_color="#003660", border_spacing=10, fg_color="silver",
	text_color="black", font=("Helvetica", 20), wrap="word")

    result_textbox.place(x=320, y=200)

    # inserting cipher text to text box
    result_textbox.insert(tk.END, txt, "center")

    # ensuring that data cannot be edited by the user.
    result_textbox.configure(state="disabled")
    
    # adding buttons
    # depending on the encryption method calling required decryption methods.
    if option == 1:
        decrypt_button = Button(output_frame, text="Decrypt", font=("yu gothic ui", 13, "bold"), width=15, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: character_shuffling_decryption(output_frame, avl_tree, lst, result_textbox))
    elif option == 2:
        decrypt_button = Button(output_frame, text="Decrypt", font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: height_decryption(output_frame, avl_tree, lst, result_textbox))
    elif option == 3:
        decrypt_button = Button(output_frame, text="Decrypt", font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: neighbour_decryption(output_frame, lst, result_textbox))
    elif option == 4 or option == 5:
        decrypt_button = Button(output_frame, text="Decrypt", font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: filename_decryption(output_frame, avl_tree_2, lst, result_textbox))
    
    decrypt_button.place(x=240, y=360)

    back_button = Button(output_frame, text="Go Back", font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: reload_info_page(info_frame))
    
    back_button.place(x=600, y =360, anchor=tk.NW)

    encrypt_btn = Button(output_frame, text='Encrypt Again', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', 
                            command=lambda:display_text(output_frame, txt, result_textbox))
    encrypt_btn.place(x=350, y=460)

    exit_button = Button(output_frame, text="Exit", font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: final_page(window))

    exit_button.place(x=800, y= 555)


# creating a page to show the output of the encryption of text file
def output_page_file(window, lst, txt):
    global output_frame_file, file_frame
    # =============creating the page which shows the output of encryption ==================

    # adding the background image
    bg_image = Image.open('images\\bg2.jpg')
    label_width = 1500
    label_height = 750
    bg_image = bg_image.resize((label_width, label_height))
    photo = ImageTk.PhotoImage(bg_image)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')

    # placing the frame
    output_frame_file = Frame(window, bg='#040405', width=950, height=600)
    output_frame_file.place(x=170, y=70)

    # adding the heading text
    heading_txt = "Ready To Decrypt!"
    heading = Label(output_frame_file, text = heading_txt, font=('yu gothic ui', 25, "bold"), bg="#040405", fg='white', bd=5, relief=FLAT)
    heading.place(x=330, y=30, width=300, height=50)  
    
    # adding the label for the text box.
    data_label = Label(output_frame_file,wraplength=500, text=' ENCRYPTED TEXT', bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 20, "bold"))
    data_label.place(x=340, y=150)

    # creating custom text box to display the output of encryption
    result_textbox = customtkinter.CTkTextbox(output_frame_file, width=320, height=130, corner_radius=1,
	border_width=10, border_color="#003660", border_spacing=10, fg_color="silver",
	text_color="black", font=("Helvetica", 20), wrap="word")

    result_textbox.place(x=320, y=200)

    # inserting cipher text to text box
    result_textbox.insert(tk.END, txt, "center")

    # ensuring that data cannot be edited by the user.
    result_textbox.configure(state="disabled")
    
    # adding buttons
    # calling required decryption methods.
    decrypt_button = Button(output_frame_file, text="Decrypt", font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: filename_decryption(output_frame_file, avl_tree, lst, result_textbox))
    decrypt_button.place(x=240, y=360)

    back_button = Button(output_frame_file, text="Go Back", font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: reload_file_page(file_frame))
    
    decrypt_button.place(x=240, y=360)
    back_button.place(x=600, y =360, anchor=tk.NW)

    encrypt_btn = Button(output_frame_file, text='Encrypt Again', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', 
                            command=lambda:display_text(output_frame, txt, result_textbox))
    encrypt_btn.place(x=350, y=460)
    
    save_button = Button(output_frame_file, text='Save File', font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=lambda : save_file(txt))

    exit_button = Button(output_frame_file, text="Exit", font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                        bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command= lambda: final_page(window))
    
    save_button.place(x=650, y=550) 
    exit_button.place(x=800, y= 550, anchor=tk.NW)

# thank you page
def final_page(window):
    global final_frame
    # adding the background image
    bg_image = Image.open('images\\bg2.jpg')
    label_width = 1500
    label_height = 750
    bg_image = bg_image.resize((label_width, label_height))
    photo = ImageTk.PhotoImage(bg_image)
    bg_panel = Label(window, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')

    # placing the frame
    final_frame = Frame(window, bg='#040405', width=950, height=600)
    final_frame.place(x=170, y=70)
    
    # adding the text
    heading_txt = "Be Back Soon Encrypters!"
    heading = Label(final_frame, text = heading_txt, font=('Game of Squids', 25, "bold"), bg="#040405", fg='white', bd=5, relief=FLAT)
    heading.place(x=290, y=280)

    # closing the tkinter window after 1.5 seconds has elapsed
    window.after(1500, window.destroy)


# destroying the info frame and creating the page again after go back button is pressed.
def reload_info_page(frame):
    frame.grid_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    info_page(window)

# destroying the file frame and creating the page again after go back button is pressed.
def reload_file_page(frame):
    frame.grid_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    file_page(window)

# destroying the front frame and creating the page again after go back button is pressed.
def reload_front_page(frame):
    frame.grid_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    front_page(window)

# function that encrypts the data again after user decrypts it.
def display_text(frame, txt, textbox):
    textbox.configure(state="normal")
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, txt, "center")
    textbox.configure(state="disabled")

    data_label = Label(frame,wraplength=500, text=' ENCRYPTED TEXT', bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 20, "bold"))
    data_label.place(x=340, y=150)


# button to show the encrypted text if the user wants
def show(frame, hide_image, show_image, data_entry):
    hide_button = Button(frame, image=hide_image, command=lambda:hide(frame, hide_image, show_image, data_entry), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
    hide_button.place(x=390, y=180)
    data_entry.config(show='*')


# button to hide the encrypted text if the user wants
def hide(frame, hide_image, show_image, data_entry):
    show_button = Button(frame, image=show_image, command= lambda: show(info_frame, hide_image, show_image, data_entry), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=390, y=180)
    data_entry.config(show='')

    
# function that ensures program only proceeds if valid data has been entered, otherwise print error messages.
def valid_data(window, frame, combo_box, data_entry):
    if data_entry.get() == "":
        error_msg = Label(frame, text= "Please enter valid text.",bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 10, "bold"))
        error_msg.place(x=110, y=220)
    elif combo_box.get() == "Select Feature":
        error_msg = Label(frame, text= "Choose a valid feature.",bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 10, "bold"))
        error_msg.place(x=110, y=380)
    elif combo_box.get() == "Choose Encryption Method":
        error_msg = Label(frame, text= "Select valid encryption method.",bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 10, "bold"))
        error_msg.place(x=110, y=290)
    elif combo_box.get() == "Choose file type":
        error_msg = Label(frame, text= "Select valid file type.",bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 10, "bold"))
        error_msg.place(x=110, y=270)
    else:
        on_Select_combobox(window, combo_box, data_entry)


# dealing with the choice selected
def on_Select_combobox(window, combo_box, data_entry):
    option = 0
    # storing user's choice in a variable that can later be passed as a parameter.
    selected_item = combo_box.get()
    if selected_item == "Character Shuffling":
        option = 1
    elif selected_item == "Height Encryption":
        option = 2
    elif selected_item == "Neighbour Encryption":
        option = 3
    elif selected_item == "Mirror Encryption":
        option = 4
    elif selected_item == "Node Encryption":
        option = 5

    # storing the data that needs to be encrypted in variable named plain_text
    plain_text = data_entry.get()
    encryption_methods(window, plain_text, option)


# calling different methods based on user choice stored in variable option
def encryption_methods(window, plain_text, option):
    if option == 1:
        character_shuffling_encryption(window, avl_tree, plain_text)
    elif option == 2:
        height_encryption(window, avl_tree, plain_text)
    elif option == 3:
        neighbour_encryption(window, avl_tree_2, plain_text)
    elif option == 4:
        mirror_encryption(window, avl_tree, plain_text)
    elif option == 5:
        node_encryption(window, avl_tree, plain_text)

# function that allows user to insert a text file from computer storage, so that the data in it can be encrypted.
def insert_file(window, avl_tree):
    # Open file dialog to select a text file
    file_path = filedialog.askopenfilename(title="Select Text File", filetypes=(("Text files", "*.txt;*.docx;*.csv;*.html;*.pdf"), ("All files", "*.*")))
    
    if file_path:
        # Get the filename from the file path
        filename = os.path.basename(file_path)
                                    
        with open(file_path, 'r', encoding='utf-8') as file:
            if filename.endswith('.pdf'):
                text = extract_text_from_pdf(file_path)
            elif filename.endswith('.docx'):
                text = extract_text_from_doc(file_path)
            else:
                text = file.read()

    # Save a copy of the text file in the destination folder
        destination_folder = "text_files"
        shutil.copy(file_path, os.path.join(destination_folder, filename))
    
    # adding buttons
    encrypt_btn = Button(file_frame, text='Encrypt', font=("yu gothic ui", 13, "bold"), width=12, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=lambda : encrypt_file(text))
    encrypt_btn.place(x=310, y=520, anchor=tk.NW)

    view_btn = Button(file_frame, text='View File', font=("yu gothic ui", 13, "bold"), width=15, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=lambda : view_file(text))
    view_btn.place(x=155, y=425)

# if text file type is pdf
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# if text file type is docx
def extract_text_from_doc(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


# function that allows user to view the selected file
def view_file(text):
    # Create a new window to display the selected text file
    new_window = tk.Toplevel()
    new_window.title("Selected File")
        
    # Create a Text widget to display the content of the text file
    text_widget = tk.Text(new_window, wrap="word", undo=True,width=80, height=18, font=("Raleway", 16), bg="black", fg="white")
    text_widget.tag_configure("center", justify='center')
    text_widget.config(state=tk.NORMAL)
    text_widget.pack(expand ="true", fill="both")
    text_widget.insert(tk.END, text)
    text_widget.config(state=tk.DISABLED)
        
# function that calls encryption function on the selected file
def encrypt_file(text):
    global output_frame_file
    text_encryption(window, avl_tree, text)

# function called when user wants to save the decrypted file
def save_file(encrypted_text):
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if save_path:
        with open(save_path, 'w') as encrypted_file:
            encrypted_file.write(encrypted_text)


# ============================ first encryption method ================================
def character_shuffling_encryption(window, avl_tree, plain_text):

    # generating a random index that will become the root of the avl tree during insertion
    random_int = random.randint(0, len(plain_text)-1)
    root = plain_text[random_int]

    # insering the ascii value of root character as key and the character as value into the avl tree
    avl_tree = insert(avl_tree, random_int, ord(root))

    # adding remaining characters
    for x in range(len(plain_text)):
        if x != random_int:
            avl_tree = insert(avl_tree, x, ord(plain_text[x]))

    # applying post_order traversal on the generated tree.
    post_order_lst = postorder_traversal(avl_tree)

    cipher_text = ""
    # searching for each element, and storing its path in a string.
    for y in post_order_lst:
        val, path = search(avl_tree, y[0])
        string = "".join(path)
        cipher_text += string       # our final encrypted string

    output_page(window, option=1, lst=post_order_lst, txt= cipher_text)


def character_shuffling_decryption(output_frame, avl_tree, post_order_lst, textbox):
    # reconstructing the key and getting original insertion order back
    insertion_lst = get_insertion_order_from_postorder(avl_tree, post_order_lst)
    plain_text = ""
    for x in range(len(insertion_lst)):
        plain_text += chr(insertion_lst[x][1])

    textbox.configure(state="normal")
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, plain_text, "center")
    textbox.configure(state="disabled")

    data_label = Label(output_frame,wraplength=500, text=' DECRYPTED TEXT', bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 20, "bold"))
    data_label.place(x=340, y=150)


# ============================ second encryption method ================================

def height_encryption(window, avl_tree, plain_text):
    cipher_text = ""
    for char in plain_text:

        # insert the character in the avl tree
        avl_tree = insert(avl_tree, ord(char), char)

    # get the height of the tree
    height_value = height(avl_tree)

    for char in plain_text:
        # add height to each ascii value of a character in plain text
        if (ord(char) + height_value) <= 127:
            # convert back to a character and add to our decrypted text
            cipher_text += chr(ord(char) + height_value)
        else:
            # if not in the range of ascii values then add the character as it is
            cipher_text += chr(ord(char))

    output_page(window, option=2, lst=cipher_text, txt= cipher_text)
    

def height_decryption(output_frame, avl_tree, cipher_text, textbox):
    plain_text = ""
    for char in cipher_text:
        # insert the character into the avl tree
        avl_tree = insert(avl_tree, ord(char), char) 

    # etg the height of the tree
    height_value = height(avl_tree)
    
    for char in cipher_text:
        # subtract height from ascii value of the character in cipher text 
        plain_text += chr(ord(char) - height_value)
        

    textbox.configure(state="normal")
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, plain_text, "center")
    textbox.configure(state="disabled")

    data_label = Label(output_frame,wraplength=500, text=' DECRYPTED TEXT', bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 20, "bold"))
    data_label.place(x=340, y=150)

# ============================ third encryption method ================================
def neighbour_encryption(window, avl_tree_2, plain_text):
    cipher_lst = []
    # Insert each character of the plaintext into the AVL tree
    for x in plain_text:
        avl_tree_2 = insert_2(avl_tree_2, ord(x), x)

    # depending on whether each character has a successor or predecessor, add 1 or 0 in place of the original character
    for y in plain_text:
        successor_node = successor_2(avl_tree_2, ord(y))
        predecessor_node = predecessor_2(avl_tree_2, ord(y))
        if successor_node:
            cipher_lst.append((1, y))
        elif predecessor_node:
            cipher_lst.append((0, y))
        else: # if there is any corner case that doesnt find a predesecor or sucessor for some reason
            cipher_lst.append((2, y))

    cipher_text = ""
    for a, b in cipher_lst:
        cipher_text += str(a)

    output_page(window, option=3, lst=cipher_lst, txt= cipher_text)


def neighbour_decryption(output_frame, lst, textbox):
    decrypted_message = []
    for key, value in lst:
        decrypted_message.append((ord(value), value))

    plain_text = ""
    for key, value in decrypted_message:
        plain_text += value

    textbox.configure(state="normal")
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, plain_text, "center")
    textbox.configure(state="disabled")

    data_label = Label(output_frame,wraplength=500, text=' DECRYPTED TEXT', bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 20, "bold"))
    data_label.place(x=340, y=150)
    

# ============================ fourth encryption method ================================
# function that generates a map that substitutes characters of original string with their respective mappings.
def generate_map():
    all_chars = list(string.printable)
    shuffled_chars = list(all_chars)
    random.shuffle(shuffled_chars)
    mapping = {}
    for original_char, encrypted_char in zip(all_chars, shuffled_chars):
        mapping[original_char] = encrypted_char
    return mapping

# creating a global encryption map
encryption_mapping = generate_map()

def mirror_encryption(window, avl_tree, plain_text):
    global encryption_mapping

    # applying a simple substitution cipher on the shuffled ascii values of the initial text
    mapped_text = ""
    for char in plain_text:
        if char in encryption_mapping:
            mapped_text += encryption_mapping[char]
        else:
            mapped_text += char

    # creating a tree using the mapped text
    for y in range(len(mapped_text)):
        avl_tree = insert(avl_tree, y, ord(mapped_text[y]))

    # mirroring the avl tree
    avl_tree = mirror(avl_tree)
    # applying a pre order traversal on the newly generated tree
    pre_order_lst = preorder_traversal(avl_tree)
    
    # forming a new string by converting the ascii values back into characters. 
    encrypted_text = ""
    for z in pre_order_lst:
        encrypted_text += chr(z[1])
    encrypted_text += chr(count_nodes(avl_tree))

    output_page(window, option = 4, lst=pre_order_lst, txt= encrypted_text)

# ============================ fifth encryption method ================================
def node_encryption(window, avl_tree, plain_text):
    # applying a simple substitution cipher on the shuffled ascii values of the initial text
    global encryption_mapping
    
    mapped_text = ""
    for char in plain_text:
        if char in encryption_mapping:
            mapped_text += encryption_mapping[char]
        else:
            mapped_text += char

    # creating a tree using the mapped text
    for y in range(len(mapped_text)):
        avl_tree = insert(avl_tree, y, ord(mapped_text[y]))

    # applying a pre order traversal on the newly generated tree
    pre_order_lst = preorder_traversal(avl_tree)
    
    # forming a new string by converting the ascii values back into characters plus adding the total number of nodes of the tree as the first encrypted character.
    encrypted_text = ""
    encrypted_text += chr(count_nodes(avl_tree))

    for z in pre_order_lst:
        encrypted_text += chr(z[1])
    
    output_page(window, option = 5, lst=pre_order_lst, txt= encrypted_text)


# ============================ text file encryption method ================================
def text_encryption(window, avl_tree, plain_text):
 # applying a simple substitution cipher on the shuffled ascii values of the initial text
    global encryption_mapping
    
    mapped_text = ""
    for char in plain_text:
        if char in encryption_mapping:
            mapped_text += encryption_mapping[char]
        else:
            mapped_text += char

    # creating a tree using the mapped text
    for y in range(len(mapped_text)):
        avl_tree = insert(avl_tree, y, ord(mapped_text[y]))

    
    # applying a pre order traversal on the newly generated tree
    pre_order_lst = preorder_traversal(avl_tree)
    
    # forming a new string by converting the ascii values back into characters plus adding the average depth of the nodes in the tree as an encrypted character at the end.
    encrypted_text = ""
    for z in pre_order_lst:
        encrypted_text += chr(z[1])
    encrypted_text += chr(average_depth(avl_tree))
    
    output_page_file(window, lst=pre_order_lst, txt= encrypted_text)

# function that regenerates a map that can decrypt the text.
def generate_decryption_map():
    global encryption_mapping
    decryption_mapping = {v: k for k, v in encryption_mapping.items()}
    return decryption_mapping

# decryption function for mirror, node and text encryption 
def filename_decryption(output_frame, avl_tree, pre_order_lst, textbox):
    global encryption_mapping
    # getting the original insertion order of the list
    insertion_order = get_insertion_order_from_preorder(avl_tree, pre_order_lst)

    # generating the reverse mapping to obtain the actual characters
    decryption_mapping = generate_decryption_map()
    decrypted_text = ''
    for char in insertion_order:
        decrypted_text += decryption_mapping.get(chr(char[1]), chr(char[1]))


    textbox.configure(state="normal")
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, decrypted_text, "center")
    textbox.configure(state="disabled")

    data_label = Label(output_frame,wraplength=500, text=' DECRYPTED TEXT', bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 20, "bold"))
    data_label.place(x=340, y=150)


# initialising the avl trees as an empty dictionary and as None (only used in neighbour encryption)
avl_tree = {}
avl_tree_2 = None

# creating splash screen
splash_screen = Tk()

create_splash_screen(splash_screen)

# destroying the splash screen
splash_screen.destroy()

# creating the tkinter screen globally and then passing it to the main function
window = Tk()

# creating the frames globally 
front_frame = Frame(window, bg='#040405', width=950, height=600)
info_frame = Frame(window, bg='#040405', width=950, height=600)
file_frame = Frame(window, bg='#040405', width=950, height=600)
output_frame = Frame(window, bg='#040405', width=950, height=600)
output_frame_file = Frame(window, bg='#040405', width=950, height=600)
final_frame = Frame(window, bg='#040405', width=950, height=600)

# calling the function to create the main screen
main(window)