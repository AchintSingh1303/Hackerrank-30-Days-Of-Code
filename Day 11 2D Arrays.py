if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maximum = -9 * 7  # Min hourglass sum possible, since constraints -9 <A[i][j] < 9,and 7 elements

    for i in range(6):
        for j in range(6):
            if j + 2 < 6 and i + 2 < 6:  # Since the values of i and j are in top left subset of an hourglass
                result = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + \
                         arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
                if result > maximum:    # If sum comes greater in another hourglass, overwrites maximum sum to print
                    maximum = result

    print(maximum)
