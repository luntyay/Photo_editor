from PIL import Image, ImageDraw, ImageOps, ImageFont
import customtkinter as ctk
import modules.find_path as f_p
import modules.screen_app as m_app
import modules.create_frame as c_f
import modules.text_input as m_input
import time
import threading
import modules.lists as m_lists
import os
from PIL import Image
from urllib.request import urlopen

event_url = False
event_1 = False

def open_file_askopenfile():
    # работает 
    global file, content

    m_app.main_app.FRAME6.grid_remove()

    file = ctk.filedialog.askopenfile(mode ='r', filetypes =[('Файл "JPG"', '*.jpg')])
    content = file.name
    # l.list_with_images.append(f"{content.split('/')[-1]}")
    # l.list_of_images.append(content)
    
    image_origin = Image.open(content)
    
    
    list_of_image = []
    list_of_image.append(content)
    list_of_image.append(image_origin)
    m_lists.list_with_images.append(list_of_image)
    if m_lists.index == m_lists.max_index:
        m_lists.index += 1
        m_lists.max_index += 1
        print(f"index: {m_lists.index}")
        print(f"max_index: {m_lists.max_index}")
    
    elif m_lists.index < m_lists.max_index:
        m_lists.max_index += 1
        m_lists.index = m_lists.max_index
        print(f"index: {m_lists.index}")
        print(f"max_index: {m_lists.max_index}")

    image_show(image_origin)
    
    if len(m_lists.list_with_images) > 1:
        if len(m_lists.list_with_images[m_lists.index]) > 1:
            # original_image = m_lists.list_with_images[m_lists.index][0]
            for i in range(len(m_lists.list_with_images[m_lists.index]) - 1):
                if i > 0:
                    del m_lists.list_with_images[m_lists.index][i]
                    
    add_img_frame()

            
    
    
def open_file_url():
    global content
    # if event_url == False:
    m_app.main_app.FRAME6.grid_remove()
        # event_url == True
    # if event_url == True:
    # url = "https://i1.sndcdn.com/artworks-000628317025-ph8y0k-t240x240.jpg"
    url = m_input.text.get()
    m_input.text.set("")
    image1 = Image.open(urlopen(url))

    image1.save("images\\url_picture.jpg")
    
    content = f_p.find_path_file('images\\url_picture.jpg')
    
    list_of_image = []
    list_of_image.append(content)
    list_of_image.append(image1)
    
    m_lists.list_with_images.append(list_of_image)
    
    
    if m_lists.index == m_lists.max_index:
        m_lists.index += 1
        m_lists.max_index += 1
        print(f"index: {m_lists.index}")
        print(f"max_index: {m_lists.max_index}")
    
    elif m_lists.index < m_lists.max_index:
        m_lists.max_index += 1
        m_lists.index = m_lists.max_index
        print(f"index: {m_lists.index}")
        print(f"max_index: {m_lists.max_index}")
    
    # print(m_lists.list_with_images, list_of_image)
    print(f"index: {m_lists.index}")
    print(f"max_index: {m_lists.max_index}")

    image_show(image1)

    if len(m_lists.list_with_images) > 1:
        if len(m_lists.list_with_images[m_lists.index]) > 1:
            # original_image = m_lists.list_with_images[m_lists.index][0]
            for i in range(len(m_lists.list_with_images[m_lists.index]) - 1):
                if i > 0:
                    del m_lists.list_with_images[m_lists.index][i]
    
    add_img_frame()

    # event_url == False


photo_list = []
# photo_list_frames = []

event = False
event_resize = False


# class show_photo(ctk.CTk):  
#     def __init__(self):
#         super().__init__()
#         global image_origin, photo_width, photo_height


#         self.IMAGE = ctk.CTkImage(
#             light_image = image_origin,
#             size = (photo_width, photo_height)
#         ) 
     

