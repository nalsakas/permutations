def permutation(arr:list, length = None):
    if length is None:
        length = len(arr)

    if len(arr) == 0 or length == 0:
        return [[]]

    collect = []
    for item in arr:
        cp = list(filter(lambda x: x != item, arr))
        ret = permutation(cp, length - 1)
        collect += list(map(lambda x: [item, *x], ret))

    return collect


if __name__ == "__main__":
    a = ['1', '2', '3']
    b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(permutation(a, 1))
    print(permutation(a, 2))
    print(permutation(a))
    print(permutation(b, 3))