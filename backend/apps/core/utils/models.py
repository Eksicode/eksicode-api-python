import re


class Choices:
    def __init__(self, *choices):
        self.__choices = {}
        for choice in choices:
            choice = choice.strip()
            attr = self._attributize(choice)
            setattr(self, attr, choice)
            self.__choices[attr] = choice

    @property
    def choices(self):
        return tuple(self.__choices.items())

    @property
    def values(self):
        return tuple(self.__choices.values())

    def get(self, item, fallback=None):
        return self.__choices.get(item, fallback)

    @staticmethod
    def _attributize(string):
        """Turns any string into a valid python variable"""
        return re.sub(r'\W|^(?=\d)', '_', string.strip()).upper()

    def __contains__(self, item):
        return item in self.__choices.values() or item in self.__choices.keys()

    def __getitem__(self, item):
        return self.__choices[item]
