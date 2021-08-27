from core.address_book.address_book import AddressBook
from core.note_book.note_book import NoteBook
from core.sort_manager.sort_manager import SortManager
from core.context_analyzer.context_analyzer import ContextAnalyzer

if __name__ == "__main__":
    address_book = AddressBook()
    note_book = NoteBook()
    sort_manager = SortManager()
    context_analyzer = ContextAnalyzer()

    while True:
        user_request = input(">>> : ")
        responsible_module, command, user_data = context_analyzer.analyze(user_request)
        if responsible_module == AddressBook:
            if command:
                answer = command(address_book, user_data)
            else:
                answer = "Wrong command for AddressBook module."
        elif responsible_module == NoteBook:
            if command:
                answer = command(note_book, user_data)
            else:
                answer = "Wrong command for NoteBook module."
        elif responsible_module == SortManager:
            if command:
                answer = command(sort_manager, user_data)
            else:
                answer = "Wrong command for SortManager module."
        elif responsible_module == "main":
            if command == "off":
                print("Good bye!")
                break
            else:
                answer = "Wrong command for Main module."
        else:
            answer = "Can not understand what you mean."

        print(answer)