#         self.IMAGE_LABEL = ctk.CTkLabel(
#             master=m_app.main_app.FRAME3,
#             text = "",
#             image = self.IMAGE,
#             bg_color='black'
#         )
#         self.IMAGE_LABEL.grid(row= 5, column= 5)
#         load_photo()

photo_width = 730
photo_height = 505

counter = 0
# def im_show(image_origin):
#     global photo_height, photo_width
#     new_image = image_origin.resize((photo_width, photo_height))
#     new_image.save("images\\sid_resized.jpg")
#     image = ctk.CTkImage(
#             light_image = new_image,
#             size = (photo_width, photo_height)
#         )
#     image_label = ctk.CTkLabel(
#         master=m_app.main_app.FRAME3,
#         text = "",
#         image = image,
#         bg_color='black'
#     )
#     image_label.grid(row= 5, column= 5)
#     load_photo(name_of_image=f_p.find_path_file('images\\sid_resized.jpg'))


    
    

def image_show(image_origin):
    global counter
    global photo_height, photo_width
   # image_origin = Image.open(f_p.find_path_file("images\\sid.jpg")
    # image_origin = Image.open(m_lists.list_with_images[m_lists.index][-1])
    
    # f_p.find_path_file(a_p.content)
    new_image = image_origin.resize((photo_width, photo_height))
    # new_image.save("images\\sid_resized.jpg")
    image = ctk.CTkImage(
            light_image = new_image,
            size = (photo_width, photo_height)
        )
    image_label = ctk.CTkLabel(
        master=m_app.main_app.FRAME3,
        text = "",
        image = image,
        bg_color='black'
    )
    image_label.grid(row= 5, column= 5)
    load_photo(name_of_image=m_lists.list_with_images[m_lists.index][0])
    image_info()
    
    if counter == 0:
        counter += 1


def image_info():
    # global image2
    # image = Image.open(f_p.find_path_file(content))
    #m_lists.list_with_images[0][0]
    width, height = m_lists.list_with_images[m_lists.index][-1].size
    # print(a_p.content)

    list_with_name_of_image = m_lists.list_with_images[m_lists.index][0].split(".")
    
    font = ctk.CTkFont(family= "Arial", size= 17, weight= "bold") 
    
    width_label = ctk.CTkLabel(
        master=m_app.main_app.FRAME2,
        text = f"Ширина зображення:{width}",
        bg_color="grey17",
        font=font
    )
    
    height_label = ctk.CTkLabel(
        master=m_app.main_app.FRAME2,
        text = f"Висота зображення:{height}",
        bg_color="grey17",
        font=font
    )
    
    type_label = ctk.CTkLabel(
        master=m_app.main_app.FRAME2,
        text = f"Тип зображення:{list_with_name_of_image[-1]}",
        # text = f"Тип зображення: jpg",
        bg_color="grey17",
        font=font
    )
    
    width_label.place(x=0, y=0)
    height_label.place(x=0, y=50)
    type_label.place(x=0, y=100)
    # image2.close()

    
def return_to_original():
    # print(m_lists.list_with_images[0][0])
    
    len_of_list = len(m_lists.list_with_images[m_lists.index])
    for i in range(len_of_list):
        # print(i)
        if i > 1:
            del m_lists.list_with_images[m_lists.index][i]
            print("true")
            
    orig_image = m_lists.list_with_images[m_lists.index][-1]

    image = ctk.CTkImage(
        light_image = orig_image,
        size = (photo_width, photo_height)
    )
    image_label = ctk.CTkLabel(
        master=m_app.main_app.FRAME3,
        text = "",
        image = image,
        bg_color='black'
    )
    image_label.grid(row = 5, column = 5)
    

    print(m_lists.list_with_images)
    load_photo(name_of_image = m_lists.list_with_images[m_lists.index][0])
    update_frame()



