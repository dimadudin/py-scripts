import random
from bstpostorder import *

run_cases = [
    (4, ["Ebork#0", "Jax#8", "Thoreuth#11", "Marlo#7"]),
    (
        8,
        [
            "Bhurdan#10",
            "Myra#5",
            "Varis#13",
            "Rhogar#17",
            "Thoreuth#11",
            "Velithria#21",
            "Astram#23",
            "Yamil#20",
        ],
    ),
]

submit_cases = run_cases + [
    (
        12,
        [
            "Thoreuth#11",
            "Bhurdan#10",
            "Ember#18",
            "Rhogar#17",
            "Mikel#19",
            "Elian#2",
            "Astram#23",
            "Myra#27",
            "Thoreuth#33",
            "Jax#30",
            "Ebork#22",
            "Bob#34",
        ],
    ),
]


class Character:
    def __init__(self, gamertag):
        self.gamertag = gamertag
        character_names = [
            "Ebork",
            "Astram",
            "Elian",
            "Tarlock",
            "Grog",
            "Myra",
            "Sullivan",
            "Marlo",
            "Jax",
            "Anthony",
            "Bhurdan",
            "Thoreuth",
            "Bob",
            "Varis",
            "Nyx",
            "Luna",
            "Ash",
            "Rhogar",
            "Ember",
            "Mikel",
            "Yamil",
            "Velithria",
        ]
        self.character_name = (
            f"{character_names[gamertag%len(character_names)]}#{gamertag}"
        )

    def __eq__(self, other):
        return self.gamertag == other.gamertag

    def __lt__(self, other):
        return self.gamertag < other.gamertag

    def __gt__(self, other):
        return self.gamertag > other.gamertag

    def __repr__(self):
        return "".join(self.character_name)


def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    return "\n".join(lines)


def format_tree_string(bst_node, lines, level=0):
    if bst_node != None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)


setattr(BSTNode, "__repr__", print_tree)


def get_characters(num):
    random.seed(1)
    characters = []
    gamertags = []
    for i in range(num * 3):
        gamertags.append(i)
    random.shuffle(gamertags)
    gamertags = gamertags[:num]
    for gamertag in gamertags:
        character = Character(gamertag)
        characters.append(character)
    return characters


def char_list_to_string(char_list):
    character_names = []
    for char in char_list:
        character_names.append(char.character_name)
    return character_names


def test(num_characters, expected):
    characters = get_characters(num_characters)
    bst = BSTNode()
    for character in characters:
        bst.insert(character)
    print("=====================================")
    print("Tree:")
    print("-------------------------------------")
    print(bst)
    print("-------------------------------------\n")
    print(f"Expecting: {expected}")
    try:
        actual_bst = BSTNode()
        for character in characters:
            actual_bst.insert(character)
        actual = char_list_to_string(actual_bst.postorder([]))
        print(f"Actual: {actual}")
        if expected == actual:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
