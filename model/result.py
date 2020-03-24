class Result(object):
    def __init__(self, row, numb):
        super().__init__()
        self.name = row[0]
        self.recommendation = row[1]
        self.coefficient = int(row[2])
        self.order = numb

    def __str__(self):
        return self.name + "\n" + self.recommendation + "\n" + str(self.coefficient) + "\n" + str(self.order)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)
