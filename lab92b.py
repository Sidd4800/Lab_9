
# Online Python - IDE, Editor, Compiler, Interpreter
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
x = set(l1)
y = set(l2)
z = x.difference(y)
a = x.symmetric_difference(y)
print(z)
print(a)
