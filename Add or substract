"""Caught speeding."""


def caught_speeding(speed: int, is_birthday: bool) -> int:
    """
    Return which category caught_speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) => 0
    caught_speeding(65, False) => 1
    caught_speeding(65, True) => 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category caught_speeding ticket you would get (0, 1, 2).
    """
    ticket_size = 0
    if speed == 0 or is_birthday is True and speed <= 5:
        ticket_size = 0
    elif speed <= 60 or is_birthday is True and speed <= 65:
        ticket_size = 0
    elif speed >= 61 and speed <= 80 or is_birthday is True and speed >= 61 and speed <= 85:
        ticket_size = 1
    elif speed >= 81 or is_birthday is True and speed >= 85:
        ticket_size = 2
    return ticket_size
