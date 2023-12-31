import pprint
from pathlib import Path

import homework_8_1.argparser as ap
import homework_8_1.connection as connection
import homework_8_1.seed as seed


def main():
    parser = ap.create_parser()
    args = parser.parse_args()
    data = args.data
    if not data.exists():
        data = Path.cwd() / args.data
    seed.seed(data)
    while True:
        command = input('>')
        commands = ap.parse_command(command)
        # print(commands)
        parsed_commands = ap.parse_commands(commands)
        pprint.pprint(parsed_commands)
        continue

if __name__ == "__main__":
    main()
