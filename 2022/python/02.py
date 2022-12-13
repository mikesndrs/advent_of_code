import numpy as np


def main():
    input_filename = '2022/inputs/02.txt'
    with open(input_filename) as f:
        text = f.read()
        lists = text.split('\n')
        input = [x.split(' ') for x in lists[:-1]]

    mapping_dict = {
        'A': 'R',
        'B': 'P',
        'C': 'S',
        'X': 'R',
        'Y': 'P',
        'Z': 'S',
    }

    # dict[opp][you] = outcome
    matchup_dict = {
        'R': {
            'R': 'draw',
            'P': 'win',
            'S': 'lose',
        },
        'P': {
            'R': 'lose',
            'P': 'draw',
            'S': 'win',
        },
        'S': {
            'R': 'win',
            'P': 'lose',
            'S': 'draw',
        },
    }

    matchup_score_dict = {
        'lose': 0,
        'draw': 3,
        'win': 6,
    }

    rps_dict = {
        'R': 1,
        'P': 2,
        'S': 3,
    }

    score_list = []
    for opponent_move, your_move in input:
        opp = mapping_dict[opponent_move]
        you = mapping_dict[your_move]
        outcome = matchup_dict[opp][you]
        score_list.append(
            matchup_score_dict[outcome] + rps_dict[you]
        )

    result1 = np.sum(np.array(score_list))
    print(result1)

    # 202-12-02 2nd puzzle
    mapping_dict = {
        'A': 'R',
        'B': 'P',
        'C': 'S',
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win',
    }

    # dict[opp][outcome] = you
    matchup_dict = {
        'R': {
            'lose': 'S',
            'draw': 'R',
            'win': 'P',
        },
        'P': {
            'lose': 'R',
            'draw': 'P',
            'win': 'S',
        },
        'S': {
            'lose': 'P',
            'draw': 'S',
            'win': 'R',
        },
    }

    score_list = []
    for opponent_move, your_move in input:
        opp = mapping_dict[opponent_move]
        outcome = mapping_dict[your_move]
        you = matchup_dict[opp][outcome]
        score_list.append(
            matchup_score_dict[outcome] + rps_dict[you]
        )

    result1 = np.sum(np.array(score_list))
    print(result1)


if __name__ == '__main__':
    main()
