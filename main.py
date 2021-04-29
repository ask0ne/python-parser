"""
A parsing algorithm to parse array string and convert it to an Array/List.
The elements of Array/List String can contain string,undefined variable,number,boolean and array.
"""
answer = []


def clean_element(element):
    """REMOVE EXTRA QUOTES AND SPACES"""
    element = element.lstrip()
    element = element.strip("'")
    element = element.strip('"')
    element = element.rstrip()
    return element


def typecast(element):
    """APPEND APPROPRIATE TYPE OF ELEMENT INTO LIST"""
    element = clean_element(element)
    if element.isdigit():
        return int(element)
    if element.lower() == "none" or element.lower() == "undefined" or element == " " or element == "":
        return None
    if element.lower() == "true":
        return True
    if element.lower() == "false":
        return False
    return element


def new_parameter(element, input_string, i):
    '''
    PARAMETER FOUND
    eg: func(x,y)
    '''
    while input_string[i] != ")":
        element += input_string[i]
        i += 1
    element += input_string[i]
    return element, i


def new_list(input_string, i):
    '''
    INNER SUBSEQUENT STRING/LIST PARSING (RECURSIVE FOR n DEPTH)
    eg: [1, [2, [3, 4]], 5]
    '''
    in_list = []
    element = ""
    i += 1
    while input_string[i] != "]":
        if input_string[i] == ",":
            if element:
                in_list.append(typecast(element))
            element = ""
            i += 1
        elif input_string[i] == "[":
            inner_list, i = new_list(input_string, i)
            in_list.append(inner_list)
        elif input_string[i] == "(":
            element, i = new_parameter(element, input_string, i)
            i += 1
        else:
            element += input_string[i]
            i += 1
    if element and element != " ":
        in_list.append(typecast(element))
        element = ""
    i += 1
    return in_list, i


def custom_parser(input_string):
    """
    main function
    """
    final_answer = []
    element = ""
    i = 0
    while i < len(input_string):
        if input_string[i] == "[":
            i += 1
            answer = []
            while input_string[i] != "]":
                '''OUTER STRING PARSING'''
                if input_string[i] == "'":
                    i +=1
                    while input_string[i] != "'":
                        element += input_string[i]
                        i +=1
                    answer.append(typecast(element))
                    element = ""
                    i +=1
                elif input_string[i] == ",":
                    if element:
                        answer.append(typecast(element))
                    element = ""
                    i += 1
                elif input_string[i] == "[":
                    inner_list, i = new_list(input_string, i)
                    answer.append(inner_list)
                elif input_string[i] == "(":
                    element, i = new_parameter(element, input_string, i)
                    i += 1
                else:
                    element += input_string[i]
                    i += 1
            if element and element != " ":
                answer.append(typecast(element))
                element = ""
            final_answer += answer
        i += 1
    return final_answer

CUSTOM_STRING = "[a, 'a,b,c', [b, [c, d]], 1, false]"
out = custom_parser(CUSTOM_STRING)
print(out)
