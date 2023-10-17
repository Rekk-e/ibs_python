import csv
import logging
import argparse

logging.basicConfig(level=logging.INFO)

"""
Из условия задания я понял, что необходимо валидировать только Headers.
Если это не так, то прошу, по возможности, сообщить мне об этом. Добавлю необходимый функционал.
"""


def headers_validate(filepath: str, delimiter: str = ",", headers: list = None) -> None:
    """
    Performs table header validation
    """

    with open(filepath) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        table_headers = next(reader)
        not_missing = True
        if headers:
            for header in headers:
                if header not in table_headers:
                    logging.info(f'The "{header}" header is missing from the table')
                    not_missing = False

        exit(1) if not_missing else exit(0)


if "__main__" == __name__:

    # Parse script arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-filepath", help="Path to file")
    parser.add_argument("-delimiter", help="Delimiter in file")
    parser.add_argument('-headers', '--headers-list', help="Headers of file", nargs='+', default=[])

    args = vars(parser.parse_args())

    # Validate csv file
    headers_validate(args["filepath"], args["delimiter"], args["headers_list"])