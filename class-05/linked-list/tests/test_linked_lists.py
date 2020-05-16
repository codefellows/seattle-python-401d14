import pytest
from linked_list.linked_list import LinkedList, Node


def test_instance():
    ll = LinkedList()
    assert ll.head == None


"""
Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.

Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

"""


def test_insert_empty():
    ll = LinkedList()
    ll.insert("apples")
    assert ll.head.value == "apples"


def test_insert_full():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert ll.head.value == "bananas"
    assert ll.head.next.value == "apples"


def test_str():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert str(ll) == "{ bananas } -> { apples } -> NULL"


def test_node_exception():
    with pytest.raises(TypeError):
        Node("sample", "this is NOT a Node")
