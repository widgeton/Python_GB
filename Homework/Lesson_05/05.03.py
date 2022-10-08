# Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

def show_field(field):
    for i in range(len(field)):
        if not i % 3:
            print(f'\n{"-" * 17}')
        print(field[i], end="\t\t")
    print(f"\n{'-' * 17}")


def check_win(field, symb):
    if (field[0] == symb and field[1] == symb and field[2] == symb) or \
            (field[3] == symb and field[4] == symb and field[5] == symb) or \
            (field[6] == symb and field[7] == symb and field[8] == symb) or \
            (field[0] == symb and field[3] == symb and field[6] == symb) or \
            (field[1] == symb and field[4] == symb and field[7] == symb) or \
            (field[2] == symb and field[5] == symb and field[8] == symb) or \
            (field[0] == symb and field[4] == symb and field[8] == symb) or \
            (field[2] == symb and field[4] == symb and field[6] == symb):
        return True
    return False


fld = list(range(1, 10))
show_field(fld)

x = chr(10060)
o = chr(11093)
count = 9
player = x

while count:
    move = int(input(f"{player} move: "))
    if move not in fld:
        print(f"Incorrect input{chr(9940)}")
        continue
    fld.insert(fld.index(move), player)
    fld.remove(move)
    show_field(fld)
    if check_win(fld, x):
        print(f"{x} - WIN{chr(127942)}{chr(127881)}")
        exit()
    player = o if player == x else x
    count -= 1
print(f"Drown game {chr(129309)}")
