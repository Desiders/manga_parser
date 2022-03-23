from typing import Optional

from bs4 import BeautifulSoup
from manga_parser.schemas.remanga import (AgeLimit, Category, Genre,
                                          PublisherType, Rank, Status,
                                          TitleType)

STATUS_BY_ID = {
    0: ("completed", "завершено"),
    1: ("ongoing", "продолжается"),
    2: ("hiatus", "заморожен"),
    3: ("no translator", "нет переводчика"),
    4: ("not yet released", "анонс"),
    5: ("licensed", "лицензировано"),
}
STATUS_ID_BY_RAW = {}

for s_id, statuses in STATUS_BY_ID.items():
    for status in statuses:
        STATUS_ID_BY_RAW[status] = s_id

TITLE_TYPE_BY_ID = {
    0: ("manga", "манга"),
    1: ("manhwa", "манхва"),
    2: ("manhua", "маньхуа"),
    3: ("comics", "западный комикс"),
    4: ("rucomix", "рукомикс"),
    5: ("indonesian comics", "индонезийский комикс"),
    6: ("novella", "новелла"),
    7: ("other", "другое"),
}
TITLE_TYPE_ID_BY_RAW = {}

for t_id, title_types in TITLE_TYPE_BY_ID.items():
    for title_type in title_types:
        TITLE_TYPE_ID_BY_RAW[title_type] = t_id

PUBLISHER_TYPE_BY_ID = {
    1: ("translator", "переводчик"),
    2: ("author", "автор"),
    3: ("publisher", "издатель"),
}
PUBLISHER_TYPE_ID_BY_RAW = {}

for p_id, publisher_types in PUBLISHER_TYPE_BY_ID.items():
    for publisher_type in publisher_types:
        PUBLISHER_TYPE_ID_BY_RAW[publisher_type] = p_id

AGE_LIMIT_BY_ID = {
    0: "0+",
    1: "16+",
    2: "18+",
}
AGE_LIMIT_ID_BY_AGE_LIMIT = {
    age_limit: a_id
    for a_id, age_limit in AGE_LIMIT_BY_ID.items()
}

GENRES_BY_ID = {
    2: "боевик", 3: "боевые искусства",
    5: "гарем", 6: "гендерная интрига",
    7: "героическое фэнтези", 8: "детектив",
    9: "дзёсэй", 10: "додзинси",
    11: "драма", 12: "игра",
    13: "история", 14: "киберпанк",
    15: "кодомо", 16: "элементы юмора",
    17: "махо-сёдзё", 18: "меха",
    19: "мистика", 20: "научная фантастика",
    21: "повседневность", 22: "постапокалиптика",
    23: "приключения", 24: "психология",
    25: "романтика", 27: "сверхъестественное",
    28: "сёдзё", 29: "сёдзё-ай",
    30: "сёнэн", 31: "сёнэн-ай",
    32: "спорт", 33: "сэйнэн",
    34: "трагедия", 35: "триллер",
    36: "ужасы", 37: "фантастика",
    38: "фэнтези", 39: "школа",
    40: "этти", 41: "юри",
    42: "эротика", 43: "яой",
    50: "комедия",
}
GENRES_ID_BY_RAW = {
    genre: g_id
    for g_id, genre in GENRES_BY_ID.items()
}

CATEGORIES_BY_ID = {
    5: "веб", 6: "в цвете",
    8: "ёнкома", 10: "сборник",
    11: "сингл", 13: "реинкарнация",
    14: "зомби", 15: "демоны",
    16: "кулинария", 17: "медицина",
    18: "культивация", 19: "зверолюди",
    21: "хикикомори", 22: "магия",
    23: "горничные", 24: "мафия",
    25: "средневековье", 26: "антигерой",
    27: "призраки / духи", 28: "гяру",
    29: "военные", 30: "ниндзя",
    31: "офисные работники", 32: "полиция",
    33: "самураи", 34: "традиционные игры",
    35: "видеоигры", 36: "преступники / криминал",
    37: "девушки-монстры", 38: "монстры",
    39: "музыка", 40: "обратный гарем",
    41: "выживание", 43: "путешествия во времени",
    44: "виртуальная реальность", 45: "боги",
    46: "эльфы", 47: "алхимия",
    48: "ангелы", 49: "антиутопия",
    50: "апокалипсис", 51: "армия",
    52: "артефакты", 54: "борьба за власть",
    55: "будущее", 56: "вестерн",
    57: "владыка демонов", 59: "волшебные существа",
    60: "воспоминания из другого мира", 61: "геймеры",
    62: "гильдии", 63: "гг женщина",
    64: "гг мужчина", 65: "гоблины",
    66: "драконы", 67: "дружба",
    68: "ранги силы", 69: "жестокий мир",
    70: "животные компаньоны", 71: "завоевание мира",
    73: "игровые элементы", 75: "квесты",
    76: "космос", 78: "магическая академия",
    79: "месть", 80: "навыки / способности",
    81: "наёмники", 82: "насилие / жестокость",
    83: "нежить", 85: "пародия",
    86: "подземелья", 87: "политика",
    88: "разумные расы", 89: "роботы",
    90: "рыцари", 91: "система",
    92: "стимпанк", 93: "скрытие личности",
    94: "спасение мира", 95: "супергерои",
    96: "учитель / ученик", 97: "философия",
    99: "шантаж", 108: "лоли",
    109: "тупой гг", 110: "гг имба",
    111: "умный гг", 112: "вампиры",
    113: "оборотни", 114: "управление территорией",
    115: "исекай", 116: "врачи / доктора",
    117: "аристократия", 118: "прокачка",
    121: "амнезия / потеря памяти", 122: "бои на мечах",
    123: "гг не человек", 124: "психодел-упоротость-треш",
    125: "грузовик-сан",
}
CATEGORIES_ID_BY_RAW = {
    category: c_id
    for c_id, category in CATEGORIES_BY_ID.items()
}