def make_photo_grey():
    global photo_height, photo_width, counter
    
    if counter > 0:
        # if len(m_lists.list_with_images[m_lists.index]) - 1 > 1:
        #     for i in range(len(m_lists.list_with_images[m_lists.index])):
        #         if i > 1:
        #             print(i)
        #             del m_lists.list_with_images[m_lists.index][i]
        

        # grey_image = m_lists.list_with_images[m_lists.index][-1]  # Открываем изображение


        # if len(m_lists.list_with_images[m_lists.index]) > 2:
        #     for i in range(len(m_lists.list_with_images[m_lists.index])):
        #         if i > 1:
        #             del m_lists.list_with_images[m_lists.index][i]

        
        # draw = ImageDraw.Draw(grey_image)  # Создаем инструмент для рисования
        # pixels_of_image = grey_image.load()  # Выгружаем значения пикселей
        # width, height = grey_image.size


        # if grey_image.mode == 'RGBA':
        #     r,g,b,a = grey_image.split()
        #     rgb_image = Image.merge('RGB', (r,g,b))

        #     inverted_image = rgb_image.convert("L")

        #     r2,g2,b2 = inverted_image.split()

        #     final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
        #     for x in range(width):
        #         for y in range(height):
        #             r = pixels_of_image[x, y][0] #узнаём значение красного цвета пикселя
        #             g = pixels_of_image[x, y][1] #зелёного
        #             b = pixels_of_image[x, y][2] #синего
        #             sr = (r + g + b) // 3 #среднее значение
        #             draw.point((x, y), (sr, sr, sr)) #рисуем пиксель

        #     m_lists.list_with_images[m_lists.index].append(final_transparent_image)

        # else:
        #     final_transparent_image = grey_image.convert("L")
        #     m_lists.list_with_images[m_lists.index].append(final_transparent_image)
        image1 = m_lists.list_with_images[m_lists.index][-1]

        if len(m_lists.list_with_images[m_lists.index]) - 1 > 1:
            for i in range(len(m_lists.list_with_images[m_lists.index])):
                if i > 1:
                    print(i)
                    del m_lists.list_with_images[m_lists.index][i]

        draw = ImageDraw.Draw(image1)
        pixels_of_image = image1.load()
        width, height = image1.size

        if image1.mode == 'RGBA':
            r, g, b, a = image1.split()
            rgb_image = Image.merge('RGB', (r, g, b))

            black_white_image = rgb_image.convert("L")

            r2, g2, b2 = black_white_image.split()

            final_transparent_image = Image.merge('RGBA', (r2, g2, b2, a))

            for x in range(width):
                for y in range(height):
                    r = pixels_of_image[x, y][0] #узнаём значение красного цвета пикселя
                    g = pixels_of_image[x, y][1] #зелёного
                    b = pixels_of_image[x, y][2] #синего
                    sr = (r + g + b) // 3 #среднее значение
                    draw.point((x, y), (sr, sr, sr)) #рисуем пиксель

            m_lists.list_with_images[m_lists.index].append(final_transparent_image)
        else:
            final_transparent_image = image1.convert("L")
            m_lists.list_with_images[m_lists.index].append(final_transparent_image)
                
        
        image = ctk.CTkImage(
            light_image = final_transparent_image,
            size = (photo_width, photo_height)
        )
        image_label = ctk.CTkLabel(
            master=m_app.main_app.FRAME3,
            text = "",
            image = image,
            bg_color='black'
        )
        image_label.grid(row= 5, column= 5)
        
        
        print(m_lists.list_with_images)
        load_photo(name_of_image = m_lists.list_with_images[m_lists.index][0])
        update_frame()

# f_p.find_path_file('images\\sid_resized.jpg')

