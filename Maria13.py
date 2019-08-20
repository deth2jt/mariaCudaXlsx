#import math

class Maria13:
    IMP0=''
    IMP0F1=''
    IMP0F2=''
    IMP0F3=''
    IMP0F4=''
    IMP0F5=''
    IMP0F6=''


    IMP0F7=''
    IMP0F8=''
    
    IMP0F9=''
    IMP0F10=''

    
    IMP1=''
    IMP1F1=''
    IMP1F2=''
    IMP1F3=''

    IMP1F4=''
    IMP1F5=''
    
    IMP2=''
    IMP2F1=''
    IMP2F2=''
    IMP2F3=''

    IMP2F4=''
    IMP2F5=''

    IMP0LEN = 0
    IMP1LEN = 0
    IMP2LEN = 0

    delimiter = '\t'

    
##    def __init__(self,IMP0,IMP0F1,IMP0F2,IMP0F3,IMP0F4,IMP0F5,IMP0F6, IMP1,IMP1F1,IMP1F2,IMP1F3,IMP2,IMP2F1,IMP2F2, IMP2F3):
##        self.IMP0=IMP0
##        self.IMP0F1=IMP0F1
##        self.IMP0F2=IMP0F2
##        self.IMP0F3=IMP0F3
##        self.IMP0F4=IMP0F4
##        self.IMP0F5=IMP0F5
##        self.IMP0F6=IMP0F6
##
##      
##
##        
##        self.IMP1=IMP1
##        self.IMP1F1=IMP1F1
##        self.IMP1F2=IMP1F2
##        self.IMP1F3=IMP1F3
##        self.IMP2=IMP2
##        self.IMP2F1=IMP2F1
##        self.IMP2F2=IMP2F2
##        self.IMP2F3=IMP2F3


    def __init__(self,IMP0,IMP0F1,IMP0F2,IMP0F3,IMP0F4,IMP0F5,IMP0F6, IMP0F7, IMP0F8, IMP1,IMP1F1,IMP1F2,IMP1F3,IMP2,IMP2F1,IMP2F2, IMP2F3):
        self.IMP0=IMP0
        self.IMP0F1=IMP0F1
        self.IMP0F2=IMP0F2
        self.IMP0F3=IMP0F3
        self.IMP0F4=IMP0F4
        self.IMP0F5=IMP0F5
        self.IMP0F6=IMP0F6

        self.IMP0F7=IMP0F7
        self.IMP0F8=IMP0F8


        
        self.IMP1=IMP1
        #print "self.IMP1", self.IMP1
        
        self.IMP1F1=IMP1F1
        self.IMP1F2=IMP1F2
        self.IMP1F3=IMP1F3


        
        self.IMP2=IMP2
        self.IMP2F1=IMP2F1
        self.IMP2F2=IMP2F2
        self.IMP2F3=IMP2F3

    def setIMPLENS(self, IMP0LEN, IMP1LEN, IMP2LEN):
        self.IMP0LEN = IMP0LEN
        self.IMP1LEN = IMP1LEN
        self.IMP2LEN = IMP2LEN

        
    def setIMP0LEN(self, val):
        self.IMP0LEN = val

    def setIMP1LEN(self, val):
        self.IMP1LEN = val

    def setIMP2LEN(self, val):
        self.IMP2LEN = val
   
    def __str__(self):
        delimiter = '\t'
        return self.IMP0 + delimiter + self.IMP0F1 + delimiter + self.IMP0F2 + delimiter + self.IMP0F3  + delimiter + self.IMP0F4 + delimiter + self.IMP0F5 + delimiter  + self.IMP0F6 + delimiter + self.IMP0F7 + delimiter + self.IMP0F8 + delimiter + self.IMP1 + delimiter + self.IMP1F1 + delimiter + self.IMP1F2 + delimiter + self.IMP1F3 + delimiter + self.IMP2 + delimiter + self.IMP2F1 + delimiter + self.IMP2F2 + delimiter + self.IMP2F3
            

    def setIMP1ToBlank(self):
        self.IMP1=''
        self.IMP1F1=''
        self.IMP1F2=''
        self.IMP1F3=''
        self.IMP1F4=''
        self.IMP1F5=''

    def setIMP2ToBlank(self):
        self.IMP2=''
        self.IMP2F1=''
        self.IMP2F2=''
        self.IMP2F3=''
        self.IMP2F4=''
        self.IMP2F5=''


    def setIMP1(self, IMP1,IMP1F1,IMP1F2,IMP1F3):
        self.IMP1=IMP1
        self.IMP1F1=IMP1F1
        self.IMP1F2=IMP1F2
        self.IMP1F3=IMP1F3

    def setIMP1(self, IMP1,IMP1F1,IMP1F2,IMP1F3,IMP1F4):
        self.IMP1=IMP1
        self.IMP1F1=IMP1F1
        self.IMP1F2=IMP1F2
        self.IMP1F3=IMP1F3
        self.IMP1F4=IMP1F4

    def setIMP1(self, IMP1,IMP1F1,IMP1F2,IMP1F3,IMP1F4,IMP1F5):
        self.IMP1=IMP1
        self.IMP1F1=IMP1F1
        self.IMP1F2=IMP1F2
        self.IMP1F3=IMP1F3
        self.IMP1F4=IMP1F4
        self.IMP1F5=IMP1F5

    def setIMP2(self,IMP2,IMP2F1,IMP2F2, IMP2F3):
        self.IMP2=IMP2
        self.IMP2F1=IMP2F1
        self.IMP2F2=IMP2F2
        self.IMP2F3=IMP2F3

    def setIMP2(self,IMP2,IMP2F1,IMP2F2, IMP2F3, IMP2F4):
        self.IMP2=IMP2
        self.IMP2F1=IMP2F1
        self.IMP2F2=IMP2F2
        self.IMP2F3=IMP2F3
        self.IMP2F4=IMP2F4

    def setIMP2(self,IMP2,IMP2F1,IMP2F2, IMP2F3, IMP2F4, IMP2F5):
        self.IMP2=IMP2
        self.IMP2F1=IMP2F1
        self.IMP2F2=IMP2F2
        self.IMP2F3=IMP2F3
        self.IMP2F5=IMP2F5

        

    def getIMP0List(self):
        if(self.IMP0LEN == 8):
            return [self.IMP0 ,self.IMP0F1,self.IMP0F2,self.IMP0F3,self.IMP0F4,self.IMP0F5,self.IMP0F6, self.IMP0F7, self.IMP0F8]
        elif(self.IMP0LEN == 7):
            return [self.IMP0 ,self.IMP0F1,self.IMP0F2,self.IMP0F3,self.IMP0F4,self.IMP0F5,self.IMP0F6, self.IMP0F7]
        else:
            return [self.IMP0 ,self.IMP0F1,self.IMP0F2,self.IMP0F3,self.IMP0F4,self.IMP0F5,self.IMP0F6]

    def getIMP1List(self):
        if(self.IMP1LEN == 5):
            return [self.IMP1,self.IMP1F1,self.IMP1F2,self.IMP1F3, self.IMP1F4, self.IMP1F5]
        elif(self.IMP1LEN == 4):
            return [self.IMP1,self.IMP1F1,self.IMP1F2,self.IMP1F3, self.IMP1F4]
        else:
            return [self.IMP1,self.IMP1F1,self.IMP1F2,self.IMP1F3]

    def getIMP2List(self):
        if(self.IMP2LEN == 5):
            return [self.IMP2,self.IMP2F1,self.IMP2F2, self.IMP2F3, self.IMP2F4, self.IMP2F4]
        elif(self.IMP2LEN == 4):
            return [self.IMP2,self.IMP2F1,self.IMP2F2, self.IMP2F3, self.IMP2F4]
        else:
            return [self.IMP2,self.IMP2F1,self.IMP2F2, self.IMP2F3]


    def getIMP0LEN(self):
        return self.IMP0LEN

    def getIMP1LEN(self):
        return self.IMP1LEN

    def getIMP2LEN(self):
        return self.IMP2LEN
    

        
    def getIMP0(self):
        return self.IMP0

    def getIMP1(self):
        return self.IMP1

    def getIMP2(self):
        return self.IMP2

    
