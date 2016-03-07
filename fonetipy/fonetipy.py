# -*- coding: utf-8 -*-
"""This module implement a phonectic buscabr alghoritm for Python."""

import re
from collections import namedtuple
from unidecode import unidecode


class FonetiPy(object):
    """BuscaBr phonectic alghoritm class."""

    __slots__ = ("__codes",)

    def __init__(self):
        """Start process with default codes from buscaBr alghoritm."""
        # Replace to
        ReplTo = namedtuple("ReplTo", ["repl", "to"])
        self.__codes = (
            ReplTo(r"BL|BR", "B"),
            ReplTo(r"PH", "F"),
            ReplTo(r"GL|GR|MG|NG|RG", "G"),
            ReplTo(r"Y", "I"),
            ReplTo(r"GE|GI|RJ|MJ", "J"),
            ReplTo(r"CA|CO|CU|CK|Q", "K"),
            ReplTo(r"N", "M"),
            ReplTo(r"AO|AUM|GM|MD|OM|ON", "M"),
            ReplTo(r"PR", "P"),
            ReplTo(r"L", "R"),
            ReplTo(r"CE|CI|CH|CS|RS|TS|X|Z", "S"),
            ReplTo(r"TR|TL", "T"),
            ReplTo(r"CT|RT|ST|PT", "T"),
            ReplTo(r"\b[UW]", "V"),
            ReplTo(r"RM", "SM"),
            ReplTo(r"[MRS]+\b", ""),
            ReplTo(r"[AEIOUH]", "")
        )

    def __call__(self, string):
        """Wrap to a default behavior > self.apply."""
        return self.apply(string)

    def apply(self, string):
        """Apply BuscaBr alghoritm on string."""
        string = string.upper()

        # Cedilla correction:
        for asc in ("ç", "Ç"):
            if asc in string:
                regex = re.compile(asc)
                string = re.sub(regex, "S", string)

        string = unidecode(unicode(string)).upper()
        for i in self.__codes:
            string = re.sub(re.compile(i.repl), i.to, string)

        return self.squeeze(string)

    def squeeze(self, string):
        """Squeeze string."""
        # last index
        l_idx = len(string) - 1
        enum = enumerate(string)
        string = "".join(i for n, i in enum
                         if string[n + 1 if n < l_idx else n - 1]
                         is not i)

        return string

# Shortcut if you don't need a class(e.g: inheritance)
fonetipy = FonetiPy()
