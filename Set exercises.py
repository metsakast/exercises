"""Set exercises."""
import string


def count_of_symbols(word: str) -> int:
    """
    Return the count of different symbols.

    Use set here.
    Small and upper case letters are different.

    count_of_symbols("hello") => 4
    count_of_symbols("aAaB") => 3
    count_of_symbols("hello!") => 5
    count_of_symbols("yes and no") => 8
    count_of_symbols("Hello hi") => 7
    count_of_symbols("123454321") => 5
    """
    found_characters = []
    for i in word:
        if i not in found_characters:
            found_characters.append(i)
    return len(found_characters)
    pass


def count_of_letters(word: str) -> int:
    """
    Return the count of ascii letters in the string.

    Lower and upper case letters are treated as one.

    count_of_letters("Hello!") => 4
    count_of_letters("HELLO") => 4
    count_of_letters("HellohELLO") => 4
    count_of_letters("12345") => 0
    :param word:
    :return:
    """
    alphabet_lower = string.ascii_lowercase
    final_characters = []
    for i in word:
        if i.lower() in alphabet_lower and i.lower() not in final_characters:
            final_characters.append(i.lower())
    return len(final_characters)
    pass


def who_visited_two_events(names1, names2, names3) -> set:
    """
    Which people have visited exactly 2 events.

    We have three lists. Each indicates visitors for one event.
    We want to know, which people have visited exactly 2 events (not 1, not 3).
    Names are case sensitive (John != john).

    names for event 1: ["john", "mary", "peter", "mary"]
    names for event 2: ["john", "jane", "peter"]
    names for event 3: ["mary", "jack", "peter"]

    peter has visited all three events
    john visited event 1 and event 2
    mary visited event 1 and event 3 (it doesn't matter it's duplicated in event 1 list)
    jane and jack both visited only one event

    The order of the result is not important.
    (Actually the elements in a set are not ordered at all.)

    who_visited_two_events(["john", "mary"], ["john", "mary", "jack"], ["john", "jack"]) => {"mary", "jack"}
    who_visited_two_events(["john", "mary"], ["john", "julia", "jack"], ["john", "ben"]) => set()

    :param names1: names for event 1
    :param names2: names for event 2
    :param names3: names for event 3
    :return: names which have visited exactly 2 events.
    """
    names_set = set()
    for i in names1:
        if ((i in names2) and not (i in names3)) or ((i in names3) and not (i in names2)):
            names_set.add(i)
    for i in names2:
        if ((i in names1) and not (i in names3)) or ((i in names3) and not (i in names1)):
            names_set.add(i)
    for i in names3:
        if ((i in names1) and not (i in names2)) or ((i in names2) and not (i in names1)):
            names_set.add(i)
    return names_set
    pass


if __name__ == '__main__':
    print(who_visited_two_events(["john", "mary"], ["john", "mary", "jack"], ["john", "jack"]))
    print(who_visited_two_events(["john", "mary"], ["john", "julia", "jack"], ["john", "ben"]))
