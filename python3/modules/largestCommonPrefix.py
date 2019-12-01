def largestcommon(prefix, string):
    # print(prefix, " " , string)
    l1 = len(prefix)
    l2 = len(string)
    i =0
    j=0
    cmn = ""
    while (i<l1 and j<l2):
        if (prefix[i]!=string[j]):
            break

        cmn+=prefix[i]
        i+=1
        j+=1
    print(prefix)
    return prefix

def largestCommonPrefix(arr):
    prefix = arr[0]
    for i in range(1, len(arr)):
        prefix = largestcommon(prefix, arr[i])
    return prefix

def main():
    arr  = ["application", "apple", "apps", "apache"]
    result = largestCommonPrefix(arr)
    print(result)



main()