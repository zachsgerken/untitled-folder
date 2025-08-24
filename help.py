#Zach Gerken
#Chapter 8 Lab 2
#October 30 2022

#print statement
print("File Processor")
print()

#get name of file you want to open
def main():
    try:
        file = input("Enter the name of the file you wish to process: ")
        my_file = open((file), 'r', encoding='utf-8')
        file_string = my_file.read()
        words = file_string.split()
        word_list(words, file)
    except(FileNotFoundError, NameError):
        print('ERROR')
        main()

# start accumulators for how many words in file as well as capital words
# for loop to put in list then if statement to remove hyphen
def word_list(words, file):
    word_count = 0
    capital_count = 0
    list = []
    for line in words:
        list.append(line)
        if "–" in list:
            list.remove(line)
        else:
            word_count += 1
            if line[0].isupper():
                capital_count += 1
    printcapital(file, word_count, capital_count)


#print statement that is passed filename, word count and capital count
def printcapital(file, word_count, capital_count):
    print("The file", file,"contains", word_count,"words of which", capital_count, "of them are capitalized.")

main()