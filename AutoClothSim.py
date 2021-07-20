import os
import time
import json
from datetime import datetime 
path = "D:/AAA Dropbox/60_It_Means_Their_Life/6_Projects/animationCashe"
files = os.listdir(path)



class autoSim():


    def __init__(self):

        self.log = {}
        self.logFile = ""
        self.rootPath = ""
        self.character = ""
        self.files = []
    
    def setRoot(self, root):
        self.rootPath = root

    def setCharacter(self,name):
        self.character = name

    def listFiles(self):
        if self.rootPath == None:
            self.warning("No root had been set")
        if os.path.isdir(self.rootPath):
            listOfFiles = os.listdir(self.rootPath)
            if listOfFiles:
                for file in listOfFiles:
                    if file.split(".")[-1] == "abc":
                        self.files.append(file)
                if self.files == None:
                    self.warning("No Alembic Cache found")
        else:
            self.warning("Setted root do not exist")

    
    def getLastModify(self, file):
        return time.ctime(os.path.getctime(file))


    def loadLog(self):

        logfile = os.path.join(self.rootPath, "log.json")
        if os.path.isfile(logfile):
            print "exists"
            self.logFile = logfile
            self.openJson(self.logFile)
        else:
            print "creiating"
            now = str(datetime.now())
            self.log = {"Created":now}
            self.saveLog(logfile)
            
            print  "SSSSS"

    def saveLog(self, logfile):

        with open(logfile, 'w') as outfile:
            json.dump(self.log,  outfile,  indent=4, sort_keys=True)


    def openJson(self, path):
        path = path.replace("\\", "/")

        if path.split(".")[-1] == "json":
            try:
                filePath = osPath(path)
                if os.path.exists(filePath):
                    with open(filePath, 'r') as infile:
                        data = json.load(infile)
                self.log = data
            except:
                return None
        else:
            return None

    def logging(self):
        print self.log
        now = str(datetime.now())
        self.log["LastChange"] =  now
        self.saveLog(self.logFile)


    def warning(self, msg):
        print msg

        

aa = autoSim()
aa.setRoot(path)
aa.listFiles()
aa.loadLog()
aa.logging()