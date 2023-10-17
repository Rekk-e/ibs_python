# Main solution
def duplicate_nums(nums: list) -> list or None:
    """
    Returns a sorted list of numbers
    that appeared twice in the list nums
    """

    result = list()
    is_not_duplicate = {}

    for num in nums:
        if num in is_not_duplicate:
            result.append(num)
        else:
            is_not_duplicate[num] = True

    return sorted(result) if result else None


# Other solution
def _duplicate_nums(nums: list) -> list or None:
    """
    Returns a sorted list of numbers
    that appeared twice in the list nums
    """

    result = list()
    unique_nums = list(set(nums))
    for i in nums:
        if not i in unique_nums or unique_nums.remove(i):
            result.append(i)

    return sorted(result) if result else None
