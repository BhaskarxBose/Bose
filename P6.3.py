try:
    f=open("poem.txt","r")
    line=f.readline()
    myint=int(f.strip())
    mcv=101/myint
except IOError:
    print("I/O error occured")
except ValueError:
    print("Could not convert data to an integer")
except ZeroDivisionError:
    print("Division by zero Error!")
except:
    print("Unexpected Error!")
else:
    print("Hurray!. No Exceptions")
