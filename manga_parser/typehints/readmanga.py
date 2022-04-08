from typing import Type, Union

from manga_parser.schemas.readmanga.manga import Manga

MangaUrlType = str
MangaShortUrlType = str
MangaOrUrlType = Union[MangaUrlType, MangaShortUrlType, Type[Manga]]
