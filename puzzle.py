import logic
AKnight = logic.Symbol("A is a Knight")
AKnave = logic.Symbol("A is a Knave")
A_said_knave = logic.Symbol("A said 'I am a Knave'")


BKnight = logic.Symbol("B is a Knight")
BKnave = logic.Symbol("B is a Knave")

CKnight = logic.Symbol("C is a Knight")
CKnave = logic.Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = logic.And(
    logic.Or(AKnight,AKnave),
    logic.Not(logic.And(AKnight, AKnave)),
    logic.Implication(AKnight, logic.And(AKnight, AKnave))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = logic.And(
    logic.Or(AKnight, AKnave),
    logic.Not(logic.And(AKnight, AKnave)),
    logic.Or(BKnight, BKnave),
    logic.Not(logic.And(BKnight, BKnave)),

    logic.Implication(AKnight, logic.And(AKnave, BKnave)),
    logic.Implication(AKnave, logic.Not(logic.And(AKnave, BKnave)))
)



# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = logic.And(
    logic.Or(AKnight, AKnave),
    logic.Not(logic.And(AKnight, AKnave)),
    logic.Or(BKnight, BKnave),
    logic.Not(logic.And(BKnight, BKnave)),

    logic.Implication(AKnight, logic.Or(logic.And(AKnight, BKnight), logic.And(AKnave, BKnave))),
    logic.Implication(AKnave, logic.Not(logic.Or(logic.And(AKnight, BKnight), logic.And(AKnave, BKnave)))),

    logic.Implication(BKnight, logic.Or(logic.And(AKnight, BKnave), logic.And(AKnave, BKnight))),
    logic.Implication(BKnave, logic.Not(logic.Or(logic.And(AKnight, BKnave), logic.And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = logic.And(
    # A, B, and C must be either knight or knave, not both
    logic.Or(AKnight, AKnave),
    logic.Not(logic.And(AKnight, AKnave)),
    logic.Or(BKnight, BKnave),
    logic.Not(logic.And(BKnight, BKnave)),
    logic.Or(CKnight, CKnave),
    logic.Not(logic.And(CKnight, CKnave)),

    # Link A's truthfulness with what A says ("I am a knave")
    logic.Implication(AKnight, logic.Implication(A_said_knave, AKnave)),
    logic.Implication(AKnave, logic.Implication(A_said_knave, logic.Not(AKnave))),

    # B says A said "I am a knave"
    logic.Implication(BKnight, A_said_knave),
    logic.Implication(BKnave, logic.Not(A_said_knave)),

    # B says: "C is a knave"
    logic.Implication(BKnight, CKnave),
    logic.Implication(BKnave, logic.Not(CKnave)),

    # C says: "A is a knight"
    logic.Implication(CKnight, AKnight),
    logic.Implication(CKnave, logic.Not(AKnight))
)




def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave, A_said_knave]
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
                if logic.model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
