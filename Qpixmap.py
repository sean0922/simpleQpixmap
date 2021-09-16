from PyQt5.Qt import (QWidget, QHBoxLayout, QLabel, QApplication)                                                                          
from PyQt5.QtGui import QPixmap                                                                                                            
import sys                                                                                                                                 

class Example(QWidget):                                                                                                                    
    def __init__(self):                                                                                                                    
        super().__init__()                                                                                                                 
        self.initUI()                                                                                                                      

    def initUI(self):                                                                                                                      
        hbox = QHBoxLayout(self)                                                                                                           
        #pixmap = QPixmap("C:\\Users\Others\Desktop\cat.png")         
        pixmap = QPixmap("cat.png")                                                                                                    

        lbl = QLabel(self)                                                                                                                 
        lbl.setPixmap(pixmap)                                                                                                              

        hbox.addWidget(lbl)                                                                                                                
        self.setLayout(hbox)                                                                                                               

        self.move(300, 200)                                                                                                                
        self.setWindowTitle('Image with PyQt')                                                                                             
        self.show()                                                                                                                        

if __name__ == '__main__':                                                                                                                 

    app = QApplication(sys.argv)                                                                                                           
    ex = Example()                                                                                                                         
    sys.exit(app.exec_())  

