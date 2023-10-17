class chain_sum:
    """
    Object that performs chain summation
    """

    def __init__(self, value=0):
        self.value = value

    def __call__(self, num=None):
        if num is None:
            return self.value
        else:
            self.value += num
            return self

