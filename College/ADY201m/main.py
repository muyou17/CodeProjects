from sqlite3 import Cursor, connect


def q1(cursor: Cursor) -> int:
    return cursor.execute(
        """
        SELECT count(DISTINCT symbol)
        FROM StockTrading
        """
    ).fetchone()[0]


def q2(cursor: Cursor) -> int:
    return cursor.execute(
        """
        SELECT count(DISTINCT CategoryId)
        FROM StockList JOIN StockTrading ON StockList.Symbol = StockTrading.symbol
        """
    ).fetchone()[0]


def q3(cursor: Cursor) -> int:
    return cursor.execute(
        """
        SELECT COUNT(DISTINCT strftime('%Y-%m', tradeDate))
        FROM StockTrading
        """
    ).fetchone()[0]


def q4(cursor: Cursor) -> tuple[float, float]:
    return cursor.execute(
        """
        WITH tradeValue AS (SELECT cast(price AS int) AS tradeValue
                            FROM StockTrading
                            WHERE symbol = 'FPT' AND substring(tradeDate, 0, 8) = '2024-08')
        SELECT min(tradeValue), max(tradeValue)
        FROM tradeValue
        """
    ).fetchone()


def main():
    cursor = connect("Stock.db").cursor()
    q4_result = q4(cursor)
    
    print(f"Question 1: {q1(cursor)}\n"
          f"Question 2: {q2(cursor)}\n"
          f"Question 3: {q3(cursor)}\n"
          f"Question 4: {q4_result[0]}, {q4_result[1]}")


if __name__ == '__main__':
    main()