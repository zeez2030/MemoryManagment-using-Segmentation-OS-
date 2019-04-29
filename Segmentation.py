from PyQt5.QtWidgets import QSizePolicy,QSpacerItem,QGridLayout,QLineEdit,QScrollArea,QCheckBox,QSpinBox,QRadioButton,QLabel,QWidget, QApplication,QPushButton,QGroupBox,QHBoxLayout,QVBoxLayout
import  sys
from PyQt5 import QtGui
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
        self.StartingaddresslineEdit.setFont(QtGui.QFont("sanserif",13))
        self.vbox2.addWidget(self.StartingaddresslineEdit)

        self.Size = QLabel("Size:")
        self.Size.setFont(QtGui.QFont("sanserif", 13))
        self.vbox2.addWidget(self.Size)
        self.SizeLineEdit = QLineEdit(self)
        self.SizeLineEdit.setFont(QtGui.QFont("sanserif", 13))
        self.vbox2.addWidget(self.SizeLineEdit)

        self.buttonhole = QPushButton("add", self)
        self.buttonhole.clicked.connect(self.addHole)
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
        self.proccess=list()
        self.i = 0
        self.j=0
        self.processno = 1
    def addHole(self):
        Startaddress=int(self.StartingaddresslineEdit.text())
        Size =int(self.SizeLineEdit.text())
        hole = {'name': "hole"+str(self.i), 'startaddress': Startaddress,
                   'size': Size}
        self.holes.append(hole)
        self.i = self.i +1
        self.groupbox2.setTitle("Hole "+str(self.i)+" info")
    def showSegmentsInfo(self):
        self.buttonSegments.hide()
        self.buttonFinish.hide()
        self.segmentsNames=list()
        self.segmentsSize=list()
        i = int(self.numberOfSegmentsLineEdit.text())
        self.segmentsGroupBox = QGroupBox("Segments info")
        self.vbox4 = QVBoxLayout()
        if  self.j ==0:
            for j in range(i):
                self.segmentName = QLabel("Segment "+str(j+1)+" Name:")
                self.segmentName.setFont(QtGui.QFont("sanserif", 13))

                self.vbox4.addWidget(self.segmentName)
                self.segmentNamelinetext = QLineEdit(self)
                self.segmentNamelinetext.setFont(QtGui.QFont("sanserif", 13))
                self.segmentsNames.append(self.segmentNamelinetext)
                self.vbox4.addWidget(self.segmentNamelinetext)
                self.segmentSize = QLabel("Segment " +str(j+1)+" Size:")
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
            self.j=1
    def addPro(self):
        segmentssize=list()
        segmentsname=list()
        startaddress=list()
        for i in self.segmentsSize:
            segmentssize.append(int(i.text()))
            startaddress.append(0)
        for i in self.segmentsNames:
            segmentsname.append(i.text())
        self.scroll.hide()
        self.addproccess.hide()
        self.buttonSegments.show()
        self.buttonFinish.show()
        self.j=0
        self.groupbox3.setTitle("Process "+str(self.processno)+" info")
        process = {'name': "P" + str(self.processno-1), 'noOfSegments': int(self.numberOfSegmentsLineEdit.text()),
                   'segmentsName':segmentsname , 'segmentsSize':segmentssize , 'startaddress':startaddress}
        self.proccess.append(process)
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
        self.draw = QPushButton("Draw")
        self.draw .clicked.connect(self.Draw)
        vbox.addWidget(self.firstfit)
        vbox.addWidget(self.bestfit)
        vbox.addWidget(self.draw )
        self.groupbox.setLayout(vbox)
    def Draw(self):
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
        sortedHoles = sorted(self.holes, key=itemgetter('startaddress'), reverse=False)
        failedProcess=list()
        if self.firstfit.isChecked():
            sum = 1
            done=0
            while sum >0:
                for i in range(len(self.proccess)):
                    for j in range(self.proccess[i]['noOfSegments']):
                        for k in sortedHoles:
                            if self.proccess[i]['segmentsSize'][j] <= k['size'] and self.proccess[i]['segmentsSize'][j] != 0:
                                start= k['startaddress']
                                process = {'name': self.proccess[i]['name']+": "+self.proccess[i]['segmentsName'][j],
                                           'parentProcess':self.proccess[i]['name'],
                                           'startaddress': start ,
                                           'size':self.proccess[i]['segmentsSize'][j],
                                           'oldprocess':0,
                                           'hole':0,
                                           'segment':1,
                                           'failed':0,
                                           'holeno': -1
                                           }
                                self.DrawingList.append(process)
                                k['startaddress']=k['startaddress']+self.proccess[i]['segmentsSize'][j]
                                k['size']=k['size']-self.proccess[i]['segmentsSize'][j]
                                self.proccess[i]['segmentsSize'][j]=0
                                done = 1
                                break
                            else:
                                done=0

                        if done != 1:
                            process = {
                                'name': self.proccess[i]['name'] + ": " + self.proccess[i]['segmentsName'][j],
                                'parentProcess': self.proccess[i]['name'],
                                'startaddress': 99999,
                                'size': self.proccess[i]['segmentsSize'][j],
                                'oldprocess': 0,
                                'hole': 0,
                                'segment': 1,
                                'failed': 1,
                                'holeno':-1

                            }
                            if  self.proccess[i]['name'] not in failedProcess:
                                failedProcess.append(self.proccess[i]['name'])
                            self.DrawingList.append(process)
                            self.proccess[i]['segmentsSize'][j] = 0
                            done=0

                sum=0
                for q in self.proccess:
                    for w in q['segmentsSize']:
                        sum=sum+w


            holeno=0
            for i in sortedHoles:
                process = {
                    'name': i['name'],
                    'parentProcess': "hole",
                    'startaddress': i['startaddress'],
                    'size': i['size'],
                    'oldprocess': 0,
                    'hole': 1,
                    'segment': 0,
                    'failed': 0,
                    'holeno':holeno

                }
                holeno=holeno+1
                self.DrawingList.append(process)
            self.SortedDrawingList = sorted(self.DrawingList, key=itemgetter('startaddress'), reverse=False)


            i=0
            x=0
            count=1
            while (i+x) < totalMemory:
                for j in self.SortedDrawingList:
                    if j['startaddress'] == i+x  and j['size'] > 0:
                        if x!=0:
                            process = {
                                'name': "OldProcess"+str(count),
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
                'name': "OldProcess" + str(count),
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


            if len(failedProcess) > 0 :
                for i in failedProcess:
                    self.removeProcess(i)

            self.Draww()

        else:
            methodOfAllocation=0

        self.groupbox2.setLayout(self.grid)
        self.scroll2 = QScrollArea()
        self.scroll2.setWidget(self.groupbox2)
        self.scroll2.setWidgetResizable(True)
        self.scroll2.setFixedWidth(400)
        self.scroll2.setFixedHeight(700)
        self.hbox.addWidget(self.scroll2)
    def Draww(self):
        # pos=0
        for i in self.SortedDrawingList:
            if i['failed'] == 0:
                if i['size'] > 0:
                    button = QPushButton(i['name'])
                    button.setToolTip("<h1>start: " + str(i['startaddress']) +
                                      "<br>end:" + str(i['startaddress'] + i['size'] - 1) + "</h1")
                    button.setMaximumHeight(i['size'] + 20)
                    self.grid.addWidget(button)
                    # pos = pos + 1
            else:
                print(i['name'] + " hasn't found a place in memory")
    def removeProcess(self,requiredProcess):
        for i in self.SortedDrawingList:
            if i['parentProcess']==requiredProcess:
                i['parentProcess']= 'hole'
                i['hole']=1
                i['segment']=0
                i['holeno']=-1
        flags=list()
        for i in range(len(self.SortedDrawingList)):
            flags.append(0)
        finish=1
        sum=1
        while sum>0:
            for i in range(len(self.SortedDrawingList)):
                if self.SortedDrawingList[i]['hole']==1 and self.SortedDrawingList[i+1]['hole']==1 and self.SortedDrawingList[i]['failed'] ==0:
                    self.SortedDrawingList[i]['size'] = self.SortedDrawingList[i+1]['size']+self.SortedDrawingList[i]['size']
                    if self.SortedDrawingList[i]['holeno'] > self.SortedDrawingList[i+1]['holeno']:
                        self.SortedDrawingList.pop(i+1)

                        break
                    elif (self.SortedDrawingList[i]['holeno'] == self.SortedDrawingList[i+1]['holeno'])  and self.SortedDrawingList[i]['holeno']== -1 :
                        self.SortedDrawingList[i]['name'] = 'NewHole '+requiredProcess
                        self.SortedDrawingList.pop(i+1)

                        break
                    elif  self.SortedDrawingList[i]['holeno'] < self.SortedDrawingList[i+1]['holeno']:
                        self.SortedDrawingList[i]['holeno']=self.SortedDrawingList[i+1]['holeno']
                        self.SortedDrawingList[i]['name'] = self.SortedDrawingList[i + 1]['name']
                        self.SortedDrawingList.pop(i + 1)

                        break
                elif self.SortedDrawingList[i]['hole']==1 and self.SortedDrawingList[i+1]['hole'] != 1 and flags[i] == 0 and self.SortedDrawingList[i]['failed'] ==0:
                    if self.SortedDrawingList[i]['holeno'] < 0 :
                        self.SortedDrawingList[i]['name']= 'NewHole'
                    flags[i]=1

                    break
            sum=0
            for i in self.SortedDrawingList :
                if (requiredProcess in i['name']) and i['failed'] ==0:
                    sum=sum+1
    def removeOldProcess(self,requiredProcess):
        for i in self.SortedDrawingList:
            if i['name'] == requiredProcess:
                i['parentProcess'] = 'hole'
                i['hole'] = 1
                i['segment'] = 0
                i['holeno'] = -1
                i['oldprocess']=0
        flags = list()
        for i in range(len(self.SortedDrawingList)):
            flags.append(0)
        finish = 1
        sum = 1
        while sum > 0:
            for i in range(len(self.SortedDrawingList)):
                if self.SortedDrawingList[i]['hole'] == 1 and self.SortedDrawingList[i + 1]['hole'] == 1 and self.SortedDrawingList[i]['failed'] == 0:
                    self.SortedDrawingList[i]['size'] = self.SortedDrawingList[i + 1]['size'] +  self.SortedDrawingList[i]['size']
                    if self.SortedDrawingList[i]['holeno'] > self.SortedDrawingList[i + 1]['holeno']:
                        self.SortedDrawingList.pop(i + 1)

                        break
                    elif (self.SortedDrawingList[i]['holeno'] == self.SortedDrawingList[i + 1]['holeno']) and self.SortedDrawingList[i]['holeno'] == -1:
                        self.SortedDrawingList[i]['name'] = 'NewHole ' + requiredProcess
                        self.SortedDrawingList.pop(i + 1)

                        break
                    elif self.SortedDrawingList[i]['holeno'] < self.SortedDrawingList[i + 1]['holeno']:
                        self.SortedDrawingList[i]['holeno'] = self.SortedDrawingList[i + 1]['holeno']
                        self.SortedDrawingList[i]['name'] = self.SortedDrawingList[i + 1]['name']
                        self.SortedDrawingList.pop(i + 1)

                        break
                elif self.SortedDrawingList[i]['hole'] == 1 and self.SortedDrawingList[i + 1]['hole'] != 1 and flags[i] == 0 and self.SortedDrawingList[i]['failed'] == 0:
                    if self.SortedDrawingList[i]['holeno'] < 0:
                        self.SortedDrawingList[i]['name'] = 'NewHole'
                    flags[i] = 1

                    break
            sum = 0
            for i in self.SortedDrawingList:
                if (requiredProcess in i['name']) and i['failed'] == 0:
                    sum = sum + 1
    def DrawDeallocate(self):
        self.groupbox3 = QGroupBox("Drawing after Deallocation")
        self.groupbox3.setFont(QtGui.QFont("sanserif", 15))
        self.grid = QVBoxLayout()
        self.grid.setSpacing(-10)
        requiredProcess=self.ProcessNameLineText.text()
        if self.pro.isChecked():
            self.removeProcess(requiredProcess)
        else:
            self.removeOldProcess(requiredProcess)

        self.Draww()

        self.groupbox3.setLayout(self.grid)
        self.scroll3 = QScrollArea(self)
        self.scroll3.setWidget(self.groupbox3)
        self.scroll3.setWidgetResizable(True)
        self.scroll3.setFixedWidth(400)
        self.scroll3.setFixedHeight(700)
        self.hbox.addWidget(self.scroll3)
    def restart(self):
        self.scroll2.hide()
        self.groupbox.hide()
        self.initBox()









if __name__ =="__main__":

    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
