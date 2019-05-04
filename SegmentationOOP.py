from PyQt5.QtWidgets import QMessageBox,QSizePolicy,QSpacerItem,QGridLayout,QLineEdit,QScrollArea,QCheckBox,QSpinBox,QRadioButton,QLabel,QWidget, QApplication,QPushButton,QGroupBox,QHBoxLayout,QVBoxLayout
import  sys
from PyQt5 import QtGui
from Hole import Hole
from proccess import Process
from operator import itemgetter



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "OS Project Group 10"
        self.top = 0
        self.left = 0
        self.width = 400
        self.height =300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.hbox = QHBoxLayout()
        self.initBox()
        self.setLayout(self.hbox)
        self.show()


    def initBox(self):
        self.groupbox = QGroupBox("Segments info")
        self.groupbox.setFont(QtGui.QFont("sanserif", 15))
        self.hbox.addWidget(self.groupbox)
        self.count = 0
        self.vbox = QVBoxLayout()

        self.memorySize = QLabel("Total memory size:")
        self.memorySize.setFont(QtGui.QFont("sanserif", 13))
        self.vbox.addWidget(self.memorySize)
        self.totalMemorySize = QLineEdit(self)
        self.vbox.addWidget(self.totalMemorySize)

        self.groupbox2 = QGroupBox("Hole 0 info")
        self.groupbox2.setFont(QtGui.QFont("sanserif", 20))
        self.vbox.addWidget(self.groupbox2)
        self.vbox2 = QVBoxLayout()

        self.Startingaddress = QLabel("Starting address:")
        self.Startingaddress.setFont(QtGui.QFont("sanserif", 13))
        self.vbox2.addWidget(self.Startingaddress)
        self.StartingaddresslineEdit = QLineEdit(self)
        self.StartingaddresslineEdit.setFont(QtGui.QFont("sanserif", 13))
        self.vbox2.addWidget(self.StartingaddresslineEdit)

        self.Size = QLabel("Size:")
        self.Size.setFont(QtGui.QFont("sanserif", 13))
        self.vbox2.addWidget(self.Size)
        self.SizeLineEdit = QLineEdit(self)
        self.SizeLineEdit.setFont(QtGui.QFont("sanserif", 13))
        self.vbox2.addWidget(self.SizeLineEdit)

        self.buttonhole = QPushButton("add", self)
        self.buttonhole.clicked.connect(self.check)
        self.buttonhole.setFont(QtGui.QFont("sanserif", 13))
        self.vbox2.addWidget(self.buttonhole)
        self.groupbox2.setLayout(self.vbox2)

        self.groupbox3 = QGroupBox("Proccess 0 info")
        self.groupbox3.setFont(QtGui.QFont("sanserif", 20))
        self.vbox.addWidget(self.groupbox3)
        self.vbox3 = QVBoxLayout()

        self.numberOfSegments = QLabel("Number of segments:")
        self.numberOfSegments.setFont(QtGui.QFont("sanserif", 13))
        self.vbox3.addWidget(self.numberOfSegments)
        self.numberOfSegmentsLineEdit = QLineEdit(self)
        self.numberOfSegmentsLineEdit.setFont(QtGui.QFont("sanserif", 13))
        self.vbox3.addWidget(self.numberOfSegmentsLineEdit)

        self.buttonSegments = QPushButton("insert segments info", self)
        self.buttonSegments.clicked.connect(self.showSegmentsInfo)
        self.buttonSegments.setFont(QtGui.QFont("sanserif", 13))
        self.vbox3.addWidget(self.buttonSegments)

        self.buttonFinish = QPushButton("Finish", self)
        self.buttonFinish.clicked.connect(self.showMethodOfAllocation)
        self.buttonFinish.setFont(QtGui.QFont("sanserif", 13))
        self.vbox3.addWidget(self.buttonFinish)

        self.groupbox3.setLayout(self.vbox3)
        self.groupbox.setLayout(self.vbox)
        self.holes = list()
        self.proccess = list()
        self.i = 0
        self.j = 0
        self.processno = 1
    def check(self):
        Startaddress = int(self.StartingaddresslineEdit.text())
        totalMemory = int(self.totalMemorySize.text())
        Size = int(self.SizeLineEdit.text())
        found=0
        if Startaddress > totalMemory :
            buttonReply = QMessageBox.question(self, "Hole "+str(self.i), "The start address is out of range" ,QMessageBox.Ok)
        elif Startaddress+Size >totalMemory:
            buttonReply = QMessageBox.question(self, "Hole " + str(self.i), "out of range",QMessageBox.Ok)
        else:
            for i in self.holes:
                if Startaddress == i.startAddress:
                    buttonReply = QMessageBox.question(self,"Hole " + str(self.i), "There is another hole has the same startaddress", QMessageBox.Ok)
                    found=1
                    break
                elif Startaddress > i.startAddress and Startaddress < i.startAddress+i.size:
                    buttonReply = QMessageBox.question(self, "Hole " + str(self.i), "There is another hole occupies this space", QMessageBox.Ok)
                    found = 1
                    break
            if found==0:
                self.addHole()
    def addHole(self):
        Startaddress=int(self.StartingaddresslineEdit.text())
        Size =int(self.SizeLineEdit.text())
        self.holes.append(Hole(Startaddress,Size,"hole"+str(self.i)))
        self.i = self.i +1
        self.groupbox2.setTitle("Hole "+str(self.i)+" info")
        self.StartingaddresslineEdit.setText('0')
        self.SizeLineEdit.setText('0')
    def showSegmentsInfo(self):
        self.buttonSegments.hide()
        self.buttonFinish.hide()
        self.segmentsNames = list()
        self.segmentsSize = list()
        i = int(self.numberOfSegmentsLineEdit.text())
        self.segmentsGroupBox = QGroupBox("Segments info")
        self.vbox4 = QVBoxLayout()
        if self.j == 0:
            for j in range(i):
                self.segmentName = QLabel("Segment " + str(j + 1) + " Name:")
                self.segmentName.setFont(QtGui.QFont("sanserif", 13))

                self.vbox4.addWidget(self.segmentName)
                self.segmentNamelinetext = QLineEdit(self)
                self.segmentNamelinetext.setFont(QtGui.QFont("sanserif", 13))
                self.segmentsNames.append(self.segmentNamelinetext)
                self.vbox4.addWidget(self.segmentNamelinetext)
                self.segmentSize = QLabel("Segment " + str(j + 1) + " Size:")
                self.segmentSize.setFont(QtGui.QFont("sanserif", 13))
                self.vbox4.addWidget(self.segmentSize)
                self.segmentSizeLineEdit = QLineEdit(self)
                self.segmentSizeLineEdit.setFont(QtGui.QFont("sanserif", 13))
                self.segmentsSize.append(self.segmentSizeLineEdit)
                self.vbox4.addWidget(self.segmentSizeLineEdit)

            self.segmentsGroupBox.setLayout(self.vbox4)
            self.scroll = QScrollArea()
            self.scroll.setWidget(self.segmentsGroupBox)
            self.scroll.setWidgetResizable(True)
            self.scroll.setFixedWidth(350)
            self.scroll.setFixedHeight(300)
            self.vbox3.addWidget(self.scroll)
            self.addproccess = QPushButton("Add process", self)
            self.addproccess.clicked.connect(self.addPro)
            self.addproccess.setFont(QtGui.QFont("sanserif", 13))
            self.vbox3.addWidget(self.addproccess)
            self.j = 1
    def addPro(self):
        noOfSegments = int(self.numberOfSegmentsLineEdit.text())
        segmentssize = list()
        segmentsname = list()
        segment=list()
        for i in self.segmentsSize:
            segmentssize.append(int(i.text()))
        for i in self.segmentsNames:
            segmentsname.append(i.text())
        for i in range(len(segmentssize)):
            segmentt={'name':segmentsname[i] ,
                     'size':segmentssize[i]}
            segment.append(segmentt)
        self.proccess.append(Process(segment,noOfSegments,"P" + str(self.processno-1)))
        self.scroll.hide()
        self.addproccess.hide()
        self.buttonSegments.show()
        self.buttonFinish.show()
        self.j = 0
        self.groupbox3.setTitle("Process " + str(self.processno) + " info")
        self.processno = self.processno + 1
    def showMethodOfAllocation(self):
        self.buttonSegments.hide()
        self.buttonFinish.hide()
        self.groupbox.hide()
        self.groupbox2.hide()
        self.groupbox3.hide()
        self.groupbox = QGroupBox("Method of Allocation")
        self.groupbox.setFont(QtGui.QFont("sanserif", 15))
        vbox = QVBoxLayout()
        self.hbox.addWidget(self.groupbox)
        self.firstfit = QRadioButton("first fit")
        self.bestfit = QRadioButton("best fit")
        self.worstfit = QRadioButton("worst fit")
        self.draw = QPushButton("Draw")
        self.draw.clicked.connect(self.Show)
        vbox.addWidget(self.firstfit)
        vbox.addWidget(self.bestfit)
        vbox.addWidget(self.worstfit)
        vbox.addWidget(self.draw)
        self.groupbox.setLayout(vbox)
    def Show(self):
        self.groupbox.hide()

        self.groupbox = QGroupBox("De-allocate a process")
        self.groupbox.setFont(QtGui.QFont("sanserif", 15))
        vbox = QVBoxLayout()
        self.hbox.addWidget(self.groupbox)
        self.pro = QRadioButton("Process")
        self.oldpro = QRadioButton("Old Process")
        self.ProcessName = QLabel("enter the process name ")
        self.ProcessNameLineText=QLineEdit(self)

        self.drawdeallocate = QPushButton("Draw after Deallocation")
        self.drawdeallocate.clicked.connect(self.DrawDeallocate)
        self.restartt = QPushButton("Restart")
        self.restartt.clicked.connect(self.restart)
        vbox.addWidget(self.pro)
        vbox.addWidget(self.oldpro)
        vbox.addWidget(self.ProcessName)
        vbox.addWidget(self.ProcessNameLineText)
        vbox.addWidget(self.drawdeallocate)
        vbox.addWidget(self.restartt)
        self.groupbox.setLayout(vbox)


        self.DrawingList= list()
        self.draw.hide()
        self.groupbox2 = QGroupBox("Drawing")
        self.groupbox2.setFont(QtGui.QFont("sanserif", 15))
        self.grid = QVBoxLayout()
        self.grid.setSpacing(-10)
        totalMemory= int(self.totalMemorySize.text())
        sortedHoles = sorted(self.holes, key=lambda x: x.startAddress, reverse=False)
        smallestHoles=sorted(self.holes, key=lambda x: x.size, reverse=False)
        largestHoles=sorted(self.holes, key=lambda x: x.size, reverse=True)
        self.failedProcess=list()
        if self.firstfit.isChecked():
            sum = 1
            done=0
            for i in self.proccess:
                lists=i.organizeProcess(sortedHoles,self.DrawingList,self.failedProcess)
                sortedHoles=lists[0]
                self.DrawingList=lists[1]
                if lists[2] == 1:
                    self.failedProcess.append(i)

            holeno=0
            for i in sortedHoles:
                self.DrawingList=i.organizeHole(self.DrawingList,holeno)
                holeno = holeno + 1

            self.SortedDrawingList = sorted(self.DrawingList, key=itemgetter('startaddress'), reverse=False)
            i=0
            x=0
            count=1
            while (i+x) < totalMemory:
                for j in self.SortedDrawingList:
                    if j['startaddress'] == i+x  and j['size'] > 0:
                        if x!=0:
                            process = {
                                'name': "oldprocess"+str(count),
                                'parentProcess': 'oldProcess',
                                'startaddress': i,
                                'size': x,
                                'oldprocess': 1,
                                'hole': 0,
                                'segment': 0,
                                'failed': 0,
                                'holeno': -1
                            }
                            self.DrawingList.append(process)
                            i=i+x+j['size']
                            done=1
                            count = count+1
                            break
                        else:
                            i = i + x + j['size']
                            done = 1
                            break
                    else:
                        done=0
                if done==1:
                    x=0
                else:
                    x=x+1

            process = {
                'name': "oldprocess" + str(count),
                'parentProcess': 'oldProcess',
                'startaddress': i,
                'size': x,
                'oldprocess': 1,
                'hole': 0,
                'segment': 0,
                'failed': 0,
                'holeno': -1
            }
            self.DrawingList.append(process)
            self.SortedDrawingList = sorted(self.DrawingList, key=itemgetter('startaddress'), reverse=False)


            if len(self.failedProcess) > 0 :
                for i in self.failedProcess:
                    print(i.name + " hasn't found a place in memory")
                    self.SortedDrawingList=i.removeProcess(self.SortedDrawingList)
        elif self.bestfit.isChecked():
            sum = 1
            done = 0
            for i in self.proccess:
                lists = i.organizeProcess(smallestHoles, self.DrawingList, self.failedProcess)
                smallestHoles = sorted(lists[0], key=lambda x: x.size, reverse=False)
                self.DrawingList = lists[1]
                if lists[2] == 1:
                    self.failedProcess.append(i)

            holeno = 0
            for i in smallestHoles:
                self.DrawingList = i.organizeHole(self.DrawingList, holeno)
                holeno = holeno + 1

            self.SortedDrawingList = sorted(self.DrawingList, key=itemgetter('startaddress'), reverse=False)
            i = 0
            x = 0
            count = 1
            while (i + x) < totalMemory:
                for j in self.SortedDrawingList:
                    if j['startaddress'] == i + x and j['size'] > 0:
                        if x != 0:
                            process = {
                                'name': "oldprocess" + str(count),
                                'parentProcess': 'oldProcess',
                                'startaddress': i,
                                'size': x,
                                'oldprocess': 1,
                                'hole': 0,
                                'segment': 0,
                                'failed': 0,
                                'holeno': -1
                            }
                            self.DrawingList.append(process)
                            i = i + x + j['size']
                            done = 1
                            count = count + 1
                            break
                        else:
                            i = i + x + j['size']
                            done = 1
                            break
                    else:
                        done = 0
                if done == 1:
                    x = 0
                else:
                    x = x + 1

            process = {
                'name': "oldprocess" + str(count),
                'parentProcess': 'oldProcess',
                'startaddress': i,
                'size': x,
                'oldprocess': 1,
                'hole': 0,
                'segment': 0,
                'failed': 0,
                'holeno': -1
            }
            self.DrawingList.append(process)
            self.SortedDrawingList = sorted(self.DrawingList, key=itemgetter('startaddress'), reverse=False)

            if len(self.failedProcess) > 0:
                for i in self.failedProcess:
                    print(i.name + " hasn't found a place in memory")
                    self.SortedDrawingList = i.removeProcess(self.SortedDrawingList)
        else:
            sum = 1
            done = 0
            for i in self.proccess:
                lists = i.organizeProcess(largestHoles, self.DrawingList, self.failedProcess)
                largestHoles = sorted(lists[0], key=lambda x: x.size, reverse=True)
                self.DrawingList = lists[1]
                if lists[2] == 1:
                    self.failedProcess.append(i)

            holeno = 0
            for i in smallestHoles:
                self.DrawingList = i.organizeHole(self.DrawingList, holeno)
                holeno = holeno + 1

            self.SortedDrawingList = sorted(self.DrawingList, key=itemgetter('startaddress'), reverse=False)
            i = 0
            x = 0
            count = 1
            while (i + x) < totalMemory:
                for j in self.SortedDrawingList:
                    if j['startaddress'] == i + x and j['size'] > 0:
                        if x != 0:
                            process = {
                                'name': "oldprocess" + str(count),
                                'parentProcess': 'oldProcess',
                                'startaddress': i,
                                'size': x,
                                'oldprocess': 1,
                                'hole': 0,
                                'segment': 0,
                                'failed': 0,
                                'holeno': -1
                            }
                            self.DrawingList.append(process)
                            i = i + x + j['size']
                            done = 1
                            count = count + 1
                            break
                        else:
                            i = i + x + j['size']
                            done = 1
                            break
                    else:
                        done = 0
                if done == 1:
                    x = 0
                else:
                    x = x + 1

            process = {
                'name': "oldprocess" + str(count),
                'parentProcess': 'oldProcess',
                'startaddress': i,
                'size': x,
                'oldprocess': 1,
                'hole': 0,
                'segment': 0,
                'failed': 0,
                'holeno': -1
            }
            self.DrawingList.append(process)
            self.SortedDrawingList = sorted(self.DrawingList, key=itemgetter('startaddress'), reverse=False)

            if len(self.failedProcess) > 0:
                for i in self.failedProcess:
                    print(i.name + " hasn't found a place in memory")
                    self.SortedDrawingList = i.removeProcess(self.SortedDrawingList)
        self.Draww()
        self.groupbox2.setLayout(self.grid)
        self.scroll2 = QScrollArea()
        self.scroll2.setWidget(self.groupbox2)
        self.scroll2.setWidgetResizable(True)
        self.scroll2.setFixedWidth(400)
        self.scroll2.setFixedHeight(700)
        self.hbox.addWidget(self.scroll2)
    def Draww(self):
        for i in self.SortedDrawingList:
            if i['failed'] == 0:
                if i['size'] > 0:
                    button = QPushButton(i['name'])
                    button.setToolTip("<h1>start: " + str(i['startaddress']) +
                                      "<br>end:" + str(i['startaddress'] + i['size'] - 1) + "</h1")
                    button.setMaximumHeight(i['size'] + 20)
                    self.grid.addWidget(button)
            else:
                print(i['name'] + " hasn't found a place in memory")
    def removeOldProcess(self, requiredProcess):

        for i in self.SortedDrawingList:
            if i['name'] == requiredProcess:
                i['parentProcess'] = 'hole'
                i['hole'] = 1
                i['segment'] = 0
                i['holeno'] = -1
                i['oldprocess'] = 0

        sum = 1
        while sum > 0:
            for i in range(len(self.SortedDrawingList)):
                if self.SortedDrawingList[i]['name'] == requiredProcess:
                    if self.SortedDrawingList[i - 1]['hole'] == 1:
                        self.SortedDrawingList[i]['startaddress'] = self.SortedDrawingList[i - 1]['startaddress']
                        self.SortedDrawingList[i]['size'] = self.SortedDrawingList[i - 1]['size'] + self.SortedDrawingList[i]['size']
                        if self.SortedDrawingList[i - 1]['holeno'] > self.SortedDrawingList[i]['holeno']:
                            self.SortedDrawingList[i]['holeno'] = self.SortedDrawingList[i - 1]['holeno']
                        self.SortedDrawingList.pop(i - 1)
                        break
                    elif i == len(self.SortedDrawingList) - 1:
                        if self.SortedDrawingList[i - 1]['hole'] == 1:
                            self.SortedDrawingList[i]['startaddress'] = self.SortedDrawingList[i - 1]['startaddress']
                            self.SortedDrawingList[i]['size'] = self.SortedDrawingList[i - 1]['size'] + self.SortedDrawingList[i]['size']
                            if self.SortedDrawingList[i - 1]['holeno'] > self.SortedDrawingList[i]['holeno']:
                                self.SortedDrawingList[i]['holeno'] = self.SortedDrawingList[i - 1]['holeno']
                            self.SortedDrawingList.pop(i - 1)
                            break
                        else:
                            if self.SortedDrawingList[i]['holeno'] < 0:
                                self.SortedDrawingList[i]['name'] = 'NewHole'
                            else:
                                self.SortedDrawingList[i]['name'] = 'Hole' + str(self.SortedDrawingList[i]['holeno'])

                    elif self.SortedDrawingList[i + 1]['hole'] == 1:
                        self.SortedDrawingList[i]['size'] = self.SortedDrawingList[i + 1]['size'] + self.SortedDrawingList[i]['size']
                        if self.SortedDrawingList[i + 1]['holeno'] > self.SortedDrawingList[i]['holeno']:
                            self.SortedDrawingList[i]['holeno'] = self.SortedDrawingList[i + 1]['holeno']
                        self.SortedDrawingList.pop(i + 1)
                        break

                    else:
                        if self.SortedDrawingList[i]['holeno'] < 0:
                            self.SortedDrawingList[i]['name'] = 'NewHole'
                        else:
                            self.SortedDrawingList[i]['name'] = 'Hole' + str(self.SortedDrawingList[i]['holeno'])

            sum = 0
            for i in self.SortedDrawingList:
                if (requiredProcess in i['name']) and i['failed'] == 0:
                    sum = sum + 1
    def DrawDeallocate(self):
        self.groupbox3 = QGroupBox("Drawing after Deallocation")
        self.groupbox3.setFont(QtGui.QFont("sanserif", 15))
        self.grid = QVBoxLayout()
        self.grid.setSpacing(-10)
        requiredProcessName=self.ProcessNameLineText.text()
        if self.pro.isChecked():
            for i in self.proccess:
                if i.name == requiredProcessName:
                    requiredProcess = i
            self.SortedDrawingList=requiredProcess.removeProcess(self.SortedDrawingList)
        else:
            self.removeOldProcess(requiredProcessName)

        self.Draww()
        self.scroll2.hide()
        self.count = self.count+1
        if self.count != 1:
            self.scroll3.hide()
        self.groupbox3.setLayout(self.grid)
        self.scroll3 = QScrollArea(self)
        self.scroll3.setWidget(self.groupbox3)
        self.scroll3.setWidgetResizable(True)
        self.scroll3.setFixedWidth(400)
        self.scroll3.setFixedHeight(700)
        self.hbox.addWidget(self.scroll3)
    # def externalComp(self):

    def restart(self):
        if self.count >0:
            self.scroll3.hide()
        self.scroll2.hide()
        self.groupbox.hide()
        self.initBox()


if __name__ =="__main__":

    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
