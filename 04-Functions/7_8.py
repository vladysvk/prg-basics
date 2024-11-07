def main():
    print(f(8))


def f(amount_to_pay):
    count = 0
    while amount_to_pay > 0:
        if amount_to_pay >= 5:
            amount_to_pay-=5
            count+=1
        elif amount_to_pay >=2:
            amount_to_pay-=2
            count+=1
        else:
            amount_to_pay-=1
            count+=1 
    return count

if __name__ == "__main__":
    main()