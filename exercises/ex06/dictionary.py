"""EX06 - Dictionary Utility Functions - Implementation"""

__author__ = "730776315"


def invert(inp: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of the input dictionary."""
    # lines 8-22: checks values to prevent duplicate keys in output
    k_list: list[str] = []
    for key in inp:
        k_list.append(inp[key])
    i: int = 0  # index of the value being compared with other values in dict
    while i < len(k_list):
        j: int = 0  # index of the current value being compared with temp
        temp: str = k_list[i]  # the value being compared with other values in dict
        count: int = 0  # counts occurences of temp in k_list
        for j in range(0, len(k_list)):
            if temp == k_list[j]:
                count += 1
            if count > 1:  # there are more occurences of temp in k_list than itself
                raise KeyError("Duplicate keys encountered.")
            j += 1
        i += 1
    # lines 24-32: creates lists of keys and values and returns
    # dict where they are switched
    new_keys: list[str] = []
    new_vals: list[str] = []
    ret_dict: dict[str, str] = {}  # initialize return dict
    for k in inp:
        new_vals.append(k)  # stores the keys of inp
        new_keys.append(inp[k])  # stores the values of inp
    for index in range(0, len(new_keys)):
        ret_dict[new_keys[index]] = new_vals[index]
    return ret_dict


def favorite_color(inp: dict[str, str]) -> str:
    """Returns the most popular color value from an input dictionary."""
    k_list: list[str] = []  # lines 39-42: creates list of color values
    for k in inp:
        k_list.append(inp[k])
    i: int = 0  # index of the value being compared with other values in k_list
    count_dict: dict[str, int] = {}  # keys: color; values: occurences of color
    while i < len(k_list):
        j: int = 0  # index of the current value being compared with k_list[i]
        temp: str = k_list[i]
        count: int = 0
        for j in range(0, len(k_list)):
            if temp == k_list[j]:
                count += 1
            j += 1
        count_dict[k_list[i]] = count
        i += 1
    top_color: str = ""
    value: int = 0
    for k in count_dict:
        if count_dict[k] > value:  # finds highest count value in count_dict
            value = count_dict[k]
            top_color = k
    return top_color


def count(inp: list[str]) -> dict[str, int]:
    """Counts the number of times a value appeared in the input list."""
    i: int = 0  # index of the value being compared with other values in inp
    count_dict: dict[str, int] = {}
    while i < len(inp):
        j: int = 0  # index of the current value being compared with inp[i]
        temp: str = inp[i]
        count: int = 0
        for j in range(0, len(inp)):
            if temp == inp[j]:
                count += 1
            j += 1
        count_dict[inp[i]] = count
        i += 1
    return count_dict


def alphabetizer(inp: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary identifying values that start with specific letters."""
    i: int = 0
    letter_list: list[str] = []  # stores first letter of words in inp
    for i in range(0, len(inp)):
        word: str = inp[i].lower()
        letter_list.append(word[0])  # adds first letter of word to letter_list
        i += 1
    out_dict: dict[str, list[str]] = {}
    for j in range(0, len(inp)):
        temp_list: list[str] = []  # list of words that start with temp (letter)
        temp: str = letter_list[j]  # start letter that we are looking for in inp
        for k in range(0, len(inp)):
            if letter_list[k] == temp:
                temp_list.append(inp[k])
            k += 1
        out_dict[temp] = temp_list  # adds results for this letter to output dict
        j += 1
    return out_dict


def update_attendance(inp: dict[str, list[str]], day: str, stu: str) -> None:
    """Updates input dictionary with an input student and the day they were present."""
    if day in inp:  # if the key already exists in inp, update value
        same_name: bool = True
        for item in inp[day]:
            if item == stu:
                same_name = False
        if same_name is True:
            inp[day].append(stu)
    else:  # if the key does not already exist in inp, add key/value pair
        inp[day] = [stu]
