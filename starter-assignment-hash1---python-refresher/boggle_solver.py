class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.found_words = set()
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        
    def is_valid_word(self, word):
        return word in self.dictionary
    
    def dfs(self, word, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return
        if self.visited[row][col]:
            return
        
        word += self.grid[row][col]
        
        # Check if the word is valid
        if len(word) >= 3 and self.is_valid_word(word):
            self.found_words.add(word)
        
        # Mark the cell as visited
        self.visited[row][col] = True
        
        # Move in all 8 directions (including diagonals)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = row + dx, col + dy
            self.dfs(word, new_row, new_col)
        
        # Unmark the cell after recursion
        self.visited[row][col] = False
    
    def getSolution(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.dfs("", row, col)
        return list(self.found_words)


def main():
    # Example input
    grid = [["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "St", "Qu", "R"],
            ["O", "N", "T", "A"]]

    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "rat", "tarp", "tar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()