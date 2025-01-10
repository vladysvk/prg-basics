def main():
    e_book = EBOOK("Algorithms", "Me", "250")
    e_book.open()
    e_book.display_status()
    e_book.next_page()
    e_book.next_page()
    e_book.next_page()
    e_book.next_page()
    e_book.next_page()
    e_book.next_page()
    e_book.next_page()
    e_book.display_status()
    e_book.close()
    e_book.display_status()
    e_book.next_page()
class EBOOK:
    def __init__(self, title, author, pages_count):
        self.is_open = False
        self.title = title
        self.author = author
        self.pages_count = pages_count
        self.current_page = 0

    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
    
    def next_page(self):
        if self.is_open:
            self.current_page+=1

    def previous_page(self):
        if self.is_open and self.current_page > 0:
            self.current_page-=1

    def display_status(self):
        if self.is_open:
            print(f"Book is open, title: {self.title}, author: {self.author}, number of pages: {self.pages_count}, current page: {self.current_page}")

if __name__ == "__main__":
    main()