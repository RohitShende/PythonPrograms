# How is exception handling done in python

try:
    raise Exception
except:
    pass
finally:
    pass


try:
    # create a file and write the list to it
    list_of_numbers = ["HI,", "This is line 1", "This is line 2", "This is line 3"]
    my_file_writer = open("my_file.txt", 'w')
    print("writing to a file...")
    my_file_writer.write("\n".join(list_of_numbers))
    print("\n =============== File Writing Successful !!! ======================")
except Exception as e:
    print("An exception occurred while writing- ", e)
    raise e

finally:
    my_file_writer.close()


# now read that file which you created and print the contents of the file

try:
    my_file_reader = open("my_file.txt")
    lines = my_file_reader.readlines()

    print("\nThe file consists :\n")
    for line in lines:
        print(line, end='')
    print("\n\n ================ File Reading Successful !!! ======================\n\n")
finally:
    my_file_reader.close()


# using "with" keyword to handle closing
with open("my_file.txt") as my_file_reader:
    lines = my_file_reader.readlines()
    print("\nThe file consists :\n")
    print(*lines, end='', sep='')
    print('\n\n ================ File Reading Successful using "with" Keyword !!! ======================')
