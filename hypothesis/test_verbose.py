from hypothesis.strategies import floats
from hypothesis import given, settings, Verbosity


@settings(verbosity=Verbosity.verbose)
@given(floats(), floats())
def test_floats_are_commutative(x, y):
    assert x + y == y + x

