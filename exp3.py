# python <fil1> <fil2> ...
import sys,os

print(sys.argv)
print(sys.argv[1:])

for filename in sys.argv[1:]:
        if os.path.isdir(filename):
            print("Directory!")
        elif os.path.isfile(filename):
            print("File!")
        else:
            print("Annat!")

with open('fibo.py',"rb") as f:
            data = f.read() # ger filens innehall
print(data)


"""   kommentar
        with open(filename, "rb") as f:
            data = f.read()
        if b'\0' in data:
            print(filename, "Binary!")
            continue
        newdata = data.replace(b"\r\n", b"\n")
        if newdata != data:
            print(filename)
            with open(filename, "wb") as f:
               f.write(newdata)
"""
pass
print('SLUT!')
sys.stdin.readline()
