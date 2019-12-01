# 
# def a():
    # print("inside the module a");
# 
# a()


def checkIsPalindrome(mystring):
    i , j = 0  , len(mystring)-1;
    while(i<=j):
        if (mystring[i]!=mystring[j]):
            break
        i+=1
        j-=1
    return i>j

print(checkIsPalindrome(""))
