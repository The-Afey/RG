def check(text):
    brackets = []

    for tp in text:
        if tp == '(':
            brackets.append(tp)
        else:
            if tp == ')':
                if not brackets:
                    return False
                else:
                    brackets.pop()

    return len(brackets) == 0


if check(input("Введите текст для проверки: ")):
    print("Скобки расставлены правильно.")
else:
    print("Скобки расставлены неправильно.")
