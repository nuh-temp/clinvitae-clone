import json
import os
import webapp2

from lib import storage

from google.appengine.ext.webapp import template


class Index(webapp2.RequestHandler):
    """Class to handle index page."""

    _INDEX_TMPL = 'index.html'

    def get(self):
        path = os.path.join(os.path.dirname(__file__), self._INDEX_TMPL)
        self.response.out.write(template.render(path, {}))


class Suggest(webapp2.RequestHandler):
    """Handles requests for auto completion."""

    def get(self):
        """Returns a JSON of list of available genes for given prefix."""
        genes = self.request.get('genes')
        self.response.content_type = 'application/json'
        if not genes:
            self.response.write('[]')
            return

        result = storage.Cache.Suggest(genes) or []
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
        data = storage.Cache.Variants(q.strip().split(',')) or {}
        result = {
            'header': storage.Cache.Header(),
            'variants': data,
        }
        self.response.write(json.dumps(result))

storage.Cache.Init()

app = webapp2.WSGIApplication([
    ('/api/v1/suggest', Suggest),
    ('/api/v1/variants', Variants),
    ('/.*', Index),
], debug=True)
