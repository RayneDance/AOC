class Solution:
    def __init__(self):
        self.file_text = open("input.txt", "r").readlines()


if __name__ == "__main__":
    s = Solution()
    print(s.file_text)