def main():
    paragraph = "cat dog mouse cat rat cat mouse"
    dictionary = count(paragraph)
    print_dict(dictionary)

def count(paragraph):
    count_dict = {}
    paragraph = paragraph.split(" ")
    for word in paragraph:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(key + ":", value)

if __name__ == "__main__":
    main()