def main() -> None:
    foo = "Hello world!";

    for bar, baz in enumerate(foo):
        print(foo[:bar+1]);


if __name__ == '__main__':
    main();