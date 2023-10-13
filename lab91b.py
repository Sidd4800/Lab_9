
# Online Python - IDE, Editor, Compiler, Interpreter
input_str = input("Write the numbers separated by spaces: ")
input_list = list(map(int,input_str.split()))

print("The original list is: " + str(input_list))

result_set = set()
result_list = []
for i in input_list:
    if i not in result_set:
        result_list.append(i)
        result_set.add(i)
        
print("final list: " +str(result_list))    
    

