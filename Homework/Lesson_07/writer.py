def w_in_txt(tpl, address):
    with open(f"{address}", "a") as file:
        file.write("-".join(tpl)+"\n")
