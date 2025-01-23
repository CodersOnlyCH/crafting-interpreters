from pathlib import Path
from urllib.parse import urlparse

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
    'Thursday 09 January 2025, 19:00 CET',
    'Thursday 23 January 2025, 19:00 CET',
    'Thursday 13 February 2025, 19:00 CET',
    'Thursday 27 February 2025, 19:00 CET',
    'Thursday 13 March 2025, 19:00 CET',
    'Thursday 27 March 2025, 19:00 CET',
    'Thursday 10 April 2025, 19:00 CET',
    'Thursday 08 May 2025, 19:00 CET',
    'Thursday 22 May 2025, 19:00 CET',
    'Thursday 12 June 2025, 19:00 CET',
    'Thursday 26 June 2025, 19:00 CET',
    'Thursday 10 July 2025, 19:00 CET',
    'Thursday 28 August 2025, 19:00 CET',
    'Thursday 11 September 2025, 19:00 CET',
    'Thursday 25 September 2025, 19:00 CET',
    'Thursday 23 October 2025, 19:00 CET',
    'Thursday 13 November 2025, 19:00 CET',
    'Thursday 27 November 2025, 19:00 CET',
    'Thursday 11 December 2025, 19:00 CET',
    'Thursday 08 January 2026, 19:00 CET',
    'Thursday 22 January 2026, 19:00 CET',
    'Thursday 26 February 2026, 19:00 CET',
    'Thursday 12 March 2026, 19:00 CET',
    'Thursday 26 March 2026, 19:00 CET',
    'Thursday 09 April 2026, 19:00 CET',
    'Thursday 14 May 2026, 19:00 CET',
    'Thursday 28 May 2026, 19:00 CET',
    'Thursday 11 June 2026, 19:00 CET',
    'Thursday 25 June 2026, 19:00 CET',
    'Thursday 09 July 2026, 19:00 CET',
    'Thursday 27 August 2026, 19:00 CET',
    'Thursday 10 September 2026, 19:00 CET',
    'Thursday 24 September 2026, 19:00 CET',
    'Thursday 08 October 2026, 19:00 CET',
    'Thursday 22 October 2026, 19:00 CET',
    'Thursday 12 November 2026, 19:00 CET',
    'Thursday 26 November 2026, 19:00 CET',
    'Thursday 10 December 2026, 19:00 CET',
    'Thursday 24 December 2026, 19:00 CET'
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
        result.append(f"chapter {index}: {chapter_url}")
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
    target_dir = Path(__file__).parent / 'output'
    target_dir.mkdir(exist_ok=True, parents=True)
    target = target_dir / 'Planning.md'
    date_index = 0
    with target.open('w') as f:
        for session, chapter_description, Title in content_per_session():
            f.write(f'## Crafting Interpreters Study Group:  Session {session} ({Title})\n\n')
            f.write(f'### Homework:\n\n')
            f.write(f'- Read {chapter_description}\n\n')
            f.write(f'### Extra Homework:\n\n')
            f.write(f'- do the challenges of the chapter\n\n')
            f.write(f'\n\nWe **review** this work on {dates_with_no_holidays[date_index]}\n\n')
            date_index += 1


if __name__ == '__main__':
    markdown_output()
    for c in content_per_session():
        print(c)
