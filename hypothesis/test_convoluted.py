from hypothesis import given, settings, Verbosity
import hypothesis.strategies as st
from hypothesis.strategies import one_of


@settings(verbosity=Verbosity.verbose, max_examples=100)
@given(seqs=st.lists(elements=st.lists(elements=st.integers(), min_size=2),min_size=2))
def test_zip_unzip(seqs):
    zipped = list(zip(*seqs))
    unzipped = list(zip(*zipped))
    assert zipped == unzipped
