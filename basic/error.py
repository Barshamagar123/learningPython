#try error exception
# a="barsha"
# try:
#     print(a)
# except NameError: 
#     print("you got error",NameError) 

# try:
#     print(a)
# except NameError:
#     print(NameError)
# except Exception as e:
#     print(e)
try:
    a=10+'barsha'
    print(a)
except Exception as e:
    print(e)