import pandas as pd
import pandas.testing

try:
    import polars as pl
    import polars.testing
except ImportError:
    pass

from .._dispatch import dispatch


@dispatch
def assert_frame_equal(left, right):
    raise NotImplementedError()


@assert_frame_equal.specialize("pandas", argument_type="DataFrame")
def _assert_frame_equal_pandas(left, right):
    return pd.testing.assert_frame_equal(left, right)


@assert_frame_equal.specialize("polars", argument_type="DataFrame")
def _assert_frame_equal_polars(left, right):
    return pl.testing.assert_frame_equal(left, right)
