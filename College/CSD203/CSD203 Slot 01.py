def filterfunc(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

def reducefunc(x: int, y: int) -> int:
    return max(x, y)

def mapfunc(number: int) -> int:
    return number ** 2

def main() -> None:
    array = list(map(float, input().split()))
    filtervals = filter(filterfunc, array)

    mapVals = map(mapfunc, filtervals)

if __name__ == '__main__':
    main()