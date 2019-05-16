# -*- coding: utf-8 -*-
class human:
    def __init__(self,name):
        self.age =1
        self.name=name
        #__開頭的instance屬性，會自動視為private(私有的)
        #_開頭的instance屬性，會自動視為protected(保護的)
        # 開頭的instance屬性，會自動視為public(公有的)
        #以上定義皆需要工程師自己去練感覺，因為python沒有強制性
        #就算是__開頭的instance屬性，也可以透過某方式強制更改
        self.__nickname="bear"
    def setAge(self,age):
        if age<=0:
            print("沒有人年紀小於0的啦!!!")
            return
        self.age=age
    
    def setName(self,name):
        if name==0:
            print("尚未取名......")
            return
        self.name=name
         
    def showAge(self):
        print(self.age)        
        
    def showName(self):
        print("My name is",self.name," , Nickname is",self.__nickname)  
        
h1=human("Petter")
h1.showAge()
h1.setAge(-18)
h1.showAge()
h1.setName("John")
h1.showName()
print(__Nickname)
h1.__Nickname="Ketty"
print(__Nickname)
h1.showName()
