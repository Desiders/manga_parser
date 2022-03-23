import time

from httpx import Client, TimeoutException
from manga_parser import RemangaController, RemangaParser, RemangaRequests
from manga_parser.exceptions.remanga.manga import MangaNotFound

remanga = RemangaController(
    requests=RemangaRequests(client=Client(timeout=10)),
    parser=RemangaParser(),
)


def message_bye():
    print("\n")
    time.sleep(0.05)
    for symbol in "Bye! :)":
        time.sleep(0.05)
        print(symbol, end="", flush=True)


def main():
    text = (
        "Hi, I'm app for search short manga info!\n"
        "Just send me manga's name or \"q\" for exit: "
    )
    while True:
        manga_name = input(text)
        if manga_name == "q":
            message_bye()
            return

        try:
            manga = remanga.manga_search(name=manga_name, count=7)
        except MangaNotFound:
            print("\nManga by this name not found!", end="\n\n")
            continue
        except TimeoutException:
            print(
                "\nSite didn't return anything during 10 seconds!",
                end="\n\n",
            )
            continue
        finally:
            text = (
                "Manga's name or \"q\" for exit: "
            )

        print(
            "-----     -----",
            "     -----     ",
            sep="\n",
        )
        for manga_data in manga:
            time.sleep(0.5)
            print(
                manga_data,
                "     -----     ",
                sep="\n",
            )
        print("-----     -----", end="\n\n")


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt):
        remanga.requests.close()
