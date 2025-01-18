def read_and_modify_file():
    import os

    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as file:
            content = file.readlines()

        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]

        output_filename = input("Enter the name of the file to save the modified content: ")

        with open(output_filename, 'w') as file:
            file.writelines(modified_content)

        print(f"File successfully written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("thankyou glad to have you again")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
