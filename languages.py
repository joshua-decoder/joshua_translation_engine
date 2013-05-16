import sys

LANGUAGE_ALIASES = [
    (u'en', u'english'),
    (u'es', u'spanish'),
    (u'de', u'german'),
]

LANGUAGE_NAMES_FROM_SHORT = {
    short: (short, long_) for short, long_ in LANGUAGE_ALIASES
}

LANGUAGE_NAMES_FROM_LONG_ENGLISH = {
    long_: (short, long_) for short, long_ in LANGUAGE_ALIASES
}


class LanguageAliases(object):
    """
    This class provides access to all of the aliases for a single language.
    """

    def __init__(self, short_name, long_english_name):
        self._short = short_name
        self._long_english = long_english_name

    @property
    def short_name(self):
        return self._short

    @property
    def long_english_name(self):
        return self._long_english

def new_lang_from_short_name(short_name):
    try:
        aliases = LANGUAGE_NAMES_FROM_SHORT[short_name.lower()]
    except KeyError:
        sys.stderr.write(
            "The language code '%s' is not supported." % short_name
        )
        raise KeyError

    return LanguageAliases(*aliases)

def new_lang_from_long_english_name(long_name):
    try:
        aliases = LANGUAGE_NAMES_FROM_LONG_ENGLISH[long_name.lower()]
    except KeyError:
        sys.stderr.write("The language '%s' is not supported." % long_name)
        raise KeyError

    return LanguageAliases(*aliases)
