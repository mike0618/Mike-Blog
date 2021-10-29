def count_animals(txt: str) -> int:
    animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog",
               "hen", "mole", "duck", "goat"]
    letters = list(txt)
    m_anm = []
    max_animals = []

    def is_exist(animal: str, ltrs: list) -> bool:
        tmp = list(ltrs)
        for ltr in animal:
            if ltr not in tmp:
                return False
            tmp.remove(ltr)
        return True

    def existed_animals(anmls: list, ltrs: list) -> list:
        existed = []
        for animal in anmls:
            if is_exist(animal, ltrs):
                existed.append(animal)
        return existed

    def counter(anmls: list, ltrs: list):
        existed = existed_animals(anmls, ltrs)
        if existed:
            for i in range(len(existed)):
                m_anm.append(existed[i])
                rest_letters = list(ltrs)
                [rest_letters.remove(ltr) for ltr in existed[i]]
                counter(existed[i:], rest_letters)
        if len(m_anm) > len(max_animals):
            max_animals.clear()
            max_animals.extend(m_anm)
        m_anm.clear()

    counter(animals, letters)
    print(max_animals)
    return len(max_animals)


if __name__ == '__main__':
    print(count_animals('goatcode'))
    print(count_animals("cockdogwdufrbir"))
    print(count_animals("dogdogdogdogdog"))
    print(count_animals('acatdgcatogocatdoggoatdct'))
