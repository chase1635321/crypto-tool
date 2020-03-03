import os

class Utils:
    def __init__(self):
        pass
    def load_file(self):
        print("Loading data from file")

        with open("temp.txt", "r") as f:
            self.data = f.read()
    def quit(self):
        os.system("rm temp.txt")
        exit()
