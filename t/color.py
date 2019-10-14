#! /usr/bin/env python3

from typing import Optional, List, Union


_STYLES = {"bold":          1,
           "faint":         2,
           "italic":        3,
           "underline":     4,
           "reverse":       7,
           "strikethrough": 9}


_COLORS = {"black":         0,
           "red":           1,
           "green":         2,
           "yellow":        3,
           "blue":          4,
           "magenta":       5,
           "cyan":          6,
           "white":         7}


def vanilla(text):
    return str(text)


def bold(text):
    return decorate(text, style="bold")


def faint(text):
    return decorate(text, style="faint")


def italic(text):
    return decorate(text, style="italic")


def underline(text):
    return decorate(text, style="underline")


def reverse(text):
    return decorate(text, style="reverse")


def strikethrough(text):
    return decorate(text, fcolor="strikethrough")


def red(text):
    return decorate(text, fcolor="red")


def green(text):
    return decorate(text, fcolor="green")


def yellow(text):
    return decorate(text, fcolor="yellow")


def blue(text):
    return decorate(text, fcolor="blue")


def magenta(text):
    return decorate(text, fcolor="magenta")


def cyan(text):
    return decorate(text, fcolor="cyan")


def white(text):
    return decorate(text, fcolor="white")


def on_black(text):
    return decorate(text, bcolor="black")


def on_red(text):
    return decorate(text, bcolor="red")


def on_green(text):
    return decorate(text, bcolor="green")


def on_yellow(text):
    return decorate(text, bcolor="yellow")


def on_blue(text):
    return decorate(text, bcolor="blue")


def on_magenta(text):
    return decorate(text, bcolor="magenta")


def on_cyan(text):
    return decorate(text, bcolor="cyan")


def on_white(text):
    return decorate(text, bcolor="white")


def decorate(text,
             style:  Optional[Union[str, List[str]]] = None,
             fcolor: Optional[str]                   = None,
             bcolor: Optional[str]                   = None):
    attr = _concat(style, fcolor, bcolor)
    return "\033[{}m{}\033[0m".format(attr, text) if attr else text


def _concat(style, fcolor, bcolor):
    """
    Example
    -------
    >>> _concat(["bold", "underline"], "white", "red")
    '1;4;37;41'
    """
    if style is None:
        attr = []
    elif isinstance(style, str):
        attr = [_STYLES[style]]
    else:
        attr = [_STYLES[x] for x in style]
    if isinstance(fcolor, str):
        attr.append(30 + _COLORS[fcolor])
    if isinstance(bcolor, str):
        attr.append(40 + _COLORS[bcolor])
    return ";".join([str(x) for x in attr])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
