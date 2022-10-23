
def get_hash(a, m, input_str):
    ln = len(input_str)
    hash_value = 0
    for i in range(0, ln):
        n_degree = ln - 1 - i
        char = input_str[i]
        hash_value = hash_value % m + ord(char) * pow(a, n_degree, m)  # ord(char) * a ** n_degree
    return hash_value


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    input_str = input()

    hash_result = get_hash(a, m, input_str)
    print(str(hash_result))
