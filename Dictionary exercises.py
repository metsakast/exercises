"""Dictionary exercise."""


def unique_dict_items(dict1: dict, dict2: dict) -> dict:
    """
    Find unique items from two dictionaries.

    You are given two dictionaries.
    Your task is to find the key-value pairs from both
    dictionaries that are unique to each dictionary.
    (This means key-value paris that are present only in one of them)

    If two dictionaries contain same keys then you can be sure that the values
    are also identical. It means that such case is not possible: dict1 = {"a": 1}, dict2 = {"a": 2}.

    :param dict1: First dictionary.
    :param dict2: Second dictionary.
    :return: Unique items from both dictionaries.
    """
    unique_items = dict()
    for key, value in dict1.items():
        if key not in dict2:
            unique_items[key] = value
    for key, value in dict2.items():
        if key not in dict1:
            unique_items[key] = value
    return unique_items
    pass


if __name__ == '__main__':
    print(unique_dict_items({"a": 1, "b": 2, "c": 3}, {"a": 1, "h": 2, "f": 3}))  # {'b': 2, 'c': 3, 'f': 3, 'h': 2}
    print(unique_dict_items({"a": 1, "b": 2}, {"a": 1, "b": 2, "f": 3, "aa": 2}))  # {'aa': 2, 'f': 3}
