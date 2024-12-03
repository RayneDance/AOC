import os
import sys
from aocd import get_data
from dotenv import load_dotenv

def main():
    year, day = get_args()
    create_folder(year, day)
    create_files(year, day)

    load_dotenv()


def get_args():
    arguments = sys.argv[1:]
    if not arguments:
        print("Usage: python gen_files_folder.py --year <year> --day <day>")
        sys.exit(1)

    # Split arguments into pairs
    args = dict(zip(arguments[::2], arguments[1::2]))
    year = args.get('--year')
    day = args.get('--day')

    try:
        year = int(year)
        day = int(day)
    except ValueError:
        print("Year and day must be integers")
        sys.exit(1)

    if not year or not day:
        print("Usage: python gen_files_folder.py --year <year> --day <day>")
        sys.exit(1)

    return year, day


def create_folder(year, day):
    folder = f'{year}/day{day}'
    os.makedirs(folder, exist_ok=True)

def create_files(year, day):
    folder = f'{year}/day{day}'
    files = ['input.txt', 'solution.py']
    for file in files:
        file_path = f'{folder}/{file}'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
            if content:
                print(f"File {file_path} already has content.")
            else:
                with open(file_path, 'w') as f:
                    f.write('')
        else:
            with open(file_path, 'w') as f:
                f.write('')
            fetch_input(year, day)


def fetch_input(year, day):
    folder = f'{year}/day{day}'
    data = get_data(day=day, year=year)
    with open(f'{folder}/input.txt', 'w') as f:
        f.write(data)

if __name__ == '__main__':
    main()