RANK_BY_ID = {
    1: "деревянный",
    2: "бронзовый",
    3: "серебряный",
    4: "золотой",
}
RANK_ID_BY_RAW = {
    rank: r_id
    for r_id, rank in RANK_BY_ID.items()
}


def status_by_id(status_id: int) -> Status:
    en_status, ru_status = STATUS_BY_ID[status_id]

    return Status(
        id=status_id,
        en_value=en_status,
        ru_value=ru_status,
    )


def status_id_by_raw(status: str) -> int:
    return STATUS_ID_BY_RAW[status.lower()]


def status_by_raw(status: str) -> Status:
    return status_by_id(status_id_by_raw(status))


def title_type_by_id(title_type_id: int) -> TitleType:
    en_title_type, ru_title_type = TITLE_TYPE_BY_ID[title_type_id]

    return TitleType(
        id=title_type_id,
        en_value=en_title_type,
        ru_value=ru_title_type,
    )


def title_type_id_by_raw(title_type: str) -> int:
    return TITLE_TYPE_ID_BY_RAW[title_type.lower()]


def title_type_by_raw(title_type: str) -> TitleType:
    return title_type_by_id(title_type_id_by_raw(title_type))


def publisher_type_by_id(publisher_id: int) -> PublisherType:
    en_publisher_type, ru_publisher_type = PUBLISHER_TYPE_BY_ID[publisher_id]

    return PublisherType(
        en_value=en_publisher_type,
        ru_value=ru_publisher_type,
    )


def publisher_type_id_by_raw(publisher_type: str) -> int:
    return PUBLISHER_TYPE_ID_BY_RAW[publisher_type.lower()]


def publisher_type_by_raw(publisher_type: str) -> PublisherType:
    return publisher_type_by_id(publisher_type_id_by_raw(publisher_type))


def age_limit_by_id(age_limit_id: int) -> AgeLimit:
    age_limit = AGE_LIMIT_BY_ID[age_limit_id]

    return AgeLimit(
        id=age_limit_id,
        value=age_limit,
    )


def age_limit_id_by_raw(age_limit: str) -> int:
    return AGE_LIMIT_ID_BY_AGE_LIMIT[age_limit.lower()]


def age_limit_by_raw(age_limit: str) -> AgeLimit:
    return age_limit_by_id(age_limit_id_by_raw(age_limit))


def genre_by_id(genre_id: int) -> Genre:
    ru_genre = GENRES_BY_ID[genre_id]

    return Genre(
        id=genre_id,
        value=ru_genre,
    )


def genre_id_by_raw(genre: str) -> int:
    return GENRES_ID_BY_RAW[genre.lower()]


def genre_by_raw(genre: str) -> Genre:
    return genre_by_id(genre_id_by_raw(genre))


def category_by_id(category_id: int) -> Category:
    ru_category = CATEGORIES_BY_ID[category_id]

    return Category(
        id=category_id,
        value=ru_category,
    )


def category_id_by_raw(category: str) -> int:
    return CATEGORIES_ID_BY_RAW[category]


def category_by_raw(category: str) -> Category:
    return category_by_id(category_id_by_raw(category))


def rank_by_id(rank_id: int) -> Rank:
    rank_name = RANK_BY_ID[rank_id]

    return Rank(
        id=rank_id,
        name=rank_name,
    )


def rank_id_by_raw(rank: str) -> int:
    return RANK_ID_BY_RAW[rank]


def rank_by_raw(rank: str) -> Rank:
    return rank_by_id(rank_id_by_raw(rank))


def escape_html_tags(text: str, builder: str = "lxml") -> Optional[str]:
    if text:
        return BeautifulSoup(text, builder).text
    return None  # it's for evidence
