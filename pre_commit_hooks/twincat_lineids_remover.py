import argparse


def fix_file(filename):
    with open(filename, 'r') as fd:
        original_lines = fd.readlines()
    new_lines = []
    changed = False
    for line in original_lines:
        if '<LineId' not in line and 'LineIds>' not in line:
            new_lines.append(line)
            changed = True
    if changed:
        with open(filename, 'w') as fd:
            fd.write(''.join(new_lines))


def main(args=None):
    if args is None:
        parser = argparse.ArgumentParser()
        parser.add_argument('filenames', nargs='*')
        args = parser.parse_args()
    try:
        for filename in args.filenames:
            fix_file(filename)
        return 0
    except Exception as exc:
        print(exc)
        return 1


if __name__ == "__main__":
    exit(main())
