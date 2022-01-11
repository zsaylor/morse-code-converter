import csv

with open("morse_key.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    morse_dict = {rows[0]: rows[1] for rows in reader}


def main():
    convert_mode = input("Convert Morse code or text? (M / T)\n")
    if convert_mode == "M":
        msg_to_convert = str(input("Enter a message:\n"))
        print(morse_to_str(msg_to_convert))
    elif convert_mode == "T":
        msg_to_convert = str(input("Enter a message:\n")).upper()
        print(str_to_morse(msg_to_convert))
    else:
        print("Entry invalid. Please type either M for morse code or T for text.")
        main()


def str_to_morse(message):
    message_list = list(message)
    morse_list = []

    for letter in message_list:
        if letter == " ":
            new_morse_letter = " "
        else:
            new_morse_letter = morse_dict[letter]
        morse_list.append(new_morse_letter)

    morse_message = '   '.join(morse_list)  # Space between letters should be 3 units.
    return morse_message


def morse_to_str(message):
    inverse_morse_dict = {code: letter for letter, code in morse_dict.items()}

    message_list = message.split("   ")

    str_list = []

    for code in message_list:
        if code == '':
            new_letter = " "
        else:
            stripped_code = code.strip()
            new_letter = inverse_morse_dict[stripped_code]
        str_list.append(new_letter)

    str_message = "".join(str_list)
    return str_message


if __name__ == "__main__":
    main()


