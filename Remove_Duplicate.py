if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))

    unique_numbers = []
    seen = set()

    for num in numbers[:n]:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)

    print(*unique_numbers)