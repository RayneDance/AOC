import os
import sys
from aocd import get_data
from dotenv import load_dotenv

def main():
    year, day = get_args()
    create_folder(year, day)
    create_files(year, day)

    load_dotenv()
    fetch_input(year, day)


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
    try:
        os.makedirs(folder)
    except FileExistsError:
        print(f'Folder {folder} already exists')


def create_files(year, day):
    folder = f'{year}/day{day}'
    files = ['input.txt', 'solution.py']
    for file in files:
        with open(f'{folder}/{file}', 'w') as f:
            f.write('')


def fetch_input(year, day):
    folder = f'{year}/day{day}'
    data = get_data(day=day, year=year)
    with open(f'{folder}/input.txt', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    main()
