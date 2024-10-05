from os import chdir, getcwd, startfile


def main() -> None:
    file_name = input("File name: ")
    with open("resize-image.bat", 'w') as file:
        file.write(
            f"gm convert {file_name} "
            f"-resize 450x300 {file_name[:-4]}.webp"
        )
    chdir(getcwd())
    startfile("resize-image.bat")


if __name__ == '__main__':
    main()