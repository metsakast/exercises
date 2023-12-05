def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("xaaaxbbxccxdxbb") => 3
    max_block("") => 0
    """
    current_sequence = ""
    current_longest_sequence = ""
    for char in s:
        if len(current_sequence) == 0:
            current_sequence += char
        elif char == current_sequence[-1]:
            current_sequence += char
        else:
            if len(current_sequence) > len(current_longest_sequence):
                current_longest_sequence = current_sequence
            current_sequence = char
    if len(current_sequence) > len(current_longest_sequence):
        current_longest_sequence = current_sequence
    return len(current_longest_sequence)

max_block("input")