from typing import Optional, Sequence, Union

from manga_parser.schemas.remanga import (AgeLimit, Branch, Category, Chapter,
                                          Genre, Status, TitleType)

CategoryTypeRaw = Union[int, str]
CategoryTypesRaw = Optional[Sequence[CategoryTypeRaw]]
CategoryType = Union[CategoryTypeRaw, Category]
CategoryTypes = Optional[Sequence[CategoryType]]

GenreTypeRaw = Union[int, str]
GenreTypesRaw = Optional[Sequence[GenreTypeRaw]]
GenreType = Union[GenreTypeRaw, Genre]
GenreTypes = Optional[Sequence[GenreType]]

StatusTypeRaw = Union[int, str]
StatusTypesRaw = Optional[Sequence[StatusTypeRaw]]
StatusType = Union[StatusTypeRaw, Status]
StatusTypes = Optional[Sequence[StatusType]]

TitleTypeTypeRaw = Union[int, str]
TitleTypeTypesRaw = Optional[Sequence[TitleTypeTypeRaw]]
TitleTypeType = Union[TitleTypeTypeRaw, TitleType]
TitleTypeTypes = Optional[Sequence[TitleTypeType]]

AgeLimitTypeRaw = Union[int, str]
AgeLimitTypesRaw = Optional[Sequence[AgeLimitTypeRaw]]
AgeLimitType = Union[int, str, AgeLimit]
AgeLimitTypes = Optional[Sequence[AgeLimitType]]

BranchTypeRaw = Union[int, str]
BranchType = Union[BranchTypeRaw, Branch]

ChapterRaw = Union[int, str]
ChapterOrUrlRaw = Union[int, str]
ChapterOrUrlType = Union[ChapterOrUrlRaw, Chapter]