def make_photo_with_grayscale_inversion():
    
    global photo_height, photo_width, counter
    if counter > 0:
    

        image1 = m_lists.list_with_images[m_lists.index][-1]

        if len(m_lists.list_with_images[m_lists.index]) - 1 > 1:
            for i in range(len(m_lists.list_with_images[m_lists.index])):
                if i > 1:
                    print(i)
                    del m_lists.list_with_images[m_lists.index][i]

        draw = ImageDraw.Draw(image1)
        pixels_of_image = image1.load()
        width, height = image1.size

        if image1.mode == 'RGBA':
            r, g, b, a = image1.split()
            rgb_image = Image.merge('RGB', (r, g, b))

            black_white_image = rgb_image.convert("L")

            r2, g2, b2 = black_white_image.split()

            final_transparent_image = Image.merge('RGBA', (r2, g2, b2, a))

            for x in range(width):
                for y in range(height):
                    r = pixels_of_image[x, y][0]
                    g = pixels_of_image[x, y][1]
                    b = pixels_of_image[x, y][2]
                    sr = (r + g + b) // 3
                    draw.point((x, y), (r2 - sr, g2 - sr, b2 - sr))

            m_lists.list_with_images[m_lists.index].append(final_transparent_image)
        else:
            black_white_image = image1.convert("L")
            final_transparent_image = ImageOps.invert(black_white_image)
            m_lists.list_with_images[m_lists.index].append(final_transparent_image)
                
        
        image = ctk.CTkImage(
            light_image = final_transparent_image,
            size = (photo_width, photo_height)
        )
        image_label = ctk.CTkLabel(
            master=m_app.main_app.FRAME3,
            text = "",
            image = image,
            bg_color='black'
        )
        image_label.grid(row= 5, column= 5)
        
        
        print(m_lists.list_with_images)
        load_photo(name_of_image = m_lists.list_with_images[m_lists.index][0])
        update_frame()
    

mage2 = None
def load_photo(name_of_image):
    global image2
    image2 = Image.open(name_of_image)
    photo_list.append(image2)
    # add_img_frame()
    # image2.close()
    
    # print(photo_list)
    
    
    #return image2
    #print(111)
    

# def add_photo_frame():
#     global photo_list, photo_list_frames
#     photo_frame = c_f.MessageFrame(text= "im",
#                                     master= m_app.main_app.FRAME1, 
#                                     width= 200, 
#                                     height= 50,
#                                     border_width= 2,
#                                     bg_color= "black"
#     )
#     photo_frame.place_name()
#     photo_list_frames.append(photo_frame)
#     # print(photo_list_frames)
#     photo_frame.grid(row= 1, column= 1)
message_y = 0
def add_img_frame():
    global event_1, message_y, image2
    img_frame = c_f.MessageFrame(text= content.split("/")[-1],
                                    master= m_app.main_app.FRAME1, 
                                    width= 200, 
                                    height= 50,
                                    border_width= 2,
                                    bg_color="red")
    img_frame.place_name()
    
    m_lists.list_of_frames.append(img_frame)
    
    
    image = ctk.CTkImage(
                    light_image = m_lists.list_with_images[m_lists.index][-1],
                    size = (33, 22)
                )
    image_label = ctk.CTkLabel(
                    master=img_frame,
                    text = "",
                    image = image,
                    bg_color='black'
                )
    # image_label.grid(row= 1, column= 1)
    # img_button = ctk.CTkButton(
    #     master= img_frame,
    #     fg_color= "red",
    #     image = image,
    #     width = 28,
    #     height= 28,
    #     text = None,
    #     command= open_button_img
    #     )
    image_label.place(x= 11, y= 11)

    m_lists.photo_list_frames.append(img_frame)
    # photo_list_frames.append(img_frame)
    if event_1 == False:
        img_frame.grid(row = message_y, pady = 10)
        message_y += 1
        # print(event) 
    
    

