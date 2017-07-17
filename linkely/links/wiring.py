from django.conf import settings
from elasticsearch import Elasticsearch

def es_client():
    conf = settings.ELASTICSEARCH['default']
    url = 'http://{user}:{password}@{host}:{port}'.format(
        user = conf['USER'],
        password = conf['PASSWORD'],
        host = conf['HOST'],
        port = conf['PORT']
    )
    return Elasticsearch([url])
