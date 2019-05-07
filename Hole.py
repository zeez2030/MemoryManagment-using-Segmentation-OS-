

class Hole:
    def __init__(self,start,size,name,holeno):
        self.name=name
        self.size=size
        self.startAddress=start
        self.holeno=holeno
    def printName(self):
        print(self.name)
    def ChangeSize(self,size):
        self.size=size

    def organizeHole(self,DrawingList):
        if self.size > 0:
            process = {
                'name':self.name,
                'parentProcess': "hole",
                'startaddress': self.startAddress,
                'size': self.size,
                'oldprocess': 0,
                'hole': 1,
                'segment': 0,
                'failed': 0,
                'holeno': self.holeno
            }
            DrawingList.append(process)

        return DrawingList