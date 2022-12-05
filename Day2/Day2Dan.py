import os

ROOT = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ROOT, 'input.txt')) as f:
    data = [line.split(" ") for line in f.read().strip().splitlines()]


def part1(data):
    shape_associations = {
        "A": {
            "X": 1,
            "Y": 1,
            "Z": 1 + 6,
        },
        "B": {
            "X": 2 + 6,
            "Y": 2 + 3,
            "Z": 2,
        },
        "C": {
            "X": 3,
            "Y": 3 + 6,
            "Z": 3 + 3,
        },
    }
    score = 0
    for each in data:
        score += shape_associations[each[0]][each[1]]
    return score



def part2(data):
    shape_associations2 = {
        "X": {
            'score': 0,
            'A': 'scissors', 
            'B': 'rock', 
            'C': 'paper'
        },
        "Y": {
            'score': 1,
            'A': 'rock', 
            'B': 'paper', 
            'C': 'scissors'
        },
        "Z": {
            'score': 2,
            'A': 'paper', 
            'B': 'scissors', 
            'C': 'rock'
        },
    }
    shape = {'rock': 1, 'paper': 2, 'scissors': 3}
    score = 0
    for each in data:
        opp, mine = each
        res = shape_associations2[mine][opp]
        score += shape[res]
        score_modifier = shape_associations2[mine]['score']
        score += score_modifier * 3
    return score

if __name__ == '__main__':
    print(part1(data))
    print(part2(data))