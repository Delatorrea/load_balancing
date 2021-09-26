import os

class Output:
    def __init__(self):
        if os.path.exists("output.txt"):
            os.remove("output.txt")

        self.archive = open('output.txt', 'w')  # Arquivo output.txt iniciado
        self.text = ''

    def save_archive(self):
        self.archive.writelines(self.text)

    def add_line(self, line):
        self.text = line

