def filter_lines(file_path, keyword):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        filtered_lines = [line for line in lines if keyword in line]
    return filtered_lines

# Usage
file_path = 'example.txt'  # ensure the file exists
keyword = 'error'
filtered_lines = filter_lines(file_path, keyword)

for line in filtered_lines:
    print(line.strip())
