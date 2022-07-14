import timeit


def solve(x, space, _print=False):
    segments = []
    max_index = len(space) - x
    for index in range(max_index + 1):
        temp_segment = []
        for x_index in range(x):
            temp_segment.append(space[index + x_index])
        segments.append(temp_segment)

    if _print: print(f'{segments=}')

    segment_minimas = [min(segment) for segment in segments]

    if _print: print(f'{segment_minimas=}')

    max_segment_minimas = max(segment_minimas)

    if _print: print(f'{max_segment_minimas=}')

    return max_segment_minimas

def solve(x, space):
    max_of_min_of_segments = 0
    max_index = len(space) - x + 1
    for index in range(max_index):
        min_of_segment = min(space[index: index + x])
        if min_of_segment > max_of_min_of_segments: max_of_min_of_segments = min_of_segment
    return max_of_min_of_segments

def main():
    tests = [
        (2, [1, 2, 3, 4, 5], 4),
        (2, [1, 2, 3, 4], 3),
        (2, [1, 2, 3], 2),
        (3, [1, 2, 3], 1),
        (1, [1, 2, 3], 3),
    ] * 300000

    start_time = timeit.default_timer()

    for x, space, solution in tests:
        try:
            result = solve(x, space)
            assert solution == result
        except Exception:
            print(f'{space=}', f'{x=}', f'{solution=}', f'{result=}')
            solve(x, space, True)

    finish_time = timeit.default_timer()

    total_time = finish_time - start_time

    print(f'{total_time=}')




if __name__ == '__main__':
    main()
