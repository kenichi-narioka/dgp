# Copyright 2020 Toyota Research Institute.  All rights reserved.
"""Various utility functions for Click options"""
import functools


def add_options(**kwargs):
    """Decorator function to add a list of Click options to a Click subcommand.
    """
    def _add_options(func):
        return functools.reduce(lambda x, opt: opt(x), kwargs["options"], func)

    return _add_options
