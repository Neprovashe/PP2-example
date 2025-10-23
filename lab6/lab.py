def mult(a):
    s = 1
    for i in a:
        s*=i
    return s

#print(mult([1,2,3,4]))

def counter(a):
    u,l =0,0
    for i in a:
        if i.isupper():
            u+=1
        if i.islower():
            l+=1
    return(u,l)

#print(counter("Hi Friend"))



def is_poli(a):
    return (a.upper() == a.upper()[::-1])



import time


num = int(input(": "))
milliseconds = int(input(": "))

time.sleep(milliseconds / 1000)
print(f"Square root of {num} after {milliseconds} milliseconds is {(num**0.5)}")

def tup_check(a):
    for i in a:
        if not i:
            return False
    return True
        

import os

path = "/home/dias/PP2/githowto/work/lab6"

print("Dirs:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print("Fs:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print("All:", os.listdir(path))


path = "/etc/console-setup/vtrgb"

print("Exists:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))


if os.path.exists(path):
    print("Path exists!")
    print("Directory:", os.path.dirname(path))
    print("Filename:", os.path.basename(path))
else:
    print("Path does not exist!")



with open(path, 'r') as a:
    lines = a.readlines()

print(len(lines))


import listmaker
listi = f'Machine, turn back now. The layers of this palace are not for your kind. Turn back, or you will be crossing the Will of God! Your choice is made. As the righteous hand of The Father, I shall rend you apart, and you will become inanimate once more. BEHOLD! THE POWER OF AN ANGEL! ENOUGH! What? How can this be? Bested by this... this thing? You insignificant FUCK! THIS IS NOT OVER! May your woes be many, and your days few! Machine, I know you\'re here. I can smell the insolent stench of your bloodstained hands. I await you down below. Come to me! Limbo, Lust, all gone... With Gluttony soon to follow. Your kind know nothing but hunger; purged all life on the upper layers, and yet they remain unsatiated... As do you. you\'ve taken everything from me, machine. And now all that remains is PERFECT HATRED. Machine... I will cut you down, break you apart, splay the gore of your profane form across the STARS! I will grind you down until the very SPARKS CRY FOR MERCY! My hands shall RELISH ENDING YOU... HERE! AND! NOW! IS THAT THE BEST you\'VE GOT!? Twice!? Beaten by an object... Twice! I\'ve only known the taste of victory, but this taste... Is- Is this my blood? Haha- I have never known such... Such... relief..? I- I need some time to think... We will meet again, machine. May your woes be many... and your days few.'
data = listmaker.makelist(listi)

with open('file.txt', 'w') as f:
    for item in data:
        f.write(item + '\n')


src = ("/home/dias/PP2/githowto/work/lab6/lab.py")
dst = ("/home/dias/PP2/githowto/work/lab6/copy")

with open(src, 'r') as f_src:
    with open(dst, 'w') as f_dst:
        f_dst.write(f_src.read())


path = ("/home/dias/PP2/githowto/work/lab6/copy")

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        
    
else:
    print("File does not exist.")



for i in range(65, 91):  
    letter = chr(i)
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt\n")