def update_frame():
    image = ctk.CTkImage(
                    light_image = m_lists.list_with_images[m_lists.index][-1],
                    size = (33, 22)
                )
    image_label = ctk.CTkLabel(
                    master=m_lists.list_of_frames[m_lists.index],
                    text = "",
                    image = image,
                    bg_color='black'
                )
    image_label.place(x= 11, y= 11)
    m_lists.list_of_frames[m_lists.index].NAME = m_lists.list_with_images[m_lists.index][0].split("/")[-1]

    
    m_lists.list_of_frames[m_lists.index].place_name()
 
# def fun_thread(n):
#     m_input.text.set("Введите ширину и высоту")
#     time.sleep(n)
#     m_input.text.set("")

# def thread():
#     thread = threading.Thread(target= fun_thread, args= (2, ))
#     thread.start()
    # thread.join()

# def input_heigh():
#     global new_photo_height
#     new_photo_height = m_input.text.get()
#     m_input.text.set("")
    # button_label = ctk.CTkLabel(
    #     master = m_app.main_app.FRAME3, 
    #     # master = f_frame.MessageFrame.message_label(),
    #     text = m_input.text.get(),
    #     font = m_input.font_size
    # )
# def input_width():
#     global new_photo_width
#     new_photo_width = m_input.text.get()
#     m_input.text.set("")

# def resize_else():
    # global event, event_resize
    # image1 = Image.open(f_p.find_path_file('images\\sid_resized.jpg'))
    # image_resize = Image.Image.resize(self=  image1,size= (int(new_photo_height), int(new_photo_width)))
    # image_resize.save("images\\image_resized.jpg")
    # image = ctk.CTkImage(
    #         light_image = image_resize,
    #         size = (photo_width, photo_height)
    #     )
    # image_label = ctk.CTkLabel(
    #         master=m_app.main_app.FRAME3,
    #         text = "",
    #         image = image,
    #         bg_color='black'
    #     )
    # image_label.grid(row= 5, column= 5)
    # print(image_resize.size)
    # load_photo(name_of_image = f_p.find_path_file('images\\image_resized.jpg'))
    # event == False
    # event_resize = False

def resize():
    global photo_height, photo_width, event, event_resize, new_photo_width, new_photo_height,image2

    # if event_resize == False:
    #     # thread()
    #     event_resize = True
    # elif event_resize == True:
    #     if event == False:
    #         new_photo_width = m_input.text.get()
    #         m_input.text.set("")
    #         event= True
    #     elif event == True:
    #         new_photo_height = m_input.text.get()
    #         m_input.text.set("")
            # event = False
            # event_resize = None
    # elif event_resize == None:
            # image1 = Image.open(f_p.find_path_file('images\\sid_resized.jpg'))
    # image_resize = Image.Image.resize(self=image2,size= (int(new_photo_width), int(new_photo_height)))
    new_photo_width = 100
    new_photo_height = 100
    
    image_resize = m_lists.list_with_images[m_lists.index][-1]
    
    if len(m_lists.list_with_images[m_lists.index]) - 1 > 1:
        for i in range(len(m_lists.list_with_images[m_lists.index])):
            if i > 1:
                print(i)
                del m_lists.list_with_images[m_lists.index][i]
    
    
    
    image_resize = Image.Image.resize(self=image_resize,size= (new_photo_width,new_photo_height))

    
    m_lists.list_with_images[m_lists.index].append(image_resize)

    
    image = ctk.CTkImage(
            light_image = image_resize,
            size = (photo_width, photo_height)
        )
    image_label = ctk.CTkLabel(
            master=m_app.main_app.FRAME3,
            text = "",
            image = image,
            bg_color='black'
        )
    image_label.grid(row= 5, column= 5)

    load_photo(name_of_image = m_lists.list_with_images[m_lists.index][0])
    event == False
    event_resize = False
    update_frame()


