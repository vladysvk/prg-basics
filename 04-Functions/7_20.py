def main():
    print(f(5))

def f(n):
    count = 1 
    num = 2  
    while count <= n:  
        for i in range(2, num):
            if num % i == 0:  
                break
        else:  
            count += 1  
        num += 1 
         
    
    return num - 1

if __name__ == "__main__":
    main()