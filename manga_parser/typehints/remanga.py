from typing import Optional, Sequence, Type, Union

from manga_parser.schemas.remanga import (AgeLimit, Branch, Category, Chapter,
                                          Genre, Publisher, Status, TitleType)
from manga_parser.schemas.remanga.manga import Manga

CategoryIdType = Union[int, str]
CategoriesIdsType = Optional[Sequence[CategoryIdType]]
CategoryType = Union[CategoryIdType, Category]
CategoriesType = Optional[Sequence[CategoryType]]

GenreIdType = Union[int, str]
GenresIdsType = Optional[Sequence[GenreIdType]]
GenreType = Union[GenreIdType, Genre]
GenresType = Optional[Sequence[GenreType]]

StatusIdType = Union[int, str]
StatusesIdsType = Optional[Sequence[StatusIdType]]
StatusType = Union[StatusIdType, Status]
StatusesType = Optional[Sequence[StatusType]]

TitleTypeIdType = Union[int, str]
TitleTypesIdsType = Optional[Sequence[TitleTypeIdType]]
TitleTypeType = Union[TitleTypeIdType, TitleType]
TitleTypesType = Optional[Sequence[TitleTypeType]]

AgeLimitIdType = Union[int, str]
AgeLimitsIdsType = Optional[Sequence[AgeLimitIdType]]
AgeLimitType = Union[int, str, AgeLimit]
AgeLimitsType = Optional[Sequence[AgeLimitType]]

BranchIdType = Union[int, str]
BranchOrIdType = Union[BranchIdType, Branch]

ChapterIdType = Union[int, str]
ChapterUrlType = str
ChapterShortUrlType = str
ChapterOrIdOrUrlType = Union[
    ChapterIdType, ChapterUrlType, ChapterShortUrlType, Chapter,
]

MangaUrlType = str
MangaShortUrlType = str
MangaOrUrlType = Union[MangaUrlType, MangaShortUrlType, Type[Manga]]

PublisherUrlType = str
PublisherShortUrlType = str
PublisherOrUrlType = Union[
    PublisherUrlType, PublisherShortUrlType, Type[Publisher],
]
