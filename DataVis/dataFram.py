import pandas as pd

class dataFram:
    def __init__(self, file, hd=0):
        self.file = str(file).split('/')[-1]
        if str(file).split('.')[-1] == "xlsx":
            self.excel(file, hd)
        elif str(file).split('.')[-1] == "csv":
            self.csv(file, hd)
        elif str(file).split('.')[-1] == "txt":
            self.txt(file, hd)
        else:
            print("Invalid File")

    def excel(self, file, hd):
        if bool(hd):
            self.data = pd.read_excel(file)
        else:
            self.data = pd.read_excel(file)
            names = []
            for n in range(self.data.shape[1]):
                names += ["column "+str(n)]
            self.data = pd.read_excel(file, header=None, names=names)

    def csv(self, file, hd):
        if bool(hd):
            self.data = pd.read_csv(file)
        else:
            self.data = pd.read_csv(file)
            names = []
            for n in range(self.data.shape[1]):
                names += ["column "+str(n)]
            self.data = pd.read_csv(file, header=None, names=names)

    def txt(self, file, hd):
        if bool(hd):
            self.data = pd.read_csv(file, sep=" ")
        else:
            self.data = pd.read_csv(file, sep=" ")
            names = []
            for n in range(self.data.shape[1]):
                names += ["column "+str(n)]
            self.data = pd.read_csv(file, sep=" ", header=None, names=names)

    def colNames(self):
        return self.data.columns

