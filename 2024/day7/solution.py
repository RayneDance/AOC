class Solution:
    def __init__(self):
        self.file_text = open("example.txt", "r").readlines()
        self.puzzle = {int(line.split(":")[0]): [(line.split(":")[1].strip().split(" "))]for line in self.file_text}


def main():
    s = Solution()
    print(s.puzzle)

if __name__ == "__main__":
    main()