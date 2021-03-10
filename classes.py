class Human:
    def __init__(self,n,o) :
        self.name=n
        self.occupation=o
    def dowork(self):
        if self.occupation=='Player':
            print(self.name,"IS very good player")
        elif self.occupation=="Dancer":
            print(self.name,"IS a amezing dancer")
        else:
            print(self.name,"is simple person having general life")

A=Human("Akash","Player")
A.dowork()


    
        