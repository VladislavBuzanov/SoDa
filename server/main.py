import requests

import service.spellchecker as spell

# word = input()
# params = {'text': word, 'lang': "ru"}
# r = requests.get('http://speller.yandex.net/services/spellservice.json/checkText', params=params)
#
# if r.status_code == 200:
#     print(r.json())
#     for row in r.json():
#         if row['s']:
#             print(row['s'][0])
from dao.repository import Dao

dao = Dao()
a = dao._find_for_each("молоко из сухого молока")
print(a)
