import queue


def main():
    create_customers_queue()

def create_customers_queue():
    customers_queue = queue.Queue()

    while True:
        print(f"Customers currently in line: {customers_queue.qsize()}")
        if customers_queue.empty():
            decision = input("To add a customer to queue type 1: \nType 0 to exit the program: \n")
            if decision == "1":
                customers_queue.put(1)
            elif decision == "0":
                break
            else:
                print("Something went wrong!")

        elif not customers_queue.empty():
            new_decision = input(f"To add a customer to queue type 1: \nTo take customer from queue type 2: \nTo exit the program type 0: \n")
            if new_decision == "1":
                customers_queue.put(customers_queue.qsize() + 1)
            elif new_decision == "2":
                customers_queue.get()
            elif new_decision == "0":
                break
            else:
                print("Something went wrong!")

if __name__ == "__main__":
    main()