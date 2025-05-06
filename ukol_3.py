def vytvor_utulek():
    return{
        "jmeno":"Arnold",
        "druh":"pes",
        "vek":10
    }

def pridej_zvire(utulek, druh, jmeno, vek):
    utulek[jmeno] = input("zadej jmeno")
    utulek[druh] = input("zadej druh zvířete")
    utulek[vek] = input("zadej vek")
    
def vypis_podle_druhu(utulek, druh):
    for jmeno, info in utulek.items():
        if info["druh"] == druh:
            print(f"{jmeno} je {info['druh']} a je jí {info['vek']} let.")

vytvor_utulek()
pridej_zvire("utulek", "kočka", "Barta", "7")
    
    