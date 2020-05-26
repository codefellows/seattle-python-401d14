import pytest

from tests.flow.flo import Flo


@pytest.mark.skip("pending")
def test_hot_dice():
    """When all dice are used without a zilch
    then user gets 6 fresh dice and continues turn.
    """
    Flo.test("tests/flow/hot_dice.txt")


@pytest.mark.skip("pending")
def test_cheat_and_fix():
    """Cheating (or typos) should not be allowed.
    Therefore the user's input must be validated
    If invalid prompt user for re-entry
    """

    Flo.test("tests/flow/cheat_and_fix.txt")


@pytest.mark.skip("pending")
def test_zilch():
    """
    No scoring dice results in a 'zilch'
    which wipes away shelved points
    and ends turn
    """
    Flo.test("tests/flow/zilch.txt")
