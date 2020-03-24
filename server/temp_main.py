from PIL import Image
import nltk
import service.image_service as service

# nltk.download()
from service import t_solver

# file_name = input("Enter file name")
# print(t_solver.rec_text(Image.open(file_name)))
recommendation = service.handle_image(Image.open('1496419762197994073.jpg'))
# print(recommendation)
