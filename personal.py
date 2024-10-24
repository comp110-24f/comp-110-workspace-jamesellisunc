def odd_and_even(list_1: list[int]) -> list[int]:
    idx: int = 0
    list_2: list[int] = []

    while idx < len(list_1):
        if idx % 2 == 0 and list_1[idx] % 2 == 1:
            list_2.append(list_1[idx])
        idx += 1
    return list_2
