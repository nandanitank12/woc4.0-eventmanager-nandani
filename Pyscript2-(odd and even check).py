import numpy as np

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

print("### True:number is even\n"

      "\tfalse:number is odd ###")
# Boolean Masking
numbool = filedata % 2 == 0

print(numbool)
