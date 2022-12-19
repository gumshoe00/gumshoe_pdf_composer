import sys
from builtins import print, exit, KeyError, sorted
import argparse
import importlib_metadata


def index(*args, **kwargs):
    _eps = []
    _eps.extend(kwargs.get('endpoints', []))
    return _eps


class Api:
    def __init__(self):
        self._outputers = {
            _ep.name: _ep for _ep in importlib_metadata.entry_points().select(group='pdfcomposer.output')
        }

    def __call__(self, *args, **kwargs):
        _outputer = kwargs.get('path', 'index')
        _kws = []
        _kws.extend([_item for _item in kwargs.items() if _item[0] != 'outputer'])
        try:
            _fnc = self._outputers[_outputer].load()
        except KeyError:
            print(f'outputer {_outputer} is not available!', file=sys.stderr)
            print(f'available outputers: ({", ".join(sorted(self._outputers))})')
            return 1
        else:
            if _outputer == 'index':
                _kws.append(('endpoints', sorted([_item[0] for _item in self._outputers.items()])))
            return _fnc(*args, **dict(_kws))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--outputer', default='default')
    parser.add_argument('--args', nargs='*')
    parser.add_argument('--kwargs', nargs='*', help='Example: title="My PDF" author="John Doe" subject="My first PDF" creator="John Doe"')
    parser_args = parser.parse_args()

    _args = []
    _kws = {'path': parser_args.outputer}
    if parser_args.args:
        _args.extend(parser_args.args)

    if parser_args.kwargs:
        for _kv_str in parser_args.kwargs.split(' '):
            _k, _v = _kv_str.split('=')
            _kws[_k] = _v

    outputer = Api()
    outputer(*_args, **_kws)
    return 0


if __name__ == '__main__':
    exit(main())
