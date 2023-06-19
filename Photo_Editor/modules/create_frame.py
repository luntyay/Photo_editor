import customtkinter as ctk 

class My_Frame(ctk.CTkFrame):
    def __init__(self, text, text_color, master, width, height, border_width, fg_color, **kwargs):
        super().__init__(master = master, 
                        width = width, 
                        height = height, 
                        border_width = border_width, 
                        fg_color = fg_color,
                        **kwargs)

        self.LABEL = ctk.CTkLabel(self, text= text, text_color = text_color)
        self.LABEL.place(relx = 0.2, rely = 0.01, anchor = ctk.CENTER )


class MessageFrame(ctk.CTkFrame):
    def __init__(self, text, master, width, height, border_width, bg_color, **kwargs):
        super().__init__(master= master, width= width, height= height, border_width= border_width, bg_color= bg_color, **kwargs)
        self.NAME = text
        self.FONT = ctk.CTkFont(family= "Arial", size= 20, weight= "bold") 
    def place_name(self):
        self.MESSAGE = ctk.CTkLabel(self, text= self.NAME)
        self.MESSAGE.place(x = 50, y = 10)
        # self.NAME = ctk.CTkLabel(master= self, text= self.SOUNDNAME, font= self.FONT)
        # self.NAME.place(x = 5, y = 2)
       
