spam = ['apples', 'bananas', 'tofu', 'cats']


def format_list(input_list):
    if not input_list:
        return "No items in the list"

    if len(input_list) == 1:
        return str(input_list[0])

    formatted_string = ""
    for item in input_list[:-1]:
        formatted_string += str(item) + ' ,'

    formatted_string += f"and {input_list[-1]}"
    return formatted_string


print(format_list(spam))
