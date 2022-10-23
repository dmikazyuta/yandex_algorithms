
def get_hash(a, m, input_str):
    ord_char_list = [ord(char) for char in input_str]
    ln = len(ord_char_list)
    if ln == 0:
        return 0
    hash_value = ord_char_list[0]
    for i in range(1, ln):
        hash_value = (hash_value * a + ord_char_list[i]) % m
    return hash_value


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    input_str = input()

    hash_result = get_hash(a, m, input_str)
    print(str(hash_result))
