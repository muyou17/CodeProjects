from warnings import filterwarnings
filterwarnings('ignore')
from polars import read_csv, read_excel, DataFrame, ColumnNotFoundError
from time import sleep


def sheet() -> tuple[DataFrame, str]:
    while True:
        try:
            file: str = input("\nInput file name (or file path): ").strip('"')

            if file.endswith('.csv'):
                return read_csv(file), file.removesuffix('.csv')

            elif file.endswith('.xlsx'):
                sheets: dict[str, DataFrame] = read_excel(file, sheet_id=0, engine='calamine')
                for index, sheet in enumerate(sheets.keys()):
                    print(f"– Sheet {index + 1}: {sheet}")
                sheet: str = tuple(sheets.keys())[int(input("\nSelect sheet: ")) - 1]
                return sheets[sheet], sheet

            elif '.' in file:
                print("Invalid file extension.")
            else:
                print("Missing file extension.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as error:
            print(f"Invalid input: {error}")


def columns(sheet: DataFrame, name: str) -> list[str]:
    print("\nSheet:", name)
    for index, column in enumerate(sheet.columns):
        print(f"– Column {index + 1}: {column.split('\n')[0]}")

    while True:
        try:
            columns: list[str] = []
            for column in range(int(input("\nNumber of columns: "))):
                columns.extend(sheet[sheet.columns[int(input("– Select column: ")) - 1]].drop_nulls().to_list())
            return columns

        except ValueError:
            print("Invalid input.")
        except ColumnNotFoundError:
            print("Column not found.")


def main() -> None:
    #Greeting
    print("Welcome to Muyō's Sheet Extractor!"
          "\nPlease input your file name if the input file is in the same directory"
          " or file path if the file is in a different directory."
          "\nThe output file will be a text file located in the same folder as this file.")

    #Input
    while True:
        try:
            source, name = sheet()
            print(source)
            proceed: int = int(input("– Input 0 to select a different sheet.\n"
                                     "– Input 1 to proceed with this sheet.\n"
                                     "Proceed with this sheet?\n"))
            if proceed:
                data: list[str] = columns(source, name)
                break

        except ValueError:
            print("Invalid input.")

    #Output
    while True:
        try:
            with open(f'{input("\nOutput file name: ")}.txt', 'w') as file:
                file.write('\n'.join(data))
                print("\nExtraction successful!\n")
                break

        except FileNotFoundError:
            print("Invalid file name.")

    #Closing
    for count in range(3, 0, -1):
        print(f"Closing program in {count}...")
        sleep(1)


if __name__ == '__main__':
    main()