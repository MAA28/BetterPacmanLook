import sys
from colorama import Fore, Style
from clize import run
from rich.table import Table
from rich import print as p

def get_input_text():
    # use stdin if it's full
    if not sys.stdin.isatty():
        input_stream = sys.stdin

    # otherwise, read the given filename
    else:
        try:
            input_filename = sys.argv[1]
        except IndexError:
            message = 'need filename as first argument if stdin is not full'
            raise IndexError(message)
        else:
            input_stream = open(input_filename, 'rU')

    lines = []

    for i, line in enumerate(input_stream):
        lines.append(line.replace('\n', '').replace('    ', ''))

    return lines


def main(n: int = 125):
    lines = get_input_text()
    if not lines:
        print(f'{Fore.RED}Nothing found... Sorry{Style.RESET_ALL}')
        return

    table = Table(title=f'{len(lines) // 2} Result(s)...', header_style='bold purple')
    table.add_column('Index')
    table.add_column('Name', style='bold ')
    table.add_column('Description', style='cyan')
    table.add_column('Version', style='dim')
    table.add_column('✓', style='green')
    table.add_column('Origin', justify='right')

    content = []
    for i in range(0, len(lines), 2):
        prefix = i // 2 + 1

        pure_address = lines[i]

        origin = pure_address.split("/")[0]


        name = pure_address.split("/")[1].split(" ")[0]
        version = pure_address.split(" ")[1] + (pure_address.split(" ")[2] if len(pure_address.split(" ")) == 3 and pure_address.split(" ")[2] != "[installed]" else "")
        installed = '✓' if len(pure_address.split(' ')) == 3 and pure_address.split(' ')[2] == "[installed]" else ''

        description = lines[i + 1]


        table.add_row(*[str(renderable) for renderable in [prefix, name, description, version, installed, origin]])



    p(table)

if __name__ == '__main__':
    run(main)
