def file_to_list(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into a list based on commas and newline characters
    file_labels_list = [item.strip() for item in content.split(',\n')]

    return file_labels_list

def main():
    # Get the directory of the file containing the set of emotions
    file_path = input("Enter the directory of the file containing the set of emotions: ")

    try:
        # Convert the content of the file to a list
        file_labels_list = file_to_list(file_path)

        # Print the resulting list
        print("List of emotions:")
        print(file_labels_list)
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")

if __name__ == "__main__":
    main()
