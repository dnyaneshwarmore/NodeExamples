# arr = list(map(int, input().split(" ")))
# print(arr)

# Fucking example of map

def square(n):
    return n**2


# arr  = list(map(square, [23,423,423424,324,2]))

arr  = list(map(lambda x : x**2, [23,423,423424,324,2]))
print(arr)
