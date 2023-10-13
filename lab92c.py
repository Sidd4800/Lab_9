
# Online Python - IDE, Editor, Compiler, Interpreter
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
a = set(list1)
b = set(list2)
res= []
for i in a:
    if i in b:
        res.append(i)
print(res)        
        
