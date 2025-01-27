from pathlib import Path
from urllib.parse import urlparse

from datetime import datetime, timedelta
from icalendar import Calendar, Event
from zoneinfo import ZoneInfo

import argparse

chapter_urls = [
    'https://craftinginterpreters.com/introduction.html',
    'https://craftinginterpreters.com/a-map-of-the-territory.html',
    'https://craftinginterpreters.com/the-lox-language.html',
    'https://craftinginterpreters.com/scanning.html',
    'https://craftinginterpreters.com/representing-code.html',
    'https://craftinginterpreters.com/parsing-expressions.html',
    'https://craftinginterpreters.com/evaluating-expressions.html',
    'https://craftinginterpreters.com/statements-and-state.html',
    'https://craftinginterpreters.com/control-flow.html',
    'https://craftinginterpreters.com/functions.html',
    'https://craftinginterpreters.com/resolving-and-binding.html',
    'https://craftinginterpreters.com/classes.html',
    'https://craftinginterpreters.com/inheritance.html',
    'https://craftinginterpreters.com/chunks-of-bytecode.html',
    'https://craftinginterpreters.com/a-virtual-machine.html',
    'https://craftinginterpreters.com/scanning-on-demand.html',
    'https://craftinginterpreters.com/compiling-expressions.html',
    'https://craftinginterpreters.com/types-of-values.html',
    'https://craftinginterpreters.com/strings.html',
    'https://craftinginterpreters.com/hash-tables.html',
    'https://craftinginterpreters.com/global-variables.html',
    'https://craftinginterpreters.com/local-variables.html',
    'https://craftinginterpreters.com/jumping-back-and-forth.html',
    'https://craftinginterpreters.com/calls-and-functions.html',
    'https://craftinginterpreters.com/closures.html',
    'https://craftinginterpreters.com/garbage-collection.html',
    'https://craftinginterpreters.com/classes-and-instances.html',
    'https://craftinginterpreters.com/methods-and-initializers.html',
    'https://craftinginterpreters.com/superclasses.html',
    'https://craftinginterpreters.com/optimization.html',
]
dates_with_no_holidays = [
    [2025, 1, 9, 19, 0],
    [2025, 1, 23, 19, 0],
    [2025, 2, 13, 19, 0],
    [2025, 2, 27, 19, 0],
    [2025, 3, 13, 19, 0],
    [2025, 3, 27, 19, 0],
    [2025, 4, 10, 19, 0],
    [2025, 5, 8, 19, 0],
    [2025, 5, 22, 19, 0],
    [2025, 6, 12, 19, 0],
    [2025, 6, 26, 19, 0],
    [2025, 7, 10, 19, 0],
    [2025, 8, 28, 19, 0],
    [2025, 9, 11, 19, 0],
    [2025, 9, 25, 19, 0],
    [2025, 10, 23, 19, 0],
    [2025, 11, 13, 19, 0],
    [2025, 11, 27, 19, 0],
    [2025, 12, 11, 19, 0],
    [2026, 1, 8, 19, 0],
    [2026, 1, 22, 19, 0],
    [2026, 2, 26, 19, 0],
    [2026, 3, 12, 19, 0],
    [2026, 3, 26, 19, 0],
    [2026, 4, 9, 19, 0],
    [2026, 5, 14, 19, 0],
    [2026, 5, 28, 19, 0],
    [2026, 6, 11, 19, 0],
    [2026, 6, 25, 19, 0],
    [2026, 7, 9, 19, 0],
    [2026, 8, 27, 19, 0],
    [2026, 9, 10, 19, 0],
    [2026, 9, 24, 19, 0],
    [2026, 10, 8, 19, 0],
    [2026, 10, 22, 19, 0],
    [2026, 11, 12, 19, 0],
    [2026, 11, 26, 19, 0],
    [2026, 12, 10, 19, 0],
]
# mapping here because sometimes I want two chapters in one session, perhaps two sessions on a single chapter?
sessions_to_chapters = {1: [1],
                        2: [2, 3],
                        3: [4],
                        4: [5],
                        5: [6],
                        6: [7],
                        7: [8],
                        8: [9],
                        9: [10],
                        10: [11],
                        11: [12],
                        12: [13],
                        13: [14],
                        14: [15],
                        15: [16],
                        16: [17],
                        17: [18],
                        18: [19],
                        19: [20],
                        20: [21],
                        21: [22],
                        22: [23],
                        23: [24],
                        24: [25],
                        25: [26],
                        26: [27],
                        27: [28],
                        28: [29],
                        29: [30],
                        }


def url_to_title(url: str) -> str:
    a = urlparse(url)
    a = a.path
    a = a.lstrip('/')
    a = a.replace('-', ' ')
    a = a.replace('.html', '')
    a = a.capitalize()
    return a


def chapter_list() -> list[str]:
    result = list()
    for index, chapter_url in enumerate(chapter_urls, start=1):
        result.append(f"Chapter {index}: {chapter_url}")
    return result


def content_per_session():
    cl = chapter_list()
    for session, chapters in sessions_to_chapters.items():
        relevant_chapter_list = [cl[index - 1] for index in chapters]

        chapter_descriptions = " ".join(relevant_chapter_list)
        titles = [url_to_title(chapter_urls[index - 1]) for index in chapters]
        title_descriptions = " / ".join(titles)
        yield (session, chapter_descriptions, title_descriptions)


def markdown_output():
    date_index = 0
    for session, chapter_description, Title in content_per_session():
        print(f'## Crafting Interpreters Study Group:  Session {session} ({Title})\n\n')
        print(f'### Homework:\n\n')
        print(f'- Read {chapter_description}\n\n')
        print(f'### Extra Homework:\n\n')
        print(f'- do the challenges of the chapter\n\n')
        print(f'\n\nWe **review** this work on {datetime(*dates_with_no_holidays[date_index]).strftime("%A, %d. %B %Y %H:%M")}\n\n')
        date_index += 1


def ics():
    cal = Calendar()
    for date, (session, description, title) in zip(dates_with_no_holidays, content_per_session()):
        date = datetime(tzinfo=ZoneInfo("Europe/Zurich"), *date)
        event = Event()
        event.add('summary', 'Crafting Interpreters Study Group')
        event.add('description', f'Crafting Interpreters Study Group [{session}]\n\n{title}\n\n{description}')
        event.add('dtstart', date)
        event.add('dtend', date + timedelta(hours=1, minutes=30))
        cal.add_component(event)
    print(cal.to_ical().decode('utf-8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ics", action="store_true")
    parser.add_argument("-m", "--markdown", action="store_true")
    args = parser.parse_args()

    if args.markdown:
        markdown_output()
    elif args.ics:
        ics()
    else:
        for c in content_per_session():
            print(c)
