def modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            content = f.read()
        modified_content = content.upper()
        with open(output_file, 'w') as f:
            f.write(modified_content)
        print(f"Modified file has been saved as '{output_file}'")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

modify_file("input.txt", "output.txt")
