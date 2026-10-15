# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: ТИХИЙ КОЛОДЕЦ»
# Автор: Иван Иванов
# Дата: сентябрь 2026
#
# Пункт 4 — 'резвести лагерь' герой строит себе убежище
# и слушает, что происходит в темноте. Пока
# пункт только выводится в меню — обрабатывать
# его будем на третьем занятии.
# ================================================

title = "ПОДЗЕМЕЛЬЕ: АДСКИЕ ШАХТЫ"
frame = "=" * 30
print(frame)
print(" " + title + " ")
print(frame)
print()
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты попал в адские шахты, здесь летают адские щенки и много лавы.")
print()
print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")
health = int(input())
strength = int(input())
agility = int(input())
vinos = int(input())
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2  
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Выносливость: {vinos}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
print("Что делаешь?")
print("1 - осмотреться")
print("2 - идти вперёд")
print("3 - отдохнуть")
print("4 - развести лагерь")
print("5 - крикнуть")
print()
choice = input()
print()






title = f"Удачи {hero_name}!"
frame_length = len(title) + 2
frame = "*" * frame_length
print(frame)
print(f" {title} ")
print(frame)