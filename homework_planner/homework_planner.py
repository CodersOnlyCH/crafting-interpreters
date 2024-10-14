import datetime
from pathlib import Path
from typing import List

import pytz
import yaml


def planning_dict():
    a = Path('tasks.yaml')
    with a.open() as f:
        return yaml.safe_load(f.read())


def write_plan():
    pass


class Reference(object):
    def __init__(self, dictie):
        if 'Reading_extra' in dictie:
            self.title, self.path = dictie['Reading_extra']['title'], \
                dictie['Reading_extra'][
                    'path']

    def url(self):
        return 'hello'

    @property
    def markdown_link(self):
        return f'[{self.title}]({self.path})'


def homework_this_week(value: dict, target='markdown') -> List[str]:
    week = value["week"]

    labs, course_notes, homework = 'labs', 'course_notes', 'homework'

    list1 = []

    if target == 'markdown':
        labs = "[labs](reference/berkeley_cs61a_material/course_reader_vol_1/labs.pdf)"
        course_notes = "[course notes](reference/berkeley_cs61a_material/course_reader_vol_2/notes.pdf)"
        homework = "[homework](reference/berkeley_cs61a_material/course_reader_vol_1/hw.pdf)"

    if "Reading" in value:
        if value["Reading"] != "":
            list1.extend([f'read the book {value["Reading"]}'])

    if "Reading_extra" in value:
        title = value["Reading_extra"]["title"]
        print(title)
        path = value["Reading_extra"]["path"]
        list1.extend([f'read [{title}]({path})'])

    return list1


def date_generator():
    start_date = datetime.datetime(2021, 3, 24, 18, 30)

    timezone = pytz.timezone("Europe/Zurich")
    d_aware = timezone.localize(start_date)
    yield d_aware
    while True:
        d_aware += datetime.timedelta(weeks=2)
        yield d_aware


def markdown_output():
    target_dir = Path(__file__).parent / 'output'
    target_dir.mkdir(exist_ok=True, parents=True)
    dg = date_generator()
    target = target_dir / 'homework.md'
    with target.open('w') as f:
        all_weeks = planning_dict()
        print(all_weeks)
        for week in all_weeks:
            f.write(f'## Crafting Interpreters Study Group: Chapter {all_weeks[week]["week"]} ({all_weeks[week]["Title"]})\n\n')

            f.write(f'### Homework:\n\n')
            f.write(f'- Read chapter {all_weeks[week]["week"]}: `{all_weeks[week]["reading_urls"]}`\n\n' )
            f.write(f'- do the challenges of the chapter\n\n')

            if 'extra_homework' in all_weeks[week]:

                f.write(f'### Extra Homework:\n\n')
                for entry in all_weeks[week]["extra_homework"]:
                   f.write(f'- {entry}\n')


            f.write(
                f'\n\nWe **review** this work on Review Meeting {all_weeks[week]["week"]} on {all_weeks[week]["Review_Meeting"]}')
            f.write('\n\n')


def discord_output():
    target_dir = Path(__file__).parent / 'output'
    target_dir.mkdir(exist_ok=True, parents=True)
    target = target_dir / 'homework_discord.md'
    with target.open('w') as f:

        all_weeks = planning_dict()
        for week in all_weeks:
            #     f.write(f'{week} ({all_weeks[week]["Theme"]})\n\n')
            for h in homework_this_week(all_weeks[week], target='discord'):
                f.write(f'- {h}\n')
            f.write(
                f'\n\nWe **review** this work on Review Meeting {week} on {all_weeks[week]["Review_Meeting"]}')
            f.write('\n\n')
            link_summary(f)
            f.write('\n\n')


def link_summary(f):
    f.write('repo: https://github.com/AndrewMagerman/wizard-book-study\n')
    base = "https://github.com/AndrewMagerman/wizard-book-study/tree/main/"
    f.write(
        f'labs = {base}reference/berkeley_cs61a_material/course_reader_vol_1/labs.pdf\n')
    f.write(
        f'course_notes = {base}reference/berkeley_cs61a_material/course_reader_vol_2/notes.pdf\n')
    f.write(
        f'homework = {base}reference/berkeley_cs61a_material/course_reader_vol_1/hw.pdf\n\n')


if __name__ == '__main__':
    discord_output()
    markdown_output()
