from PIL import Image
import nltk
import service.image_service as service

# nltk.download()


file_name = input("Enter file name")
recommendation = service.handle_image(Image.open(file_name))
# print(recommendation)
