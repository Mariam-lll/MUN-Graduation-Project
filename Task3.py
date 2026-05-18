
def load_file():
    while True:
        file_path = input("Please enter the file path: ")
        try:
            with open(file_path, "r") as file:
                read_file = file.read()
            break
        except:
            print("File not found. Please enter a valid file path.")
    return read_file

def words_lines(file):
    words = file.split()
    words_no = len(words)
    lines_no = file.count("\n")
    return words_no, lines_no

def count_specific(text, file):
    return file.count(text)

def file_report(file):
    words, lines = words_lines(file)
    print(f"~File report~\nWords count: {words}\nLines count: {lines}\nNumber of characters: {len(file)}")


def start():
    print("Welcome to file reporter")
    file = load_file()
    print("How can we help?\n1. Words and line count\n2. The frequency of a word\n3. Show file report\n4. Preview file")

    while True:
        service = input("Please enter the service number: ")
        try: 
            int(service) and service in ["1", "2", "3", "4"]
            break
        except:
            print("Please enter a valid service number within 1, 4.")

    if service == "1":
        words, lines = words_lines(file)
        print(f"Words count: {words}\nLines count: {lines}")
    elif service == "2":
        text = input("Enter the specified text: ")
        print(f"The frequency of the word {text} is: {count_specific(text, file)}")
    elif service == "3":
        file_report(file)
    elif service == "4":
        print(file)
start()

