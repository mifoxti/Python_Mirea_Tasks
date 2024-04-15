import deal
import pytest


@deal.pre(lambda x: x > 0)
@deal.post(lambda result: result % 2 == 0)
def divide_by_two(x):
    return x / 2


def test_divide_by_two():
    with pytest.raises(deal.PreContractError):
        divide_by_two(-1)

    with pytest.raises(deal.PostContractError):
        divide_by_two(3)
