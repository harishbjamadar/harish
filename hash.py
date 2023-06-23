import time
start=time.time()
int_val = 4
str_val = 'GeeksforGeeks'
flt_val = 24.56
print("the integer hash value is :"+ str(hash(int_val)))
print("the integer hash value is :"+ str(hash(str_val)))
print("the integer hash value is :"+ str(hash(flt_val)))
end=time.time()
print(f"the runtime of the program is {end-start}")
