# import customtkinter as ctk
# import modules.function as function
# import modules.test1 as test1
# import os
# import modules.lists as l
# import modules.text_input as m_input
# from PIL import Image
# from urllib.request import urlopen

# def open_file():
#     # работает 
#     global file, content
#     file = ctk.filedialog.askopenfile(mode ='r', filetypes =[('Файл "JPG"', '*.jpg')])
#     content = file.name
#     # l.list_with_images.append(f"{content.split('/')[-1]}")
#     # l.list_of_images.append(content)
#     list_of_image = []
#     list_of_image.append(content)
#     l.list_with_images.append(list_of_image)
#     if l.index == l.max_index:
#         l.index += 1
#         l.max_index += 1
#         print(f"index: {l.index}")
#         print(f"len: {len(l.list_with_images)}")
    
#     elif l.index < l.max_index:
#         l.max_index += 1
#         l.index = l.max_index
#         print(f"max_index {l.max_index}")
#         print(f"index {l.index}")


#     function.image_show()
    
    
# def open_file():
#     # url = "https://i1.sndcdn.com/artworks-000628317025-ph8y0k-t240x240.jpg"
#     url = m_input.text.get()
#     image = Image.open(urlopen(url))
#     function.im_show(image)
#     m_input.text.set("")
#     function.show()


