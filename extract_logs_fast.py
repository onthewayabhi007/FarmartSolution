import sys
import json

def extract_logs(log_file, target_date, index_file="index.json"):
    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            index = json.load(f)

        if target_date not in index:
            print(f"No logs found for {target_date}")
            return

        position = index[target_date]

        with open(log_file, 'r', encoding='utf-8') as file:
            file.seek(position)  # Jump to the start of the target date section

            for line in file:
                if line.startswith(target_date):
                    print(line, end='')
                else:
                    break  # Stop when we reach a different date

    except FileNotFoundError:
        print("Error: Log file or index not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs_fast.py <log_file> <YYYY-MM-DD>")
        sys.exit(1)

    log_file = sys.argv[1]
    target_date = sys.argv[2]

    extract_logs(log_file, target_date)