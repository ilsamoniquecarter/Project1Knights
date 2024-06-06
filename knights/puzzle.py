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
    Or(A_knight, A_knave),
    Not(And(A_knight, A_knave)),
    Implication(A_knight, And(A_knight, A_knave)),
    Implication(A_knave, Not(And(A_knight, A_knave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(A_knight, A_knave),
    Not(And(A_knight, A_knave)),
    Or(B_knight, B_knave),
    Not(And(B_knight, B_knave)),
    Implication(A_knight, And(A_knave, B_knave)),
    Implication(A_knave, Not(And(A_knave, B_knave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(A_knight, A_knave),
    Not(And(A_knight, A_knave)),
    Or(B_knight, B_knave),
    Not(And(B_knight, B_knave)),
    Implication(A_knight, Or(And(A_knight, B_knight), And(A_knave, B_knave))),
    Implication(A_knave, Not(Or(And(A_knight, B_knight), And(A_knave, B_knave)))),
    Implication(B_knight, Or(And(A_knight, B_knave), And(A_knave, B_knight))),
    Implication(B_knave, Not(Or(And(A_knight, B_knave), And(A_knave, B_knight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(A_knight, A_knave),
    Not(And(A_knight, A_knave)),
    Or(B_knight, B_knave),
    Not(And(B_knight, B_knave)),
    Or(C_knight, C_knave),
    Not(And(C_knight, C_knave)),
    # A says "I am a knight." or "I am a knave."
    Implication(A_knight, Or(A_knight, A_knave)),
    Implication(A_knave, Not(Or(A_knight, A_knave))),
    # B says "A said 'I am a knave.'"
    Implication(B_knight, A_knave),
    Implication(B_knave, Not(A_knave)),
    # B says "C is a knave."
    Implication(B_knight, C_knave),
    Implication(B_knave, Not(C_knave)),
    # C says "A is a knight."
    Implication(C_knight, A_knight),
    Implication(C_knave, Not(A_knight))
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
