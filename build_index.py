import json

def build_index(log_file, index_file="index.json"):
    index = {}
    with open(log_file, 'r', encoding='utf-8') as file:
        position = 0
        for line in file:
            date = line.split()[0]  # Extract date (YYYY-MM-DD)
            if date not in index:
                index[date] = position  # Store byte offset of first occurrence
            position = file.tell()  # Update position

    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f)

if __name__ == "__main__":
    log_file = "large_log_file.log"
    build_index(log_file)
    print("Index built successfully!")
