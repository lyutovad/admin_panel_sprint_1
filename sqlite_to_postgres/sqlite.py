class SQLiteLoader:
    def __init__(self, connection) -> None:
        self.connection = connection

    def load(self, data_class, table_name: str, batch_size: int = 100) -> list:
        curs = self.connection.cursor()
        curs.execute(f"SELECT * FROM {table_name};")

        while True:
            data = curs.fetchmany(batch_size)
            if not data:
                break
            records = []
            for m in data:
                record = data_class(**m)
                records.append(record)
            yield records
