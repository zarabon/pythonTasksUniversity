# Даны строки S и S0. Требуется удалить из строки S все подстроки,
# совпадающие с S0. Если таких подстрок нет, то строку S изменять
# не требуется. (Например, "Приславетсла", "сла" → "Привет").

s = input('s:\n >')
s0 = input('s0:\n >')
print(s.replace(s0, ''))