with open('input.txt', 'r') as f:
    with open('output.txt', 'w') as f2:
        f2.write(str(sum(list(map(int, f.read().split(' '))))))