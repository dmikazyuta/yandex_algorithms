from functools import cmp_to_key

def compare(next, prev):
    prev_fl = float(prev[1])
    next_fl = float(next[1])
    if prev_fl == next_fl:
            if float(prev[0]) < float(next[0]):
                return 1
            else:
                return -1
    elif prev_fl < next_fl:
        return 1
    else:
        return -1


def get_sched(lessons):
    lessons_sorted = sorted(lessons.values(), key=cmp_to_key(compare))
    result = []
    prev = [0,0]
    for key in range(len(lessons_sorted)):
        if float(lessons_sorted[key][0]) >= float(prev[1]):
            prev = lessons_sorted[key]
            result.append(prev)
    return(result)


if __name__ == '__main__':
    lessons = {} #defaultdict(list)
    prev = 0

    n = int(input())
    for i in range(n):
        less_start, less_end = input().split(" ")
        lessons[i] = [less_start, less_end]

    result_list = get_sched(lessons)
    print(len(result_list))
    for rs in result_list:
        print(*rs, end="\n")