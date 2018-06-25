from hypothesis import given, settings, Verbosity
from hypothesis.strategies import text

from ec import encode, decode

@settings(verbosity=Verbosity.verbose)
@given(s=text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
