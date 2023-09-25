# Find Bill's Treasure

This is a programming challenge proposed by Professor Dr. José Grimaldo da Silva Filho. All the material and base code were provided by him. Your mission is to help Bill find his treasure in a 10x10 terrain, but with an additional challenge: you are not allowed to use memory-intensive algorithms such as DFS, BFS, Dijkstra, or A*.

## Description

Bill has lost his treasure in a 10x10 meter terrain and is counting on your cleverness to retrieve it. However, there are some restrictions to be considered:
- The use of memory-intensive algorithms is prohibited.
- You start by choosing a point (x, y) on the grid as the starting point.
- You can only move Bill up, down, left, or right.
- The treasure is hidden at some random location on the grid.
- You have a laser that indicates the Euclidean distance from each cell around Bill to the treasure. You can use this laser!

Your task is to create an efficient algorithm that finds Bill's treasure as quickly as possible, adhering to the rules mentioned above.

**Note:** For more detailed information on the proposed problem, consult the `BillExercise.odt.pdf` file provided by Professor Grimaldo.

## Installing Dependencies

Before starting, make sure to install the following Python dependencies:

1. No third-party packages are required for this challenge as it only uses Python's standard libraries.

You can follow the steps below to check if the necessary dependencies are present:

```bash
# Check if Python is installed
python --version

# Check if the tkinter package is available (Python's GUI library)
python -m tkinter -h
```

If tkinter is not already installed, the command `sudo apt install python3-tk` (for Linux) should solve it.

## How to Use

The algorithm in the `bill_found_the_treasure.py` file has already been developed with a basic logic that we've created. Edit the `bill_temp.py` to implement your own solution!

1. Clone this repository to your local environment.
2. Implement the logic to find the treasure in the `bill_temp.py` file.
3. Run the file to check if you've found the treasure correctly.
