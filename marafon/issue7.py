from itertools import product


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
        if m_anm:
            m_anm.pop()

    counter(animals, letters)
    print(max_animals)
    return len(max_animals)


def count_animals2(txt):
    animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog",
               "hen", "mole", "duck", "goat"]

    def counter(anml):
        exist = True
        ltrs = list(txt)
        count = 0
        while exist:
            for ltr in anml:
                if ltr not in ltrs:
                    exist = False
                    break
                ltrs.remove(ltr)
            else:
                count += 1
        return count

    def check(d: dict):
        strn = ''
        tmp = list(txt)
        for k, v in d.items():
            strn += k * v
        if len(strn) <= len(txt):
            for ltr in strn:
                if ltr not in tmp:
                    return False
                tmp.remove(ltr)
            return True
        return False

    counted = {}
    for a in animals:
        num = counter(a)
        if num:
            counted[a] = num

    for n in range(sum(counted.values())):
        for p in product(range(max(counted.values()) + 1), repeat=len(counted)):
            if sum(p) == n:
                dict_counted = counted.copy()
                for i, a in enumerate(dict_counted):
                    if p[i] <= dict_counted[a] and p[i]:
                        dict_counted[a] -= p[i]
                if check(dict_counted):
                    result = {k: v for k, v in dict_counted.items() if v}
                    print(result)
                    return sum(result.values())


if __name__ == '__main__':
    print(count_animals('goatcode'))
    print(count_animals("cockdogwdufrbir"))
    print(count_animals("dogdogdogdogdog"))
    print(count_animals('acatdgcatogocatdoggoatdct'))
    print(count_animals('cockdogwdufrbiraier' * 3))

    print(count_animals2('goatcode'))
    print(count_animals2("cockdogwdufrbir"))
    print(count_animals2("dogdogdogdogdog"))
    print(count_animals2('acatdgcatogocatdoggoatdct'))
    print(count_animals2('cockdogwdufrbiraier' * 3))
