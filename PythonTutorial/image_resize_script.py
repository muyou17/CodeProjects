from subprocess import CalledProcessError, run


def main() -> None:
    while True:
        file_name = input("File name: ")
        try:
            run(fr'gm convert "G:/My Drive/File Transfer/{file_name}" -resize 450x300 '
                fr'"G:/My Drive/web_projects/python_tutorial/assets/images/{file_name}.webp"',
                shell=True, check=True)
            print("Image resized successfully.")
            exit(0)
        except CalledProcessError as e:
            print(f"An error occurred while resizing the image: {e}")
        except FileNotFoundError:
            print("The directory was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()