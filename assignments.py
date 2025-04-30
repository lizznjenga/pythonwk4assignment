def modify_content(content):
    
    return content.upper()

def main():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except IOError:
        print(f"Error: Could not read the file '{input_filename}'.")
        return

    modified_content = modify_content(content)

    output_filename = input("Enter the name of the file to write the modified content to: ")
    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content successfully written to '{output_filename}'.")
    except IOError:
        print(f"Error: Could not write to the file '{output_filename}'.")

if __name__ == "__main__":
    main()
