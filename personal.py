def free_biscuits(input_dict: dict[str, list[int]]) -> dict[str, bool]:
    scores: dict[str, bool] = {}

    for keys in input_dict:
        points: list[int] = input_dict[keys]

        sum: int = 0
        for elem in points:
            sum += elem

        if sum >= 100:
            scores[keys] = True
        else:
            scores[keys] = False

    return scores
