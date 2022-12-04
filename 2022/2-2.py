import pandas as pd

OUTCOMES = {
    # Formatted as (opponent throw, desired outcome)
    ('rock', 'loss'): "scissors",
    ('paper', 'loss'): "rock",
    ('scissors', 'loss'): "paper",
    ('rock', 'tie'): "rock",
    ('paper', 'tie'): "paper",
    ('scissors', 'tie'): "scissors",
    ('rock', 'win'): "paper",
    ('paper', 'win'): "scissors",
    ('scissors', 'win'): "rock",
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
        "X": "loss",
        "Y": "tie",
        "Z": "win",
    }

    guide = guide.replace(replace_dict)

    return guide


def compare(guide):

    throw_outcome = (guide['opponent_throw'], guide['outcome'])
    player_throw = OUTCOMES[throw_outcome]

    return player_throw


if __name__ == "__main__":

    csv_fn = "2_data.csv"

    guide = pd.read_csv(csv_fn, header=None, names=['opponent_throw', 'outcome'])
    guide = convert_to_rps(guide)

    guide['player_throw'] = guide.apply(compare, axis=1)
    guide['throw_pts'] = guide['player_throw'].map(POINT_VALUES)
    guide['outcome_pts'] = guide['outcome'].map(POINT_VALUES)

    total_pts = guide['throw_pts'].sum() + guide['outcome_pts'].sum()
    print(total_pts)
