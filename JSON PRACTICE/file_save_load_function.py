import json

def save_file(targetted_file,the_file):
    with open(targetted_file, "w") as file:
        json.dump(the_file, file, indent=4)

def load_file(targetted_file):
    try:
        with open(targetted_file,"r") as file:
            print("Loading the file.....")
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Ooops... You don't have the needed file! Making a new one...")
        with open(targetted_file,"w") as file:
            json.dump([], file)
            print("Please re-run the program. Thank you!")

            return []