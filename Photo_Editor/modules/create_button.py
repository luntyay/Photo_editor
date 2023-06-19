import customtkinter as ctk 
import modules.screen_app as m_app
import modules.find_path as f_p
import modules.function as function
import modules.add_photo as a_p




def create_button(master, text, command, width, height, image, corner_radius = 5):
    button = ctk.CTkButton(master = master,
                           width = width,
                           height = height,
                           corner_radius = corner_radius,
                           text = text,
                           fg_color= "gray10",
                           image = image,
                           hover_color = "gray12",
                           command= command
    )
    return button
# Frame 5

# оригинал
button11 = create_button(
    master= m_app.main_app.FRAME5,
    text= "original",
    command = function.return_to_original,
    width= 75,
    height= 40,
    image = None,
)
button11.place(x=10, y=5)

# повернуть 
button6 = create_button(
    master= m_app.main_app.FRAME5,
    text= "rotate",
    command = function.rotate,
    width= 75,
    height= 40,
    image = None,
)
button6.place(x=100, y=5)
# обрезать
button7 = create_button(
    master= m_app.main_app.FRAME5,
    text= "crop",
    command = function.crop,
    width= 75,
    height= 40,
    image = None,
)
button7.place(x=190, y=5)
# предыдущее фото
button_previous = create_button(
    master= m_app.main_app.FRAME5,
    text= "<-",
    command = function.previous_photo,
    width= 75,
    height= 40,
    image = None,
)
button_previous.place(x=280, y=5)
# следующее фото
button_next = create_button(
    master= m_app.main_app.FRAME5,
    text= "->",
    command = function.next_photo,
    width= 75,
    height= 40,
    image = None,
)
button_next.place(x=380, y=5)
# изменить размер
buttoт8 = create_button(
    master= m_app.main_app.FRAME5,
    text= "resize",
    command = function.resize,
    width= 75,
    height= 40,
    image = None,
)
buttoт8.place(x=470, y=5)
# добавить текст
button9 = create_button(
    master= m_app.main_app.FRAME5,
    text= "delete",
    command = function.delete_image,
    width= 75,
    height= 40,
    image = None,
)
button9.place(x=560, y=5)

# сохранить фото
button10 = create_button(
    master= m_app.main_app.FRAME5,
    text= "save",
    command = function.save,
    width= 75,
    height= 40,
    image = None,
)
button10.place(x=650, y=5)

# Frame 4

# добавление фото
button1 = create_button(
    master= m_app.main_app.FRAME4,
    width= 175,
    height= 75,
   # corner_radius= 2,
    text= "add phtoto",
    #fg_color= "gray",
    command= function.show,
    image= None
)
button1.place(x=31, y=12)
# инверсия
button2 = create_button(
    master= m_app.main_app.FRAME4,
    width= 175,
    height= 75,
    #corner_radius= 2,
    text= "inversion",
   # fg_color= "gray",
    command= function.negative,
    image= None
)
button2.place(x=216, y=12)
# черно-белый
button3 = create_button(
    master= m_app.main_app.FRAME4,
    width= 175,
    height= 75,
    # corner_radius= 2,
    text= "gray",
   # fg_color= "gray",
    command= function.make_photo_grey,
    image= None
)
button3.place(x=401, y=12)
# инверсия черно-белого
button4 = create_button(
    master= m_app.main_app.FRAME4,
    width= 175,
    height= 75,
    # corner_radius= 2,
    text= "gray inversion",
   # fg_color= "gray",
    command= function.make_photo_with_grayscale_inversion,
    image= None
)
button4.place(x=586, y=12)
# конвертация JPG -> PNG
button5 = create_button(
    master= m_app.main_app.FRAME4,
    width= 175,
    height= 75,
    # corner_radius= 2,
    text= "JPG -> PNG",
   # fg_color= "gray",
    command= function.convertion,
    image= None
)
button5.place(x=771, y=12)


