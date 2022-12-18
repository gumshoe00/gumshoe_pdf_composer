import sys
from builtins import str, print, exit, KeyError, sorted, ImportError
import argparse

import importlib_metadata


def default(*args, **kwargs):
    print(args, '\n', kwargs)


class App:
    def __init__(self):
        """init App


        Example:

            outputers (entrypoints - including plugins): {

                'default': EntryPoint(name='default',
                                      value='pdfcomposer.__main__:default',
                                      group='pdfcomposer.output'),

                'compose': EntryPoint(name='compose',
                                      value='pdfcomposer_compose.__main__:main',
                                      group='pdfcomposer.output')
            }


        """
        eps = importlib_metadata.entry_points().select(group='pdfcomposer.output')
        self._outputers = {
            entrypoint.name: entrypoint for entrypoint in eps
        }

    def __call__(self, plugin='default', *args, **kwargs):
        try:
            outputer = self._outputers[plugin].load()
        except KeyError:
            print(f'outputer {plugin} is not available!', file=sys.stderr)
            print(f'available outputers: ({", ".join(sorted(self._outputers))})')
            return 1
        else:
            return outputer(*args, **kwargs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--outputer', default='default')
    parser.add_argument('--args', nargs='*')
    parser.add_argument('--kwargs', nargs='*', help='Example: title="My PDF" author="John Doe" subject="My first PDF" creator="John Doe"')
    parser_args = parser.parse_args()

    _args = []
    _kws = {}
    if parser_args.args:
        _args.extend(parser_args.args)

    if parser_args.kwargs:
        for _kv_str in parser_args.kwargs.split(' '):
            _k, _v = _kv_str.split('=')
            _kws[_k] = _v

    outputer = App()
    outputer(parser_args.outputer, *_args, **_kws)
    return 0


if __name__ == '__main__':
    exit(main())
