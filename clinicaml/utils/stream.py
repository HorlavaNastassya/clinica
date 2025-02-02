# coding: utf8

"""This module handles stream and log redirection."""

import sys

clinica_verbose = False


class FilterOut(object):
    def __init__(self, stdout):
        self.stdout = stdout

    def write(self, text):
        import re

        if not text:
            return
        if re.match("^(@clinicaml@)", text):
            self.stdout.write(text.replace("@clinicaml@", ""))
            self.stdout.flush()

    def flush(self):
        self.stdout.flush()

    def __enter__(self):
        self.origin_stdout = sys.stdout
        self.flush()

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.origin_stdout
        self.flush()


def active_cprint():
    sys.stdout = FilterOut(sys.stdout)


def cprint(msg):
    global clinica_verbose
    if clinica_verbose is True:
        print(msg)
    else:
        print("@clinicaml@%s\n" % msg)
    sys.stdout.flush()
