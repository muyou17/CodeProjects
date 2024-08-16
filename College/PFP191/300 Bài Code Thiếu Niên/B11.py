from random import choice


def main() -> None:
    ratio: list[int] = [0, 0]

    while True:
        player: str = input('Input r/p/c: ')

        if player not in ('r', 'p', 'c'):
            exit(0)

        print("Computer:", computer := choice('rpc'))
        if player == computer:
            pass
        elif player == 'p' and computer == 'r':
            ratio[0] += 1
        elif player == 'r' and computer == 'c':
            ratio[0] += 1
        elif player == 'c' and computer == 'p':
            ratio[0] += 1
        else:
            ratio[1] += 1

        print("Player - Computer Ratio: %d - %d" % (ratio[0], ratio[1]), end='\n\n')


if __name__ == '__main__':
    main()