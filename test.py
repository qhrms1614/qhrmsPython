# i=0
# while i<9:
#     i=i+1
#     print(5*i)
# print("program ended") //while 5단

# i=1
# while i<9:
#     i+=1
#     j=0
#     while j<9:
#         j+=1
#         print(i,'x',j,'=',i*j) //while 구구단
    
# for x in range(1,10,1):
#     for y in range(1,10):
#         print(x,'x',y,'=',x*y)  // range 구구단

# 홀수 99까지 추가해서 리스트 생성 /w for

# l=[]
# for x in range(1,100,2):
#     l.append(x)
# print(l)
    
# while True:
#     for x in range(11):
#         print(' '*x,'*')
#         if x==10:
#             for x in range(10,-1,-1):
#                 print(' '*x,'*')

# def doMulti (a,b):
#     return a*b
# for i in range(2,10):
#     for j in range(1,10):
#         print(i,"x",j,"=",doMulti(i,j))
# def plus(a,b):
#     return a+b
# a=1
# b=0
# c=plus(a,b)
# while(c<1000):
#     print(plus(a,b))
#     a=b
#     b=c
#     c=plus(a,b)

# def plus(*param): #포인터 (여러개 넣을수있음/가변 매개변수)
#    sum=0
#    for x in param:
#        sum+=x
#    return sum
# n=plus(1,2,3,4,5)
# print(n)
   

# n=int(input('값을 넣으시오.')) #항상 '문자열'을 반환한다
# print(n**2,n,end='')
# print("terminated")

# m=input('값을 넣으시오')
# print(int(n))

#write,append
f=open("d://menu1.txt","a") #만들기
# r:read -> 읽기 전용
# w:write -> 기존 데이터 모두 날리고 새로 쓰기
# a:append -> 기존 데이터 유지하고 추가쓰기
f.write("시험용4 줄바꿈입니다\n")
for line in f.readlines(): # 해당 파일에 있는 내용 출력하기
    print(line)
f.close()