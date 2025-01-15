def main():
    names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
    names = sorted(names, key=lambda name: len(name))
    print(names)


if __name__ == "__main__":
    main()