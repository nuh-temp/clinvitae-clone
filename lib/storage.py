import csv
import logging

from lib import trie


class Cache(object):
    """Singleton to cache data from file."""

    _initialized = False
    _genes_dict = None
    _storage = None
    _header = None

    _DATA_FILENAME = 'variant_results.tsv'

    @classmethod
    def Init(cls):
        """Initializes cache by reading and parsing data file."""
        if cls._initialized:
            return

        cls._storage = {}
        cls._genes_dict = trie.PrefixTree()
        with open(cls._DATA_FILENAME, 'r') as csvfile:
            cvs_reader = csv.reader(csvfile, delimiter='\t')
            cls._header = cvs_reader.next()
            for row in cvs_reader:
                key = row[0].upper()
                if key not in cls._storage:
                    cls._storage[key] = []

                cls._storage[key].append(row)

        for gene in cls._storage.iterkeys():
            cls._genes_dict.Insert(gene)

        logging.info('cache has been initialized.')
        cls._initialized = True

    @classmethod
    def Suggest(cls, prefix):
        """Looks up suggestions by given prefix."""
        cls.Init()

        result = cls._genes_dict.SearchByPrefix(prefix.upper())
        return [g for g in sorted(result)]

    @classmethod
    def Header(cls):
        """Returns data header as a list."""
        cls.Init()

        return cls._header

    @classmethod
    def Variants(cls, genes):
        """Returns variants for given genes."""
        cls.Init()

        result = []
        for gene in genes:
            v = cls._storage.get(gene)
            if v:
                result.extend(v)

        return result
