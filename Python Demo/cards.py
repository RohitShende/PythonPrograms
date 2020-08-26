import random


class PlayingCard:

    __all_faces = {
        1: "A", 11: "J", 12: "Q", 13: "K"
    }
    __all_suites = {
        1: "clubs", 2: "diamonds", 3: "hearts", 4: "spades"
    }

    def __init__(self):
        random_fv = random.randint(1, 13)
        random_suit = random.randint(1, 4)

        if 1 < random_fv < 11:
            self.__face_value = str(random_fv)
        else:
            self.__face_value = self.__all_faces[random_fv]

        self.__suit = self.__all_suites[random_suit]

    def get_suit(self):
        return self.__suit

    def get_face_value(self):
        return self.__face_value

    def __str__(self):
        return "{} <{}>".format(self.__face_value, self.__suit)

    def __repr__(self):
        return "{} <{}>".format(self.__face_value, self.__suit)


def main():
    playing_cards = []
    print("You have", end=' ')

    suites = set()
    for i in range(5):
        card = PlayingCard()
        playing_cards.append(card)
        if i != 4:
            print("a {} of {}, ".format(card.get_face_value(), card.get_suit()), end='')
        else:
            print("and a {} of {}".format(card.get_face_value(), card.get_suit()))

        suites.add(card.get_suit())
    if len(suites) == 1:
        print("You have a flush!")


if __name__ == '__main__':
    for i in range(1000):
        main()
