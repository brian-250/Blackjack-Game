import sys

def is_ace(card_name):
    return (card_name == "A")

def is_face_card(card_name):
    return (card_name == "J") or (card_name == "Q") or (card_name == "K")

def is_number_card(card_name):
    card_value = 0
    is_number_card = True
    try:
        card_value = int(card_name)
        if (card_value < 2) or (card_value > 10):
            return False
    # This was some previous code that was not needed:
    # except ValueError:
    except:
        is_number_card = False
    return is_number_card

def is_card_name(str):
    return ((is_ace(str)) or (is_face_card(str)) or (is_number_card(str)))

def all_arguments_valid(arguments):
    for i in range(1, len(arguments)):
        if not (is_card_name(arguments[i])):
            print("error: unknown card " + arguments[i])
            return False
    return True

def card_points(card_name):
    return_card_value = 0
    if is_ace(card_name):
        return_card_value = 1
    elif is_face_card(card_name):
        return_card_value = 10
    elif is_number_card(card_name):
        return_card_value = int(card_name)
    return return_card_value

# This was some previos code that did not work:
# def hand_contains_ace(arguments):
#     return any(is_ace(arg) for arg in arguments[1:])

def hand_contains_ace(arguments):
    for i in range(1, len(arguments)):
        if (is_ace(arguments[i])):
            return True
    return False

def is_bust(score):
    return (score > 21)

# This was some previous code that did not work:
# def hand_score(arguments):
#     sum_score = sum(card_points(arg) for arg in arguments[1:])
#     if not is_bust(sum_score + 10) and hand_contains_ace(arguments):
#         sum_score += 10
#     return sum_score

def hand_score(arguments):
    sum = 0
    for i in range(1, len(arguments)):
        sum = sum + card_points(arguments[i])
    if (not is_bust((sum + 10))) and (hand_contains_ace(arguments)):
        sum = sum + 10
    return sum

def print_score(score):
    if score < 22:
        print("Score is " + str(score) + "\n")
    else:
        print("Score is "  + str(score) + ", BUST\n")

if __name__ == "__main__":
    arguments = sys.argv
    if not (all_arguments_valid(arguments)):
        sys.exit(-1)
    print_score(hand_score(arguments))
    sys.exit(0)
