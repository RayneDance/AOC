import os
import sys
import shutil
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

    input_path = f'{folder}/input.txt'
    solution_path = f'{folder}/solution.py'
    if os.path.exists(input_path) and os.path.exists(solution_path):
        print("Files already exist.")
        return

    else:
        if os.path.exists(input_path):
            with open(input_path, 'r') as f:
                content = f.read()
            if content:
                print(f"File {input_path} already has content.")
        else:
            fetch_input(year, day)

        if os.path.exists(solution_path):
            content = f.read()
            if content:
                print(f"File {solution_path} already has content.")
            else:
                create_solution(solution_path)
        else:
            create_solution(solution_path)

def create_solution(solution_path):

    # Check working directory. We need AOC/tools/base.py.
    current_dir = os.getcwd().split('/')[-1]
    file = "base.py"
    if current_dir != 'tools':
        file = "./tools/" + file


    # copy AOC/base.py as solution.py
    shutil.copyfile(file, solution_path)

def fetch_input(year, day):
    folder = f'{year}/day{day}'
    data = get_data(day=day, year=year)
    with open(f'{folder}/input.txt', 'w') as f:
        f.write(data)

if __name__ == '__main__':
    main()
