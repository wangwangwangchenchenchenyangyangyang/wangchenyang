import os
######functions########
def printer(words):
	print(words)
#######################
word = input("file:")

os.system("cd "+word)
print("cd "+word)
word = input("name:")
os.system("g++ "+word)
print("g++ "+word)
word = input("b:")
os.system(".\\" + word)
print(".\\" + word)