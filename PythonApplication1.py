#data = ['a','b','c',['abcd','afg']]

#print (data[0]) #data에서 처음의 데이타
#print (data[-1]) #data에서 마지막의 데이타

#a = []
#b = [1,2,3]
#c = ['Life','is','too','short']
#d = [1,2,'Life','is']
#e = [1,2,['Life','is']]

#print(b+c)
#print(b*3)

#g = ['a','b','c','d']

#g[0] = 'greenjoa'
#g[1] = ['greenjoa1','greenjoa2']
#g[1:2] = ['greenjoa1','greenjoa2']

#print(g[0])
#print(g[1])
#print(g[1:2])

#g.insert(2,'e')
#g.append('greenjoa2')
#print(g[-1])
#print(g[2])

#data = ['greenjoa1','greenjoa2','greenjoa3']
#data.insert(1,123) #data의 처음 데이타 뒤에 123 삽입
#data.insert(3,234) #data의 두번째 데이타 뒤에 123 삽입
#data.insert(5,345) #data의 세번째 데이타 뒤에 123 삽입

#print(data)

#guests = ['a','b','c','d']

#for steps in range(4):
#    print(guests[steps]) #데이타안의 0,1,2,3 번째의 데이타를 수출
#    print(steps) #데이타 주소를 수출

#nEntries = len(guests) #데이타 길이를 모를 때
#for steps in range(nEntries):
#    print(guests[steps])

#for guests in guests:
#    print(guests)

scores = [85,62,63,45,90]
#scores.sort() #
scores.reverse()

print(scores)