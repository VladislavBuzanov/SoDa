import psycopg2

from service import tokenizer


class Dao:

    def __init__(self, debug=False) -> None:
        self.debug = debug
        self.connection = psycopg2.connect(dbname='postgres',
                                           user='postgres',
                                           password='postgres',
                                           host='localhost')

    def execute(self, sql):
        cursor = self.connection.cursor()
        if self.debug:
            print('"' + sql + '" is executing')
        cursor.execute(sql)
        self.connection.commit()
        if self.debug:
            print('"' + sql + '" is executed')
        return [x for x in cursor.fetchall()]

    def find(self, sentence):
        a = self.execute(
            "SELECT it.title, ingredient.description, ingredient.utility_coefficient " +
            "FROM ingredient LEFT JOIN ingredient_title it on ingredient.id = it.id " +
            "WHERE it.title LIKE '%" + sentence + "%'")
        if a:
            return a
        else:
            return self._find_for_each(sentence)

    def _find_for_each(self, sentence):
        for word in tokenizer.tokenize(sentence):
            if word == " " or word == "" or len(word) < 4:
                continue
            else:
                sql = "SELECT DISTINCT it.title, ingredient.description, ingredient.utility_coefficient FROM ingredient LEFT JOIN ingredient_title it on ingredient.id = it.id WHERE it.title LIKE '%" + word + "%'"
                result_set = self.execute(sql)
                if result_set:
                    # print(result_set)
                    return result_set

        return []
