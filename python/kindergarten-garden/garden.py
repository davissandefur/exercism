class Garden(object):
    _plant_key = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, garden, students=("Alice Bob Charlie David Eve Fred Ginny Harriet Ileana "
                                         "Joseph Kincaid Larry".split())):
        self.plant_rows = garden.split()
        self.students = sorted(students)

    def plants(self, student):
        """ This method determines the plants that a given student has. """

        start = self.students.index(student)*2
        plot = slice(start, start + 2)

        return [self._plant_key[abbreviation] for abbreviation in (self.plant_rows[0][plot] + self.plant_rows[1][plot])]