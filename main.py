import menu

m=menu.Menu()
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
print("프로그램 종료")