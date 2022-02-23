class Menu:
    def __init__(self):
        self.filename="d:/menu.txt"
        self.menu=[]
    def fileRead(self):
        f=open(self.filename,"r")
        for line in f.readlines():
            item=line.split(',')
            dict={}
            dict['name']=item[0]
            item[1]=item[1].replace("\n","")
            dict['price']=int(item[1])
            self.menu.append(dict)
        f.close()
        
    def menu_display(self):
        menu_num=1
        for dict in self.menu:
            print(menu_num,dict['name'],dict['price'])
            menu_num+=1
    def fileWrite(self):
        f=open(self.filename,"w")
        for dict in self.menu:
            f.write(dict['name']+","+str(dict['price'])+"\n")
        f.close()
        
    def addNew(self):
        name=input("메뉴명을 입력하세요")
        price=int(input("가격을 입력하세요"))
        dict={}
        dict['name']=name
        dict['price']=price
        self.menu.append(dict)
    def update(self):
        n=int(input("메뉴번호를 입력하세요"))
        name=input("메뉴명을 입력하세요")
        price=int(input("가격을 입력하세요"))
        self.menu[n-1]['name']=name
        self.menu[n-1]['price']=price
    def delete(self):
        n=int(input("메뉴번호를 입력하세요"))
        del self.menu[n-1]




m=Menu()
# m.fileRead()
# m.menu_display()
a=input('작업을 선택하세요(C:추가,U:수정,D:삭제,X:종료)')
while a!='X':
      if a=='C':
        m.addNew()
      elif a=='U':
        m.update()
      elif a=='D':
          m.delete()
      m.menu_display()
      a=input('작업을 선택하세요(C:추가,U:수정,D:삭제,X:종료)')
m.fileWrite()