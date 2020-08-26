from random import randint


suites = ["spade", "hearts", "club", "diamond"]
face_value = list(range(2, 11)) + ["A", "J", "Q", "K"]


def pick_a_card():
    fv_r = randint(0, len(face_value)-1)
    suites_r = randint(0, len(suites)-1)
    card = (suites[suites_r], face_value[fv_r])
    return card


def main():
    card_set = set()
    suite_set = set()
    while len(card_set) != 3:
        card = pick_a_card()
        suite_set.add(card[0])
        card_set.add(card)

    print(card_set)
    if len(suite_set) == 1:
        print("You Win !!!")


for i in range(1000):
    main()