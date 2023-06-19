import customtkinter as ctk
import modules.screen_app as m_app



font_size = ctk.CTkFont(
    family= "Arial",
    size= 15,
    weight= "bold"
)

text = ctk.StringVar()

text_input = ctk.CTkEntry(
    master= m_app.main_app.FRAME_INPUT,
    width= 209,
    height= 30,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text
)

text_input.place(
    x = 11,
    y = 11
    # anchor = ctk.CENTER
    # sticky = ctk.CENTER
)
# text_input.grid(x= 0, y= 0)
