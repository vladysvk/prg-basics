def main():
    print(f("Internet of Things"))
    

def f(name):
    name_list = name.split(" ")
    new_name = ""
    for i in name_list:
        new_name += i[0]
    return new_name

if __name__ == "__main__":
    main()