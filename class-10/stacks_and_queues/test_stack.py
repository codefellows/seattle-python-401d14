import pytest

from stack import Stack

def test_push_one_item():
    fruits = Stack()
    fruits.push('apple')
    expected = 'apple'
    actual = fruits.peek()
    assert actual == expected

def test_pop_items():
    dishes = Stack()
    dishes.push('yellow dish')
    dishes.push('mom dish')
    dishes.push('cat dish')
    expected = 'mom dish'
    dishes.pop()
    actual = dishes.pop()
    assert actual == expected

def test_is_empty():
    paranths = Stack()
    paranths.push('(')
    paranths.push(')')
    paranths.pop()
    paranths.pop()
    actual = paranths.is_empty()
    expected = True
    assert actual == expected
