import sys
from builtins import str, print, exit, KeyError, sorted, ImportError
import argparse


import importlib.metadata


def default():
    print('gumshoe-pdf-composer')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--outputer', default='default')
    args = parser.parse_args()

    eps = importlib.metadata.entry_points()['pdf_composer.output']
    outputers = {
        entrypoint.name: entrypoint for entrypoint in eps
    }

    try:
        outputer = outputers[args.outputer].load()
    except KeyError:
        print(f'outputer {args.outputer} is not available!', file=sys.stderr)
        print(f'available outputers: ({", ".join(sorted(outputers))})')
        return 1

    outputer('Gumshoe PDF Composer')
    return 0


if __name__ == '__main__':
    exit(main())
