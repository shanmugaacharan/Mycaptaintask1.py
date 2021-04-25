def most_frequent(a):
    r={}
    for k in a:
        r[k]=r.get(k,0)+1
    print(r)
test_str=input(print("Please enter the string:"))
most_frequent(test_str)
