
if __name__ == '__main__':
    n = int(input().strip())
    numbers = str(bin(n)[2:]).split('0')
    lengths = [len(num) for num in numbers]
    print(max(lengths))