NUMBER_OF_DISKS = 3
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

print(A)

def move(n, source, auxiliary, destination):
    if n <= 0:
        return

    move(n-1, source, destination, auxiliary)

    destination.append(source.pop())

    print('\n', A, B, C)

    move(n-1, auxiliary, source, destination)

if __name__ == '__main__':
    move(NUMBER_OF_DISKS, A, B, C)