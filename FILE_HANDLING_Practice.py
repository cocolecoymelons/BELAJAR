
while True:
    decision = input("""

            1. Write Note
            2. Read Note
            3. Delete specific Note content
            4. Clear Note contents
            5. Make a new Note 
            6. Exit

""")
    try:
        if decision == '1':
            choose_file_to_write = input("Choose file:\n")
            with open(choose_file_to_write, "a") as note:
                input_note = input("Write:" + '\n')
                note.write(input_note + "\n")
                print("Success.")
        elif decision == '2':
            choose_file_to_read = input("Choose file:\n")
            with open(choose_file_to_read, "r") as note:
                print(note.read())

        elif decision == '3':
            choose_file_to_be_deleted3 = input("Choose file:\n")

            with open(choose_file_to_be_deleted3, "r") as note:

                list_note_tobe_deleted = note.read().splitlines()
                print(list_note_tobe_deleted)

                note_tobe_deleted = int(input("Write the note index you want to delete(index start from 0):\n"))

                if note_tobe_deleted < 0 or note_tobe_deleted > len(list_note_tobe_deleted) - 1:
                    raise IndexError

                else:
                    list_note_tobe_deleted.pop(note_tobe_deleted)
                    with open(choose_file_to_be_deleted3,"w") as note:
                        for i in list_note_tobe_deleted:
                            note.write(i + "\n")

                        print("Success.")

        elif decision == '4':
            note_file_tobe_deleted = input("Choose the file to be deleted:\n")
            with open(note_file_tobe_deleted,"w") as note:
                pass
            print("Clear Note contents success.")

        elif decision == '5':
            new_file_name = input("Input file name: ")
            with open(new_file_name,"w") as note:
                print("Create a new file success.")
                    
        elif decision == '6':
            print("See you next time!")
            break

        else:
            print("Invalid Menu.")

    except ValueError:
        print("Please input a number!")
    except FileNotFoundError:
        print("There is no notes available!")
    except IndexError:
        print("Index out of range!")
            