import sys

def extract_logs(log_file, target_date):
    try:
        with open(log_file, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith(target_date):
                    print(line, end='')
    except FileNotFoundError:
        print("Error: Log file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_file> <YYYY-MM-DD>")
        sys.exit(1)

    log_file = sys.argv[1]
    target_date = sys.argv[2]

    extract_logs(log_file, target_date)