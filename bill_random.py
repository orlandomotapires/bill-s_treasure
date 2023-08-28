import random
import math
import tkinter as tk
from tkinter import messagebox

N = 10
M = 10
L = 5

grid = []

def generate_grid(N, M):
    grid = []
    for i in range(N):
        grid.append([])
        for j in range(M):
            grid[i].append("wall")

    # Place random lines inside the grid
    num_lines = random.randint(N * M // 4, N * M // 2)
    for _ in range(num_lines):
        i = random.randint(1, N-2)
        j = random.randint(1, M-2)
        direction = random.choice(["horizontal", "vertical"])
        length = random.randint(1, min(N-1, M-1) // 2)
        if direction == "horizontal":
            for jj in range(j, min(j + length, M-1)):
                grid[i][jj] = "wall"
        else:
            for ii in range(i, min(i + length, N-1)):
                grid[ii][j] = "wall"

    # Place open spaces randomly in the grid
    num_open = random.randint(N * M // 2, N * M)
    for _ in range(num_open):
        i = random.randint(1, N-2)
        j = random.randint(1, M-2)
        grid[i][j] = "open"

    return grid

grid = generate_grid(N,M)


# Generate random treasure location
treasure_i = random.randint(1, N-2)
treasure_j = random.randint(1, M-2)
while True:
    distance = math.sqrt((treasure_i - 1)**2 + (treasure_j - 1)**2)
    if distance >= L:
        break
    treasure_i = random.randint(1, N-2)
    treasure_j = random.randint(1, M-2)

class GridWorld(tk.Tk):
    def __init__(self, N, M, L, grid, decision_callback=None):
        tk.Tk.__init__(self)
        self.N = N
        self.M = M
        self.grid = grid
        self.L = L
        self.decision_callback = decision_callback
        self.number_decisions = 0
        self.found_treasure = False
        self.max_decisions = 500

        self.canvas = tk.Canvas(self, width=self.M*40, height=self.N*40)
        self.canvas.pack()

        self.bill_i, self.bill_j = self.get_random_open_position()
        self.treasure_i, self.treasure_j = self.get_random_open_position()
        while math.sqrt((self.bill_i - self.treasure_i)**2 + (self.bill_j - self.treasure_j)**2) < self.L:
            self.treasure_i, self.treasure_j = self.get_random_open_position()

        self.draw_grid()
        self.draw_bill()
        self.draw_treasure()

        if self.decision_callback:
            self.after(100, self.make_decision)

    def get_random_open_position(self):
        i = random.randint(0, self.N-1)
        j = random.randint(0, self.M-1)
        while self.grid[i][j] == "wall":
            i = random.randint(0, self.N-1)
            j = random.randint(0, self.M-1)
        return (i, j)

    def draw_grid(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.grid[i][j] == "wall":
                    color = "black"
                else:
                    color = "white"
                x1, y1 = j*40, i*40
                x2, y2 = x1+40, y1+40
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def draw_bill(self):
        x1, y1 = self.bill_j*40, self.bill_i*40
        x2, y2 = x1+40, y1+40
        self.canvas.create_oval(x1+10, y1+10, x2-10, y2-10, fill="red")

    def draw_treasure(self):
        x1, y1 = self.treasure_j*40, self.treasure_i*40
        x2, y2 = x1+40, y1+40
        self.canvas.create_rectangle(x1+15, y1+15, x2-15, y2-15, fill="yellow")
        
    def make_decision(self):
        up = None
        down = None
        left = None
        right = None

        if self.bill_i > 0 and self.grid[self.bill_i-1][self.bill_j] != "wall":
            up = math.sqrt((self.bill_i-1 - self.treasure_i)**2 + (self.bill_j - self.treasure_j)**2)
        if self.bill_i < self.N-1 and self.grid[self.bill_i+1][self.bill_j] != "wall":
            down = math.sqrt((self.bill_i+1 - self.treasure_i)**2 + (self.bill_j - self.treasure_j)**2)
        if self.bill_j > 0 and self.grid[self.bill_i][self.bill_j-1] != "wall":
            left = math.sqrt((self.bill_i - self.treasure_i)**2 + (self.bill_j-1 - self.treasure_j)**2)
        if self.bill_j < self.M-1 and self.grid[self.bill_i][self.bill_j+1] != "wall":
            right = math.sqrt((self.bill_i - self.treasure_i)**2 + (self.bill_j+1 - self.treasure_j)**2)

        direction = " "
        
        if self.number_decisions >= 200 or impossible(left, right, up, down):
            direction = "giveup"

        if direction != "giveup":
            direction = self.decision_callback(up, down, left, right)

        print(f"num_decisions: {self.number_decisions}")

        self.number_decisions  += 1

        if direction == "giveup":
            messagebox.showinfo("Not today", "Bill gave up!")
            self.quit()        
            return  
        
        elif direction == "up" and up is not None:
            self.bill_i -= 1
        elif direction == "down" and down is not None:
            self.bill_i += 1
        elif direction == "left" and left is not None:
            self.bill_j -= 1
        elif direction == "right" and right is not None:
            self.bill_j += 1
        else:
            messagebox.showinfo("Error", "Invalid direction returned by decision_callback")
            self.quit()
            return

        if self.bill_i == self.treasure_i and self.bill_j == self.treasure_j:
            messagebox.showinfo("Congratulations", "Bill found the treasure!")
            self.found_treasure = True
            self.quit()
        elif self.number_decisions >= self.max_decisions:
            messagebox.showinfo("Time's up", "Maximum number of decisiosn reached, sorry!")
            self.quit()
        else:
            self.canvas.delete("all")
            self.draw_grid()
            self.draw_bill()
            self.draw_treasure()
            self.after(500, self.make_decision)

# You return one of these: up, down, left, right or giveup
# As parameters you receive the euclidean distance
# to the goal from each neighborhood position
# if the position is a wall it will return None as distance

Dir = []
def example_callback(up, down, left, right):
    directions = ["up", "down", "left", "right"]
    distances = [up, down, left, right]

    num_max_al = 4
    num_atu = 0 
    decisao_foracada = False

    if num_atu == num_max_al:
        num_atu = 0
    if num_atu < num_max_al and num_atu != 0:
        decisao_foracada = True

    Min = 9999
    for i in distances:
        if i != None:
            Min = min(Min, i)
    
    dis = distances.index(Min)
    Dir.append(Min)
    if len(Dir) < 3:
        return directions[dis]
    else:
        if Min == Dir[-3] or decisao_foracada:
            num_atu += 1
            print("Tomei uma decisao aleatoria")
            decisao = random_decision(left, right, up, down)
            print(f"Minha decisao: {decisao}")
            return decisao
    return directions[dis]


def random_decision(left, right, up, down):
    directions = ["up", "down", "left", "right"]
    direction = random.choice(directions)

    while not direction_valid(direction, left, right, up, down):
        direction = random.choice(directions)

    return direction

def direction_valid(direction, left, right, up, down):
    return (direction == "left" and left != None) or (direction == "right" and right != None) or (direction == "up" and up != None) or (direction == "down" and down != None)

def impossible(left, right, up, down):
    return left == None and right == None and up == None and down == None

app = GridWorld(N, M, L, grid, example_callback)
#app.bind("<Left>", lambda event: app.move_bill("left"))
#app.bind("<Right>", lambda event: app.move_bill("right"))
#app.bind("<Up>", lambda event: app.move_bill("up"))
#app.bind("<Down>", lambda event: app.move_bill("down"))
app.mainloop()

cost_decision = -1     # Recompensa a cada rodada
reward_treasure = 1000 # Recompensa se achar o tesouro
reward_no_treasure = 0 # Recompensa se não achar

score = cost_decision * app.number_decisions 

if app.found_treasure:
  score += reward_treasure     
else:
  score += reward_no_treasure
  
print(score)   