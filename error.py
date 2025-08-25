filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as f:
        content = f.read()
        print("File content successfully read:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
