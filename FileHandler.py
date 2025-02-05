class FileHandler:
    def __init__(self, file_path):
        # Store the file path in an instance variable
        self.file_path = file_path

    def read_file(self):
        try:
            # Open the file in read mode and print its contents
            with open(self.file_path, 'r') as file:
                content = file.read()
                print("File Content:")
                print(content)
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"Error: {str(e)}")


# Example of passing the file path via constructor
file_path = "example.txt"  # Replace with your actual file path
file_handler = FileHandler(file_path)

# Calling the method to read the file
file_handler.read_file()
