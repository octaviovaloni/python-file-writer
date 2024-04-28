from pathlib import Path

def ask_yn() -> bool:
    while True:
        response = input("y/n -> ")
        match response.lower():
            case "y":
                return True
            case "n":
                return False

def ask_in_range(min: int, max: int) -> int:
    while True:
        try:
            response = int(input())
            if response < min or response > max:
                print("Please enter a valid input")
            else:
                return response
        except:
            print("Please enter a valid input")

  
print("Python info save test")

save_files = list(Path(".").rglob("*.save"))
save_file = None
save_file_path = ""

# Loading files
if save_files:
    print("Old save files found, do you want to use one of them?")
    if ask_yn() == True:
        print("Select one of the files below: ")
        
        for index in range(len(save_files)):
            print(f"{index}: {save_files[index]}")
            
        save_file = save_files[ask_in_range(0, len(save_files) - 1)]
        try:
            save_file_path = save_file
            save_file = open(save_file, "a+")
        except:
            print("Problem ocurred while trying to open the save file.")
            exit()
        print("Save file opened successfully.")
        print(f"Save selected: {save_file.name}")
    else:
        file_name = input("File name: ")
        save_file = file_name + ".save"
        try:
            save_file_path = save_file
            save_file = open(save_file, "a+")
        except:
            print("Problem ocurred while trying to create the file.")
            exit()
        print("File created successfully.")
else:
    file_name = input("File name: ")
    save_file = file_name + ".save"
    try:
        save_file_path = save_file
        save_file = open(save_file, "a+")
    except:
        print("Problem ocurred while trying to create the file.")
        exit()
    print("File created successfully.")

# Reading and writing
print("Do you want to read or write? (y = write / n = read)")
response = ask_yn()

if response == True:
    while True:
        input_str = input("write -> ")
        if input_str == "":
            break
        save_file.write(input_str + "\n")
else:
    read_file = open(save_file_path, "r")
    print(read_file.read())

save_file.close()