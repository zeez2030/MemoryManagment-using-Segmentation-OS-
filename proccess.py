from segments import Segment
from Hole import Hole

class Process:
    def __init__(self,arrayOfSegments,noOfSegments,name):
        self.Segments=list()
        self.NoSegments=noOfSegments
        self.name=name
        self.arrayofSeg=arrayOfSegments
        self.insertSeg(self.arrayofSeg)
        self.finished=0

    def insertSeg(self,arrayofSeg):
        for i in range(self.NoSegments):
            seg=Segment(arrayofSeg[i]['size'],arrayofSeg[i]['name'])

            self.Segments.append(seg)

    def printName(self):
        print(self.name)
    def organizeProcess(self,sortedHoles,DrawingList,failedProcess):


        self.finished=1
        sum=1
        failed=0
        while sum > 0:
                for j in range(self.NoSegments):
                    for k in sortedHoles:
                        if self.Segments[j].size <= k.size and self.Segments[j].size != 0:
                            start = k.startAddress
                            process = {'name': self.name + ": " + self.Segments[j].name,
                                       'parentProcess': self.name,
                                       'startaddress': start,
                                       'size': self.Segments[j].size,
                                       'oldprocess': 0,
                                       'hole': 0,
                                       'segment': 1,
                                       'failed': 0,
                                       'holeno': -1
                                       }
                            DrawingList.append(process)
                            k.startAddress = k.startAddress + self.Segments[j].size
                            k.ChangeSize(k.size  - self.Segments[j].size)
                            self.Segments[j].size = 0
                            done = 1
                            break
                        else:
                            done = 0

                    if done != 1:
                        lent=0
                        found=0
                        while lent<len(failedProcess):
                            if self.name == failedProcess[lent].name:
                                found=1
                                break
                            else:
                                found=0
                            lent=lent+1
                        if found==1:
                            failed=0
                        else:
                            failed=1
                        self.Segments[j].size = 0
                        done = 0

                sum = 0
                for q in self.Segments:
                        sum = sum + q.size
        zeez=list()
        zeez.append(sortedHoles)
        zeez.append(DrawingList)
        zeez.append(failed)
        return zeez

    def removeProcess(self,SortedDrawingList):
        for i in SortedDrawingList:
            if i['parentProcess'] == self.name:
                i['parentProcess'] = 'hole'
                i['hole'] = 1
                i['segment'] = 0
                i['holeno'] = -1
        flags = list()
        for i in range(len(SortedDrawingList)):
            flags.append(0)
        sum = 1
        while sum>0:
            for i in range(len(SortedDrawingList)):
                if self.name in SortedDrawingList[i]['name'] :
                    if SortedDrawingList[i-1]['hole'] == 1  and i!= 0:
                        SortedDrawingList[i]['startaddress'] =SortedDrawingList[i-1]['startaddress']
                        SortedDrawingList[i]['size'] = SortedDrawingList[i - 1]['size'] + SortedDrawingList[i]['size']
                        if SortedDrawingList[i-1]['holeno']>SortedDrawingList[i]['holeno']:
                            SortedDrawingList[i]['holeno']=SortedDrawingList[i-1]['holeno']
                        SortedDrawingList.pop(i - 1)
                        break
                    elif i == len(SortedDrawingList) - 1  :
                        if SortedDrawingList[i - 1]['hole'] == 1 and i!= 0:
                            SortedDrawingList[i]['startaddress'] = SortedDrawingList[i - 1]['startaddress']
                            SortedDrawingList[i]['size'] = SortedDrawingList[i - 1]['size'] + SortedDrawingList[i]['size']
                            if SortedDrawingList[i - 1]['holeno'] > SortedDrawingList[i]['holeno']:
                                SortedDrawingList[i]['holeno'] = SortedDrawingList[i - 1]['holeno']
                            SortedDrawingList.pop(i - 1)
                            break
                        else:
                            if SortedDrawingList[i]['holeno'] < 0:
                                SortedDrawingList[i]['name'] = 'NewHole'
                            else:
                                SortedDrawingList[i]['name'] = 'Hole' + str(SortedDrawingList[i]['holeno'])

                    elif SortedDrawingList[i+1]['hole'] == 1 :
                        SortedDrawingList[i]['size'] = SortedDrawingList[i + 1]['size'] + SortedDrawingList[i]['size']
                        if SortedDrawingList[i+1]['holeno']>SortedDrawingList[i]['holeno']:
                            SortedDrawingList[i]['holeno']=SortedDrawingList[i+1]['holeno']
                        SortedDrawingList.pop(i + 1)
                        break

                    else:
                        if SortedDrawingList[i]['holeno']< 0:
                            SortedDrawingList[i]['name']='NewHole'
                        else:
                            SortedDrawingList[i]['name'] = 'Hole'+str(SortedDrawingList[i]['holeno'])
            sum=0
            for i in SortedDrawingList :
                if (self.name in i['name']) and i['failed'] ==0:
                    sum=sum+1
        sortedHoles=list()
        k=0
        for i in SortedDrawingList:
            if i['hole']==1 and i['size']>0:
                sortedHoles.append(Hole(i['startaddress'],i['size'],i['name'],i['holeno']))

        returnlist=list()
        returnlist.append(SortedDrawingList)
        returnlist.append(sortedHoles)
        return returnlist