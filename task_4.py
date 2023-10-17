import tempfile


def to_begin(func):
    """
    Decorator for carriage return to the beginning of the tempfile
    """

    def wrapper(*args, **kwargs):
        self = args[0]
        self.tf.seek(0)
        return func(*args, **kwargs)

    return wrapper


class ManagedTempFile(object):
    """
    Сlass-based context manager that creates
    a temporary file using the tempfile library
    """

    def __init__(self) -> None:
        self.tf = tempfile.TemporaryFile(mode='w+t')

    def __enter__(self):
        return self

    @to_begin
    def __exit__(self, type, value, traceback) -> bool:
        file_content = self.tf.read()
        print(f"Number of characters in file: {len(file_content)}")
        self.tf.close()
        return True

    @to_begin
    def write(self, msg: str) -> None:
        """
        Writes text to the beginning of the file
        """

        file_content = self.tf.read()
        self.tf.seek(0)
        self.tf.write(msg)
        if file_content:
            self.tf.write(file_content)

    @to_begin
    def show(self) -> None:
        """
        Prints the contents of a file to the console
        """

        print(self.tf.read())

    @to_begin
    def repeat(self) -> None:
        """
        Duplicates the current contents of the file
        and appends it to the end of the file
        """

        self.tf.write(self.tf.read())

'''
with ManagedTempFile() as mt:
    mt.write("hello world\n")
    mt.write("hello world2\n")
    mt.repeat()
    mt.show()
'''
