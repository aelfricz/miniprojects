import collections

node = collections.namedtuple("node", "data left right")

leaf = lambda data: node(data, None, None)

tree = node("a",
        node("b", None, None),
        node("c", node("d", leaf("e"), leaf("f")), None)
        )

def next_layer(*nodes):
    #return list(filter(None, [n.left for n in nodes] + [n.right for n in nodes]))
    return list(filter(None, sum(([n.left, n.right] for n in nodes), [])))


def test_next_layer():
    assert not next_layer(node("x", None, None))
    assert next_layer(node("x", node("y","z",None), None))

def node_names(*nodes):
    #print(nodes)
    return " ".join(n.data for n in nodes)

x = node("foo", 34, 56)
assert x.data == "foo"
assert x.left == 34
assert x.right == 56

def layer_by_layer(root):
    nodes = [root]
    while nodes:
        yield node_names(*nodes)
        nodes = next_layer(*nodes)

import pytest

def test_layer_by_layer():
    tree = node("x", leaf("12"), node("10",leaf("11"),None))
    gen = layer_by_layer(tree)
    assert next(gen) == "x"
    assert next(gen) == "12 10"
    assert next(gen) == "11"

def test_complex_tree():
    tree = node("x",
                node("12",leaf("13"),leaf("14")),
                node("10",leaf("11"),leaf("15")),
                )
    gen = layer_by_layer(tree)
    assert next(gen) == "x"
    assert next(gen) == "12 10"
    assert next(gen) == "13 14 11 15"


for layer in layer_by_layer(tree):
    print(layer)
