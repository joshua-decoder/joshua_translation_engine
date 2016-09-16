import sys

LANGUAGE_ALIASES = [
    (u'ar', u'arabic'),
    (u'cz', u'czech'),
    (u'da', u'danish'),
    (u'nl', u'dutch'),
    (u'en', u'english'),
    (u'et', u'estonian'),
    (u'fi', u'finnish'),
    (u'fr', u'french'),
    (u'de', u'german'),
    (u'el', u'greek'),
    (u'it', u'italian'),
    (u'no', u'norwegian'),
    (u'pl', u'polish'),
    (u'pt', u'portuguese'),
    (u'sl', u'slovene'),
    (u'es', u'spanish'),
    (u'sv', u'swedish'),
    (u'tr', u'turkish'),
]

LANGUAGE_NAMES_FROM_SHORT = dict(
    (short, (short, long_)) for (short, long_) in LANGUAGE_ALIASES
)

LANGUAGE_NAMES_FROM_LONG_ENGLISH = dict(
    (long_, (short, long_)) for (short, long_) in LANGUAGE_ALIASES
)

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
