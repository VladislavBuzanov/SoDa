import service.t_solver as solver
import service.answer_service as answerer
from dao.repository import Dao
from model import result

dao = Dao()


def handle_image(file):
    text = solver.rec_text(file)
    list_rec = []
    text = text.replace("-", '').replace("_", '').replace(";", ",").replace(")", ",").replace("(", ",")
    content = text.split(",")
    i = 0
    for sentence in content:
        result_str = dao.find(sentence)
        if result_str:
            i += 1
            res = result.Result(result_str[0], i)
            list_rec.append(res)
            # print(res)
    list_rec = set(list_rec)
    quality = calculate_quality(list_rec, i)
    print(quality)
    quality = answerer.handle(quality)
    return [quality, list_rec]


def calculate_quality(list_rec, i):
    result_quality = 0.0
    for subj in list_rec:
        result_quality += ((i - subj.order + 1) * subj.coefficient * 1.0) / (i + 1)
    return result_quality
