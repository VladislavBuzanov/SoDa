import service.t_solver as solver
import service.text_service as text_handler


def handle_image(file):
    text = solver.rec_text(file)
    key_words = text_handler.handle_text(text)
    return key_words

