#res = 0
#def division(a,b):
#    res = 0
#    try:
#        res = a/b
#    except:
#        try:
#            a = int(a)
#            b = int(b)
#            res = a / b
#        except ZeroDivisionError:
#            res = 0
#        except ValueError:
#            res = "Enter number"
#    print(res)
#res = division.res
#while division.res == 0:
#    division(input("a ="),input("b ="))d
x = 15
try:
    print(x)
except:
    print("Something went wrong")
else:
    print("Else program do")
finally:
    print("The program has completed its work")