name="aman"

with open("../birthday_wisher/letter_templates/letter_1.txt") as letter:
    lines=letter.read()
    lines=lines.replace("[NAME]",nam)
    print(lines)