def rotate():
    global photo_height, photo_width, counter, image2
    
    if counter > 0:
        
        rotated_img = m_lists.list_with_images[m_lists.index][-1]
        
        
        if len(m_lists.list_with_images[m_lists.index]) - 1 > 1:
            for i in range(len(m_lists.list_with_images[m_lists.index])):
                if i > 1:
                    print(i)
                    del m_lists.list_with_images[m_lists.index][i]
        
        rotated_img = rotated_img.rotate(-90, expand=True)
        
        m_lists.list_with_images[m_lists.index].append(rotated_img)

        image = ctk.CTkImage(
            light_image = rotated_img,
            size = (photo_width, photo_height)
        )
        image_label = ctk.CTkLabel(
            master=m_app.main_app.FRAME3,
            text = "",
            image = image,
            bg_color='black'
        )
        image_label.grid(row= 5, column= 5)
        load_photo(name_of_image = m_lists.list_with_images[m_lists.index][0])
        update_frame()

def crop():
    global photo_height, photo_width, counter, image2
    if counter > 0:
        
        im_cut = m_lists.list_with_images[m_lists.index][-1]
        
        
        if len(m_lists.list_with_images[m_lists.index]) - 1 > 1:
            for i in range(len(m_lists.list_with_images[m_lists.index])):
                if i > 1:
                    print(i)
                    del m_lists.list_with_images[m_lists.index][i]
        
        im_cut = im_cut.crop((100, 75, 300, 150))
        
        
        m_lists.list_with_images[m_lists.index].append(im_cut)
        
        image = ctk.CTkImage(
            light_image = im_cut,
            size = (photo_width, photo_height)
        )
        image_label = ctk.CTkLabel(
            master=m_app.main_app.FRAME3,
            text = "",
            image = image,
            bg_color='black'
        )
        image_label.grid(row= 5, column= 5)
        load_photo(name_of_image = m_lists.list_with_images[m_lists.index][0])
        update_frame()
        
        
def next_photo():
    if m_lists.index < m_lists.max_index:
        m_lists.index += 1

        str_or_not = isinstance(m_lists.list_with_images[m_lists.index][-1], str)
        
        if not str_or_not:
            image = ctk.CTkImage(
                light_image = m_lists.list_with_images[m_lists.index][-1],
                size = (photo_width, photo_height)
            )
            image_label = ctk.CTkLabel(
                master=m_app.main_app.FRAME3,
                text = "",
                image = image,
                bg_color='black'
            )
            image_label.grid(row= 5, column= 5)
        else:
            image = ctk.CTkImage(
                light_image = m_lists.list_with_images[m_lists.index][-1],
                size = (photo_width, photo_height)
            )
            image_label = ctk.CTkLabel(
                master=m_app.main_app.FRAME3,
                text = "",
                image = image,
                bg_color='black'
            )
            image_label.grid(row= 5, column= 5)
            
        print(f"index: {m_lists.index}")
        print(f"max_index: {m_lists.max_index}")

        load_photo(name_of_image = m_lists.list_with_images[m_lists.index][0])

def previous_photo():
    if m_lists.index > 0:
        m_lists.index -= 1

        str_or_not = isinstance(m_lists.list_with_images[m_lists.index][-1], str)
        
        if not str_or_not:
            image = ctk.CTkImage(
                light_image = m_lists.list_with_images[m_lists.index][-1],
                size = (photo_width, photo_height)
            )
            image_label = ctk.CTkLabel(
                master=m_app.main_app.FRAME3,
                text = "",
                image = image,
                bg_color='black'
            )
            image_label.grid(row= 5, column= 5)
        else:
            image = ctk.CTkImage(
                light_image = m_lists.list_with_images[m_lists.index][-1],
                size = (photo_width, photo_height)
            )
            image_label = ctk.CTkLabel(
                master=m_app.main_app.FRAME3,
                text = "",
                image = image,
                bg_color='black'
            )
            image_label.grid(row= 5, column= 5)
        
        print(f"index: {m_lists.index}")
        print(f"max_index: {m_lists.max_index}")
        
        load_photo(name_of_image = m_lists.list_with_images[m_lists.index][0])
        # print(m_lists.list_with_images[m_lists.index])
        # print(f"prev_index {m_lists.index}")
        # image1.close()


