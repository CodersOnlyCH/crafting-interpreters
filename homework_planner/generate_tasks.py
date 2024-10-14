from pathlib import Path
from urllib.parse import urlparse

import yaml

chapters = [
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
dates = [
    'Thursday 09 January 2025, 19:00 CET',
    'Thursday 23 January 2025, 19:00 CET',
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


def translate_url_for_title(url: str) -> str:
    a = urlparse(url)
    a = a.path
    a = a.lstrip('/')
    a = a.replace('-', ' ')
    a = a.replace('.html', '')
    a = a.capitalize()
    print(a)
    return a


def generate_tasks():
    result = dict()
    tasks_file = Path(__file__).parent / 'output' / 'tasksinput.yml'
    with tasks_file.open(mode='w') as f:
        for index, data in enumerate(zip(chapters, dates)):
            chapter, date = data
            i = index + 1
            result.update({f"Week {i:02d}": {"week": index + 1,
                                             "Title": translate_url_for_title(chapter),
                                             "reading_urls": chapter,
                                             "Review_Meeting": date},
                           })

        yaml.dump(result, f, default_flow_style=False)
        print(tasks_file)


if __name__ == '__main__':
    generate_tasks()
