import csv
import random
import string


class RandomCsvGenerator():
    """
    Class for generating random data in csv format
    """

    def __init__(self, n: int, header: dict) -> None:
        if n > 1000000000:
            raise ValueError("n must be less than 10^9")

        self.rows = n
        self.header = header
        self.types = {
            int: lambda: random.randint(0, 100),
            bool: lambda: random.choice([True, False]),
            str: lambda: ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        }

    def _get_random_row(self) -> dict:
        """
        Generates a random row
        """

        for _ in range(self.rows):
            row = dict()
            for k, v in self.header.items():
                row[k] = self.types[v]()

            yield row

    def generate_csv(self) -> None:
        """
        Creating csv file and write random data
        """

        with open("random_data.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(self.header.keys())

            for row in self._get_random_row():
                writer.writerow(row.values())


header = {
    'column1': int,
    'column2': str,
    'column3': bool
}

generator = RandomCsvGenerator(1000, header)
generator.generate_csv()

