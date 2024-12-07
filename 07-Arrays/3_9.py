def main():
    if compare(array1, array2):
        print("arrays are the same")
    else:
        print("arrays are not the same")
    if compare(array3, array4):
        print("arrays are the same")
    else:
        print("arrays are not the same")
    if compare(array5, array6):
        print("arrays are the same")
    else:
        print("arrays are not the same")
    if compare(array7, array8):
        print("arrays are the same")
    else:
        print("arrays are not the same")

def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    else:
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                return False
        return True
    
array1, array2 = ["water","book","sky"],["water","book","sky"]
array3, array4 = [True,False],[True,False,True]
array5, array6 = [5,3,1],[5,3,1]
array7, array8 = [3,2,1],[3,2]
    
if __name__ == "__main__":
    main()