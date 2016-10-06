import csv
import webapp2
import os
from google.appengine.ext.webapp import template
import json
import logging


class Cache(object):

	storage = None

	@classmethod
	def Init(cls):
		if cls.storage is not None:
			return

		cls.storage = {}
		with open('variant_results.tsv', 'r') as csvfile:
			csvfile.readline()
			spamreader = csv.reader(csvfile, delimiter='\t')
			for row in spamreader:
				key = row[0].upper()
				if key not in cls.storage:
					cls.storage[key] = []

				cls.storage[key].append(row[1:])


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
	def Variants(cls, gene):
		if cls.storage is None:
			cls.Init()		

		return cls.storage.get(gene)


class Index(webapp2.RequestHandler):

    def get(self):
		template_values = {
			'message': 'Hello World!'
		}
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.out.write(template.render(path, template_values))


class Suggest(webapp2.RequestHandler):

	def get(self):
		genes = self.request.get('genes')
		self.response.content_type = 'application/json'
		if not genes:
			self.response.write('[]')
			return

		result = Cache.Suggest(genes)
		self.response.write(json.dumps(result))


class Variants(webapp2.RequestHandler):
	def get(self):
		# q=BRAF&f=&source=ARUP,Carver,ClinVar,EmvClass,Invitae,kConFab&classification=1,2,3,4,5,6&BRAF
		q = self.request.get('q')
		self.response.content_type = 'application/json'
		variants = Cache.Variants(q) or []
		self.response.write(json.dumps(result))


app = webapp2.WSGIApplication([
    ('/api/v1/suggest', Suggest),
    ('/api/v1/variants', Variants),
    ('/', Index),
], debug=True)

