class Board:
    def __init__(self, n=8):
        self.n = n
        self.queens = []

    def place(self, row, col):
        self.queens.append((row, col))

    def remove(self, row, col):
        self.queens.remove((row, col))

    def is_safe(self, row, col):
        for r, c in self.queens:
            if r == row or c == col:
                return False
            if abs(r - row) == abs(c - col):
                return False
        return True

    def solve(self):
        if len(self.queens) == self.n:
            return True

        row = len(self.queens)

        for col in range(self.n):
            if self.is_safe(row, col):
                self.place(row, col)

                if self.solve():
                    return True

                self.remove(row, col)

        return False

    def __str__(self):
        lines = []
        for r in range(self.n):
            line = ""
            for c in range(self.n):
                if (r, c) in self.queens:
                    line += "[Q]"
                else:
                    line += "[ ]"
            lines.append(line)
        return "\n".join(lines)

    def __len__(self):
        return len(self.queens)

    def __iter__(self):
        return iter(self.queens)

def run_solver(n=8):
    b = Board(n)
    if b.solve():
        print(f"Rozwiązanie dla {n} królowych:")
        print(b)
    else:
        print(f"Brak rozwiązania dla {n} królowych.")

if __name__ == "__main__":
    run_solver(8)