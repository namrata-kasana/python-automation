class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.readlines()
                return content
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"Error: {str(e)}")
        return []

    def search_and_filter(self, search_term):
        # Read the file content
        lines = self.read_file()

        # Filter lines containing the search term (case-insensitive search)
        if lines:
            filtered_lines = [line for line in lines if search_term.lower() in line.lower()]
            return filtered_lines
        return []

    def display_filtered_lines(self, search_term):
        filtered_lines = self.search_and_filter(search_term)
        if filtered_lines:
            print(f"Lines containing '{search_term}':")
            for line in filtered_lines:
                print(line.strip())  # .strip() to remove any extra newlines
        else:
            print(f"No lines found containing '{search_term}'.")

# Example of using the class with file path and search term
if __name__ == "__main__":
    file_path = "example.txt"  # Replace with your file path
    search_term = "error"  # Replace with the search term you want

    file_handler = FileHandler(file_path)
    file_handler.display_filtered_lines(search_term)
