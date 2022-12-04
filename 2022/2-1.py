# Challenge: use the pandas library

import pandas as pd

OUTCOMES = {
    # Formatted as (opponent throw, your throw)
    ('rock', 'rock'): "tie",
    ('paper', 'paper'): "tie",
    ('scissors', 'scissors'): "tie",
    ('rock', 'scissors'): "loss",
    ('paper', 'rock'): "loss",
    ('scissors', 'paper'): "loss",
    ('rock', 'paper'): "win",
    ('paper', 'scissors'): "win",
    ('scissors', 'rock'): "win",
}

POINT_VALUES = {
    # Points from throw
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    # Points from outcome
    'loss': 0,
    'tie': 3,
    'win': 6,
}


def convert_to_rps(guide):

    replace_dict = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    guide = guide.replace(replace_dict)

    return guide


def compare(guide):

    throws = (guide['opponent_throw'], guide['player_throw'])
    outcome = OUTCOMES[throws]

    return outcome


if __name__ == "__main__":

    csv_fn = "2_data.csv"

    guide = pd.read_csv(csv_fn, header=None, names=['opponent_throw', 'player_throw'])
    guide = convert_to_rps(guide)

    guide['outcome'] = guide.apply(compare, axis=1)
    guide['throw_pts'] = guide['player_throw'].map(POINT_VALUES)
    guide['outcome_pts'] = guide['outcome'].map(POINT_VALUES)

    total_pts = guide['throw_pts'].sum() + guide['outcome_pts'].sum()
    print(total_pts)
