#! /usr/bin/env python

# Author: ilkkayli                                                      
# Prerequisities: python 2.x with pip installed.              
# Upgrades all installed pip distributions.                             


from PySide.QtCore import *
from PySide.QtGui import *
import sys
import mainGui
import pip
import subprocess
import os
   
class Program(QDialog, mainGui.Ui_Dialog):
    
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)
        self.setupUi(self)
        
        self.workerThread = WorkerThread()
        self.connect(self.updateButton, SIGNAL("clicked()"), self.getDists)
        self.connect(self.workerThread, SIGNAL("exception()"), self.threadDone)
        self.connect(self.quitButton, SIGNAL("clicked()"), self.exitApp)
        self.connect(self.workerThread, SIGNAL("changed(QString)"), self.updateLabel)
        self.connect(self.workerThread, SIGNAL("updateProgressbar(QString)"), self.updateProgressbar)
      
    #initializes the workerThread that does the upgrading   
    def getDists(self):
        self.workerThread.start()
        
    def updateLabel(self, text):
        self.label.setText(text)
        
    def updateProgressbar(self, val):
        self.progressBar.setValue(int(val))
        
    def threadDone(self):
        QMessageBox.warning(self, "Error", "Python not found! Please install it first.")      
      
    def exitApp(self):
        sys.exit(0)
        
class WorkerThread(QThread):
        
    def __init__(self, parent=None ):
                        
        super(WorkerThread, self).__init__(parent)
        
    def run(self):                      
        
        try:
           python_version = subprocess.check_output("Python --version")
           
           self.emit(SIGNAL("changed(QString)"), "Updating...")
            
           batcmd="pip freeze"
           dists = subprocess.check_output(batcmd)
            
           #converts the cmd output from a string to a list
           line = []
           for dist in dists:
               line.append(dist)
               s = ''.join(line)
    
            #there are some extra values in the captured output, like version numbers, "==", carriage returns.. We have to get rid of them like this:
           s = s.replace("\r","")
           s = s.split("==")
    
            #retrieves amount of installed dists for the progressbar                       
           counter = 0
           for i in s:
               if "\n" in i:
                   char_index = i.find("\n")
                   new_item = i[char_index + 1:]
                   if len(new_item) > 2:
                       counter = counter + 1            
            
            #go thru the list item by item, update them and the progressbar too
           valProgressbar = 0            
           percents = 100/counter
              
           for i in s:
               if "\n" in i:
                   char_index = i.find("\n")
                   new_item = i[char_index + 1:]
                   if len(new_item) > 2:
                       subprocess.call("pip install --upgrade " + new_item)
                       valProgressbar = valProgressbar + percents
                       self.emit(SIGNAL("updateProgressbar(QString)"), str(valProgressbar))
             
            #finalize the UI after updating           
           self.emit(SIGNAL("updateProgressbar(QString)"), str(100)) 
           self.emit(SIGNAL("changed(QString)"), "Finished!")
                
        except OSError as e:
            self.emit(SIGNAL("exception()")) 

app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()
