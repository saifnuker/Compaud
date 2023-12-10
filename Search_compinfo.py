# search_compinfo.py

def retrieve_info(file_path, key, value):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            found = False
            for i in range(0, len(lines), 6):  # Each entry has 6 lines (5 info lines + 1 blank)
                info = lines[i:i+5]
                if key == 'name' and value.lower() in info[0].lower():
                    print("".join(info))
                    found = True
                    break
                elif key == 'ip' and value.lower() in info[1].lower():
                    print("".join(info))
                    found = True
                    break
                elif key == 'location' and value.lower() in info[2].lower():
                    print("".join(info))
                    found = True
                    break
                elif key == 'os' and value.lower() in info[3].lower():
                    print("".join(info))
                    found = True
                    break
                elif key == 'version' and value.lower() in info[4].lower():
                    print("".join(info))
                    found = True
                    break

            if not found:
                print(f"No entry found for {key.capitalize()}: {value}")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    file_path = r'computer_audit.txt'

    key = input("Enter the information category (name, ip, location, os, version): ").lower()
    value = input(f"Enter the {key.capitalize()} to search for: ")

    retrieve_info(file_path, key, value)