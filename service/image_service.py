import service.t_solver as solver
from dao.repository import Dao

dao = Dao()


def handle_image(file):
    text = solver.rec_text(file)
    recommendation = []
    quality = int(0)
    text = text.replace("-", '').replace("_", '').replace(";", ",").replace(")", ",").replace("(", ",")
    content = text.split(",")
    for sentence in content:
        # print(content)
        result = dao.find(sentence)
        # print(result)
        for row in result:
            recommendation.append(row[1])
            quality += int(row[2])
    print(recommendation)
    print(quality)
    return
