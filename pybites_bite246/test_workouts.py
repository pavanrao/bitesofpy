import pytest

from workouts import print_workout_days


def test_print_workout_days_upper(capsys):
    print_workout_days("upper")
    captured = capsys.readouterr()
    assert captured.out=="Mon, Thu\n"

def test_print_workout_days_lower(capsys):
    print_workout_days("lower")
    captured = capsys.readouterr()
    assert captured.out=="Tue, Fri\n"

def test_print_workout_days_cardio(capsys):
    print_workout_days("cardio")
    captured = capsys.readouterr()
    assert captured.out=="Wed\n"

def test_print_workout_days_no_match(capsys):
    print_workout_days("brain")
    captured = capsys.readouterr()
    assert captured.out=="No matching workout\n"