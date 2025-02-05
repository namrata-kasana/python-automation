import argparse

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                print("File Content:")
                print(content)
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"Error: {str(e)}")


# Setting up the command line argument parser
def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a file path.")
    parser.add_argument("file_path", type=str, help="Path to the file you want to read")
    return parser.parse_args()


# Main script
if __name__ == "__main__":
    # Parse arguments from the command line
    args = parse_arguments()

    # Create a FileHandler object with the file path from the command line argument
    file_handler = FileHandler(args.file_path)

    # Call the read_file method
    file_handler.read_file()
