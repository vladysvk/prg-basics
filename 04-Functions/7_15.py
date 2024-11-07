def main():
    print(f("+-+-+-+-"))

def f(detector):
    count = 0
    for i in detector:
        if i == "+":
            count += 1
            if count == 3:
                return True
        elif i == "-":
            count -= 1
    return False

if __name__ == "__main__":
    main()