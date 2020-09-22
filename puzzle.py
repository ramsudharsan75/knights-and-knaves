from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),

    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))

    # Or(And(AKnight, AKnave), AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))

    # Or(
    #     And(AKnave, Not(And(AKnave, BKnave))),
    #     And(AKnave, And(AKnight, BKnave)),
    #     And(AKnave, And(AKnave, BKnight)),
    # )
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    Implication(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))

    # Or(And(AKnave, BKnight), And(AKnight, BKnight)),
    # Or(
    #     And(AKnave, BKnight),
    #     And(AKnave, BKnave)
    # )
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave)),
    Or(CKnave, CKnight),
    Not(And(CKnight, CKnave)),


    Implication(AKnight, And(Or(AKnight, AKnave))),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    # Doesn't matter if A said anything - B could be either knave/knight
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave)

    # Or(
    #     AKnight,
    #     And(AKnave, And(AKnight, AKnave))
    # ),
    # Or(
    #     And(BKnight, AKnave),
    #     BKnave  # A may/may not have said anything
    # ),
    # Or(
    #     And(BKnight, CKnave),
    #     And(BKnave, CKnight)
    # ),
    # Or(
    #     And(CKnight, AKnight),
    #     And(CKnave, AKnave)
    # )
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
