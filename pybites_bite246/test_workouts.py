import pytest

from workouts import print_workout_days

@pytest.mark.parametrize(
    "test_input, expected",[
        ("upper", "Mon, Thu\n"),
        ("lower", "Tue, Fri\n"),
        ("cardio", "Wed\n"),
        ("brain", "No matching workout\n")
    ]
)
def test_print_workout(capsys, test_input, expected):
    print_workout_days(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected 

