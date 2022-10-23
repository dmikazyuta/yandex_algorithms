
def check_id(fw, sw):
    if abs(len(fw) - len(sw)) > 1:
        return 'FAIL'
    if len(fw) > len(sw):
        return check_id(sw, fw)

    fw_idx = 0
    sw_idx = 0
    diff_flag = False

    while fw_idx < len(fw) and sw_idx < len(sw):
        if fw[fw_idx] != sw[sw_idx]:
            if diff_flag:
                return 'FAIL'
            diff_flag = True

            if len(fw) == len(sw):
                fw_idx += 1
        else:
            fw_idx += 1

        sw_idx += 1

    return 'OK'


if __name__ == '__main__':
    first_word = input()
    second_word = input()

    result = check_id(first_word, second_word)
    print(result)