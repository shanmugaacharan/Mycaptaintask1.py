def reverse(a):
    r={}
    for k in a:
        r[k]=r.get(k,0)+1
    print(r)
test_str=input(print("Please enter the string:"))
reverse(test_str)