def negative():
    #print(123)
    global photo_height, photo_width, counter
    
    if counter > 0:

        image1 = m_lists.list_with_images[m_lists.index][-1]

        if len(m_lists.list_with_images[m_lists.index]) - 1 > 1:
            for i in range(len(m_lists.list_with_images[m_lists.index])):
                if i > 1:
                    print(i)
                    del m_lists.list_with_images[m_lists.index][i]

        draw = ImageDraw.Draw(image1)  
        pixels_of_image = image1.load()  
        width, height = image1.size

        if image1.mode == 'RGBA':
            r,g,b,a = image1.split()
            rgb_image = Image.merge('RGB', (r,g,b))

            inverted_image = ImageOps.invert(rgb_image)

            r2,g2,b2 = inverted_image.split()

            final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
            for x in range(width):
                for y in range(height):
                    r = pixels_of_image[x, y][0] 
                    g = pixels_of_image[x, y][1] 
                    b = pixels_of_image[x, y][2] 
                    sr = (r + g + b) // 3 
                    draw.point((x, y), (r2 - sr, g2 - sr, b2 - sr)) 

            m_lists.list_with_images[m_lists.index].append(final_transparent_image)
        else:
            final_transparent_image = ImageOps.invert(image1)
            m_lists.list_with_images[m_lists.index].append(final_transparent_image)

        
        image = ctk.CTkImage(
            light_image = final_transparent_image,
            size = (photo_width, photo_height)
        )
        image_label = ctk.CTkLabel(
            master=m_app.main_app.FRAME3,
            text = "",
            image = image,
            bg_color='black'
        )
        image_label.grid(row= 5, column= 5)
        load_photo(name_of_image = m_lists.list_with_images[m_lists.index][0])
        update_frame()
        # image1.close()


def add_text():
    global image2
    # label_text = ctk.CTkLabel(
    #     master = m_app.main_app.FRAME3,
    #     text = m_input.text.get(),
    #     font = m_input.font_size
    #     # bg_color= "transparent"
    # )
    # label_text.place(x= 11, y= 11)
    font = ImageFont.truetype("arial.ttf", 25)
    drawer = ImageDraw.Draw(image2)
    drawer.text(xy=(101, 110), text="m_input.text.get()", font=font)
    image2.save('images\\new_img.jpg')
    load_photo(name_of_image = f_p.find_path_file('images\\new_img.jpg'))
    # image1 = Image.open(f_p.find_path_file('new_img.jpg'))  
    # image2.show()
    m_input.text.set("")

def convertion():
    
    
    
    if len(m_lists.list_with_images[m_lists.index]) > 1:
        
        path_to_file = m_lists.list_with_images[m_lists.index][0].split(".")
        path_to_file[-1] = "png"
        path_to_file = ".".join(path_to_file)
        
        m_lists.list_with_images[m_lists.index][-1].save(path_to_file, "PNG")
        
        counter = 0
        
        for i in range(len(m_lists.list_with_images[m_lists.index])):
            print(i - counter)
            counter += 1
            del m_lists.list_with_images[m_lists.index][i - counter]
            
        m_lists.list_with_images[m_lists.index].append(path_to_file)
        
        image1 = Image.open(m_lists.list_with_images[m_lists.index][0])
        
        # print(m_lists.list_with_images[m_lists.index][0])
        
        m_lists.list_with_images[m_lists.index].append(image1)
        
        # print(m_lists.list_with_images)

    
        update_frame()
    
    # if counter > 0:
    #     m_lists.list_with_images[m_lists.index][-1].save(path_to_file, "PNG")   
    #     # load_photo(name_of_image = m_lists.list_with_images[m_lists.index][-1])
    #     print(m_lists.list_with_images)

