def calculate_approximately_square_root_by_bisection(square_target, tolerance = 1e-7, max_iterations = 1000):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    if square_target == 0 or square_target == 1:
        return square_target
    
    low = 0
    high = max(1, square_target)

    for _ in range(max_iterations):
        mid = (low + high) / 2
        square_mid = mid * mid

        if abs(square_mid - square_target) <= tolerance:
            return mid

        if square_mid < square_target:
            low = mid
            continue

        high = mid
    
    raise Exception(f'Cannot find square root of {square_mid} in {max_iterations} iterations')

def main():
    N = 4
    print(calculate_approximately_square_root_by_bisection(N))

main()