def second_largest(arr):
    arr = sorted(arr)
    return arr[-2]


def difference(arr):
    return sorted(arr)[-1] - sorted(arr)[0] 

def median(arr):
    if len(arr) % 2 == 0:
        median_num = (arr[len(arr//2)] + arr[len(arr//2)+1])/2
    else:
        return arr[len(arr)//2]
    
def smallest_and_largest(arr):
    return [sorted(arr)[0], sorted(arr)[-1]]

def separated(arr):
    string = f"{arr[0]}"

    for i in range(1, len(arr)):
        string += f"-{arr[i]}"
    return string