def save():
    global photo_height, photo_width, counter, image2
    # m_lists.list_with_images[m_lists.index][-1]
    # image2.save("images\\saved_image.jpg")
    # for i in range(len(m_lists.list_with_images[m_lists.index]) - 2):
    #     del m_lists.list_with_images[m_lists.index][0]

    # path_to_file = m_lists.list_with_images[m_lists.index][0].split("/")
    # path_to_file = path_to_file[-1]
    # path_to_file = "".join(path_to_file) 
    # print(f"images\\{path_to_file}")
    
    if len(m_lists.list_with_images[m_lists.index]) > 2:
        m_lists.list_with_images[m_lists.index][-1].save(m_lists.list_with_images[m_lists.index][0])
        del m_lists.list_with_images[m_lists.index][1]
        print(m_lists.list_with_images)
        
    update_frame()
        


def show():
    if event_url == False:
        m_app.main_app.FRAME6.grid(padx=200, pady= 100) 

        button_askopenfile = ctk.CTkButton(master = m_app.main_app.FRAME6,
                            width = 250,
                            height = 200,
                            corner_radius = 5,
                            text = "button_askopenfile",
                            fg_color= "gray10",
                            hover_color = "gray12",
                            command= open_file_askopenfile)
        button_askopenfile.place(x=25, y=250) 

        button_url = ctk.CTkButton(master = m_app.main_app.FRAME6,
                            width = 250,
                            height = 200,
                            corner_radius = 5,
                            text = "button_url",
                            fg_color= "gray10",
                            hover_color = "gray12",
                            command= open_file_url)
        button_url.place(x=320, y=250) 
    # if event_url == True:
    #     url = m_input.text.get()
    #     image = Image.open(urlopen(url))
    #     # im_show(image)
    #     image_show(image)
    #     m_input.text.set("")
    #     event_url == False


def delete_image():
    global counter
    if counter > 0:
        if len(m_lists.list_with_images) == 1:
            for child in m_app.main_app.FRAME3.winfo_children():
                child.destroy()
            m_lists.photo_list_frames[m_lists.index].grid_remove()
            del m_lists.photo_list_frames[m_lists.index]
            del m_lists.list_with_images[m_lists.index]
            m_lists.index -= 1
            m_lists.max_index -= 1
            counter = 0
        if len(m_lists.list_with_images) > 1:
            if m_lists.index == 0:
                m_lists.photo_list_frames[m_lists.index].grid_remove()
                del m_lists.photo_list_frames[m_lists.index]
                del m_lists.list_with_images[m_lists.index]
                m_lists.max_index -= 1
                image = ctk.CTkImage(
                    light_image = m_lists.list_with_images[m_lists.index][-1],
                    size = (photo_width, photo_height)
                )
                image_label = ctk.CTkLabel(
                    master=m_app.main_app.FRAME3,
                    text = "",
                    image = image,
                    bg_color='black'
                )
                image_label.grid(row= 5, column= 5)              
                
            if m_lists.index > 0:
                m_lists.photo_list_frames[m_lists.index].grid_remove()
                del m_lists.photo_list_frames[m_lists.index]
                del m_lists.list_with_images[m_lists.index]
                m_lists.index -= 1
                m_lists.max_index -= 1
                # print(len(m_lists.list_with_images))
                # # print(m_lists.list_with_images)
                # if len(m_lists.list_with_images) == 1:
                #     print(1)
                #     m_lists.max_index = 0
                image = ctk.CTkImage(
                    light_image = m_lists.list_with_images[m_lists.index][-1],
                    size = (photo_width, photo_height)
                )
                image_label = ctk.CTkLabel(
                    master=m_app.main_app.FRAME3,
                    text = "",
                    image = image,
                    bg_color='black'
                )
                image_label.grid(row= 5, column= 5)
            
        print(f"index: {m_lists.index}")
        print(f"max_index: {m_lists.max_index}")
        # print(m_lists.max_index)
        
        
        
        
