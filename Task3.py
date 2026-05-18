from datetime import datetime
import os

def load_file():
    while True:
        file_path = input("Please enter the file path: ")
        try:
            with open(file_path, "r") as file:
                read_file = file.read()
            break
        except:
            print("File not found. Please enter a valid file path.")
    return read_file, file_path

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

def last_modified(file_path):
    mod_date = os.path.getmtime(file_path)
    return datetime.fromtimestamp(mod_date)


def start():
    print("Welcome to file reporter")
    file, file_path = load_file()
    print("How can we help?\n1. Words and line count\n2. The frequency of a word\n3. Show file report\n4. Preview file\n5. Last modification date")

    while True:
        service = input("Please enter the service number: ")
        try: 
            int(service) and service in ["1", "2", "3", "4", "5"]
            break
        except:
            print("Please enter a valid service number within 1, 5.")

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
    elif service == "5":
        print(f"The last modification date is: {last_modified(file_path)}")
    
start()
print("Thanks for using file reporter!!")
