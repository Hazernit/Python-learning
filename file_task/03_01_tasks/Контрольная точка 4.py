from random import randint, choice

human_problem = input("Расскажите о своей проблеме:")

reason = ['Во всём виноваты ваши родители', 'Просто улыбнитесь',
          'Что нас не убивает, делает нас сильнее', 'Жизнь продолжается',
          'Даже после самой темной ночи наступает рассвет, а сильный дождь заканчивается радугой']

total = randint(2000, 7000)

print("Понимаю.", choice(reason) + "! С вас", total, "рублей.")