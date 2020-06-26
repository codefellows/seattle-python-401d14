import pytest

from graph import Graph, Vertex

def test_add_vertex():

    g = Graph()

    expected = 'spam'

    vertex = g.add_vertex('spam')

    actual = vertex.value

    assert actual == expected

def test_add_edge():

    g = Graph()

    apples = g.add_vertex('apples')

    bananas = g.add_vertex('bananas')

    g.add_edge(apples, bananas)

    assert True, 'Will be fully exercised in get_neighbors tests'

def test_add_edge_interloper():

    g = Graph()

    insider = g.add_vertex('insider')

    outsider = Vertex('outsider')

    with pytest.raises(KeyError):
        g.add_edge(outsider, insider)


def test_get_vertices():
    
    g = Graph()

    apples = g.add_vertex('apples')

    bananas = g.add_vertex('bananas')

    actual = g.get_vertices()

    assert len(actual) == 2


def test_get_neighbors():
    
    g = Graph()

    apple = g.add_vertex('apple')

    banana = g.add_vertex('banana')

    g.add_edge(apple, banana)

    neighbors = g.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor = neighbors[0]

    assert neighbor.vertex.value == 'banana'

    assert neighbor.weight == 1


def test_get_size():

    g = Graph()

    apple = g.add_vertex('apple')

    banana = g.add_vertex('banana')

    assert len(g) == 2










    

