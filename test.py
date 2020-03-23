squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print('最小的数是：%s'%min(squares))
print(max(squares))
print(sum(squares))
print(squares)