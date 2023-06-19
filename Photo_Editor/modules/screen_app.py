import customtkinter
import modules.create_frame as m_frame


class App(customtkinter.CTk):
    def __init__(self,app_width,app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}")
        self.resizable(False, False)
        self.title("Редактор зображень")

        self.FRAME_INPUT = m_frame.My_Frame(text= "", 
                                       text_color= "orange", 
                                       master = self, 
                                       width= 230, 
                                       height= 52, 
                                       border_width= None, 
                                       fg_color= None)
        self.FRAME1 = customtkinter.CTkScrollableFrame(master= self, width=199, height= 205, label_text="список зображень") # скролл фрейм для списка с изображениями
        # 2.1
        # self.FRAME2 = customtkinter.CTkScrollableFrame(master= self, width=199, height= 230, label_text="інформація про зображення") # скролл фрейм для списка с инфой про изображениями\
        # 2.2
        self.FRAME2 = m_frame.My_Frame(text= "", 
                                       text_color= "orange", 
                                       master = self, 
                                       width= 230, 
                                       height= 230, 
                                       border_width= None,
                                       fg_color= None)
        
        self.FRAME3 = m_frame.My_Frame(text= "ptoto", 
                                       text_color= "orange", 
                                       master = self, 
                                       width= 732, 
                                       height= 505, 
                                       border_width= None,
                                       fg_color= None)

        self.FRAME4 = m_frame.My_Frame(text= "", 
                                       text_color= None, 
                                       master = self, 
                                       width= 978, 
                                       height= 102, 
                                       border_width= None,
                                       fg_color= None)
        
        self.FRAME5 = m_frame.My_Frame(text= "", 
                                       text_color= None, 
                                       master = self, 
                                       width= 732, 
                                       height= 50, 
                                       border_width= None,
                                       fg_color= None)
        self.FRAME6 = m_frame.My_Frame(text= "", 
                                       text_color= None, 
                                       master = self, 
                                       width= 600, 
                                       height= 505, 
                                       border_width= 5,
                                       fg_color= None)
        
        
        
        self.FRAME_INPUT.place(x= 11, y= 11)
        self.FRAME3.place(x=255, y=11) 
        # self.FRAME3.place(x=255, y=81) 
        self.FRAME4.place(x=11, y=588) 
        self.FRAME1.place(x=11, y=74) 
        self.FRAME1._scrollbar.grid(padx=5) 
        # 2.1
        # self.FRAME2.place(x=11, y=325) 
        # self.FRAME2._scrollbar.grid(padx=5) 
        # 2.2
        self.FRAME2.place(x=11, y=345) 
        self.FRAME5.place(x=255, y=526)



        # 
        # self.SONG_OF_NAME_LBL = customtkinter.StringVar()
        # self.SONG_NAME_LBL = customtkinter.CTkLabel(self.FRAME2, textvariable= self.SONG_OF_NAME_LBL, width=35).place(x= 5,y= 5)
        # self.SONG_OF_NAME_LBL.set('Назва пісні:')
        
        # self.SONG_NAME = customtkinter.StringVar()
        # self.SONGLABEl = customtkinter.CTkLabel(self.FRAME2, textvariable= self.SONG_NAME, width=35).place(x= 5, y= 30)
        
        
        

main_app = App(1000, 700)