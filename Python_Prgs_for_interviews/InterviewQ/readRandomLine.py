# to read random line in the file( ex. 50, 65, 78th line)
class ReadRandomLine:
    def __init__(self, objfile):
        self._objfile = objfile

    def __getitem__(self, index):
        lines = self._objfile.readlines()
        try:
            return lines[self.index]
        except IndexError:
            print('Please check the line number')


fileobj = open(r"C:\Users\LENOVO\.PyCharmCE2019.3\config\scratches\filetoRead.txt", 'r')
ojb = ReadRandomLine(fileobj)

ReadRandomLine.__getitem__(index=5)