"""dictionary for ex 06"""

__author__ = "730668650"


def invert(dict_invert: dict[str, str]) -> dict[str, str]:
    """inverts the dictionary key and value of input"""
    new_dict: dict[str, str] = {}

    for key in dict_invert:
        new_dict[dict_invert[key]] = key
    # inverts dict_input for return value
    if len(dict_invert) != len(new_dict):
        raise KeyError("duplicate keys")
    # checks to make sure there were no duplicate keys
    return new_dict


def favorite_color(fav_color: dict[str, str]) -> str:
    """returns the most popular color"""

    fav_count: int = 0
    val_count: int = 0
    favorite: str = ""
    temp_val: str = ""

    for key in fav_color:
        temp_val = fav_color[key]
        # sets variable to current key value to be checked
        for key in fav_color:
            if temp_val == fav_color[key]:
                val_count = val_count + 1
        if fav_count < val_count:
            favorite = temp_val
            fav_count = val_count
        val_count = 0
    return favorite
    # took forever to find out how to go through each value while checking current value
    # realized I could set value then create another loop within the loop


def count(vals: list[str]) -> dict[str, int]:
    """returns dictionary of all unique values and their count"""

    dict_count: dict[str, int] = {}
    # return value

    # added indexing variables to determine if there were multiples (up to that point)
    # bool is changed to false to cause key to not be added
    # removed excess variables bc I realized I could write it to work in less code

    for element in vals:
        if element in dict_count:
            dict_count[element] += 1
        else:
            dict_count[element] = 1
    # checks if value is in dictionary
    # if it is: adds one to count
    # if it isn't: creates a new dictionary entry

    return dict_count


def alphabetizer(list0: list[str]) -> dict[str, list[str]]:
    """creates dictionary with entries by starting letter"""

    alpha_dict: dict[str, list[str]] = {}

    for element in list0:
        a: str = element.lower()
        # added so it's not case sensitive
        if a[0] in alpha_dict:
            temp_list: list[str] = alpha_dict[a[0]]
            temp_list.append(element)
            alpha_dict[a[0]] = temp_list
        # if 1st letter of element is in dict, append it to dict
        # got stuck here for a bit bc I left out [0] for if statement
        else:
            temp_list: list[str] = [element]
            alpha_dict[a[0]] = temp_list
        # if it is first instance of letter, create new entry
        # had to change out instances of element[0] to a[0]
    return alpha_dict


weekly_attendance: dict[str, list[str]] = {
    "Monday": ["John, Joe, Vridia"],
    "Tuesday": ["Vridia", "Joseph"],
}


def update_attendance(attendance: dict[str, list[str]], day: str, person: str) -> None:
    """mutates input dictionary with day and person"""

    if day in attendance:
        temp_list: list[str] = attendance[day]
        temp_list.append(person)
        attendance[day] = temp_list
    # if day is already in attendance add it
    else:
        temp_list: list[str] = [person]
        attendance[day] = temp_list
    # if day isn't add new key
