
def get_number_of_tree(n) -> int:
    if n <= 1:
        return 1

    count = 0
    for i in range(1, n + 1):
        count += get_number_of_tree(i - 1) * get_number_of_tree(n - i)
    return count


if __name__ == '__main__':
    n = int(input())
    print(str(get_number_of_tree(n)))
