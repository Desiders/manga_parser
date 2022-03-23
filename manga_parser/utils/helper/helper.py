from itertools import islice
from typing import Sequence, Optional


def limit_offset(
    data: Sequence,
    offset: int,
    limit: Optional[int] = None,
) -> list:
    return list(islice(islice(data, offset, None), limit))


def reverse(data: Sequence) -> Sequence:
    return data[::-1]
