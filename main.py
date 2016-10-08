import csv
import json
import logging
import os
import webapp2

from lib import trie

from google.appengine.ext.webapp import template


class Cache(object):

    storage = None
    header = None

    @classmethod
    def Init(cls):
        if cls.storage is not None:
            return

        cls.storage = {}
        with open('variant_results.tsv', 'r') as csvfile:
            cvs_reader = csv.reader(csvfile, delimiter='\t')
            cls.header = cvs_reader.next()
            for row in cvs_reader:
                key = row[0].upper()
                if key not in cls.storage:
                    cls.storage[key] = []

                cls.storage[key].append(row)

    @classmethod
    def Suggest(cls, key):
        if cls.storage is None:
            cls.Init()

        result = set()
        key = key.upper()
        for gene in cls.storage.iterkeys():
            if gene.startswith(key):
                result.add(gene)

        return [g for g in sorted(result)]

    @classmethod
    def Header(cls):
        if cls.header is None:
            cls.Init()
        return cls.header

    @classmethod
    def Variants(cls, genes):
        if cls.storage is None:
            cls.Init()

        result = []
        for gene in genes:
            v = cls.storage.get(gene)
            if v:
                result.extend(v)

        return result


class Index(webapp2.RequestHandler):
    """Class to handle index page."""

    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))


class Suggest(webapp2.RequestHandler):
    """Handles requests for auto completion."""

    def get(self):
        """Returns a JSON of list of available genes for given prefix."""
        genes = self.request.get('genes')
        logging.info('Suggest: genes=%s', genes)
        self.response.content_type = 'application/json'
        if not genes:
            self.response.write('[]')
            return

        result = Cache.Suggest(genes) or []
        self.response.write(json.dumps(result))


class Variants(webapp2.RequestHandler):
    """Handles requests for gene's variants."""

    def get(self):
        """Returns a JSON of dict with variants' headers and data."""
        q = self.request.get('q')
        self.response.content_type = 'application/json'
        if not q:
            self.response.write('{}')
            return
        data = Cache.Variants(q.strip().split(',')) or {}
        result = {
            'header': Cache.Header(),
            'variants': data,
        }
        self.response.write(json.dumps(result))


app = webapp2.WSGIApplication([
    ('/api/v1/suggest', Suggest),
    ('/api/v1/variants', Variants),
    ('/.*', Index),
], debug=True)
