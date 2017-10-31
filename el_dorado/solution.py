rows = int(input())
current_row = [int(input())]
for i in range(rows - 1):
    previous_row = current_row + [0]
    current_row = [int(x) + max(previous_row[a], previous_row[a - 1]) for a, x in enumerate(input().split())]
print(max(current_row))
