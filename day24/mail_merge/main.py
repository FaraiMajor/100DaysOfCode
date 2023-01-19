PLACEHOLDER = "[name]"


with open("day24/mail_merge/Input/Names/invited_names.txt") as names:
    name_list = names.read().split("\n")
    # name_list = names.readlines()

with open("day24/mail_merge/Input/Letters/starting_letter.txt") as letter_file:
    contents = letter_file.read()
    for name in name_list:
        name = name.strip()
        new_letter = contents.replace(PLACEHOLDER, name)
        print(new_letter)
        with open(f"day24/mail_merge/Output/ReadyToSend/letter_for_{name}.txt", "w") as final_letters:
            final_letters.write(new_letter)
