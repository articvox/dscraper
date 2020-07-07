def flatten(target: []) -> []:
    return [item for sublist in target for item in sublist]


def difference(list1: [], list2: []) -> []:
    return [c for c in list1 if c not in list2]
