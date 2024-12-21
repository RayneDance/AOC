import copy
class Solution:
    def __init__(self):
        self.file_text = open("input.txt", "r").readlines()
        self.data = []
        self.p2data = []
        for line in self.file_text:
            f_count = 0
            for i, char in enumerate(line.strip()):
                if i % 2 == 0:
                    for _ in range(int(char)):
                        self.data.append(Block(f_count))
                    f_count += 1
                else:
                    for _ in range(int(char)):
                        self.data.append('.')
        self.p2data = copy.deepcopy(self.data)
        self.shift_data()
        self.shift_p2data()

    def shift_data(self):
        idx0 = self.data.index('.')
        for i in range(len(self.data)-1, 0, -1):
            if self.data[i] != '.':
                self.data[idx0] = self.data[i]
                self.data[i] = '.'
                idx0 = self.get_next_empty_memory(idx0)
                if idx0 == -1 or idx0 >= i:
                    break

    def shift_p2data(self):
        idx0 = self.p2data.index('.')
        idx1 = len(self.p2data) - 1
        max_block = len(self.p2data) - 1
        #print(self.p2data)
        while idx1 > self.find_contiguous_memory_of_sz(1):
            idx1, sz = self.get_last_contiguous_block(max_block)
            idx0 = self.find_contiguous_memory_of_sz(sz)


            if idx0 == -1 or idx1 < idx0:
                idx0 = 0
                max_block = idx1 - 1
            else:
                for _ in range(sz):
                    self.p2data[idx0] = self.p2data[idx1]
                    self.p2data[idx1] = '.'
                    idx0 += 1
                    idx1 += 1
                    #print(self.p2data)
                else:
                    idx1 -= 1
                    max_block = idx1
            #print(idx0, idx1, max_block, sz)

    def get_next_empty_memory(self, idx):
        return self.data.index('.', idx)

    def find_contiguous_memory_of_sz(self, sz):
        count = 0
        for i in range(0, len(self.p2data)):
            if self.p2data[i] == '.':
                count += 1
                if count == sz:
                    return i - sz + 1
            else:
                count = 0
        return -1

    def get_last_contiguous_block(self, idx_max=None):
        idx = len(self.p2data) - 1 if idx_max is None else idx_max
        while self.p2data[idx] == '.':
            idx -= 1

        val = self.p2data[idx].data
        idx_end = idx

        while idx >= 0 and self.p2data[idx] != '.' and self.p2data[idx].data == val:
            idx -= 1
        idx += 1

        return idx, (1 + idx_end - idx)


class Block:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

def main():
    s = Solution()
    total = 0
    total2 = 0
    for i, x in enumerate(s.data):
        if x != '.':
            total += i * x.data
    for i, x in enumerate(s.p2data):
        if x != '.':
            total2 += i * x.data
    print(total)
    print(total2)

if __name__ == "__main__":
    main()