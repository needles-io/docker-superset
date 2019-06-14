import os

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 300
}

# redshift+psycopg2://username@host.amazonaws.com:5439/database
# SQLALCHEMY_DATABASE_URI = f'redshift+psycopg2://needles:WGQMBBaj3oV1Q06j@fb-cluster1.cqyixkdcerwo.ap-southeast-2.redshift.amazonaws.com:5439/fb'
SQLALCHEMY_DATABASE_URI = 'sqlite:////var/lib/superset/superset.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'NEEDLESthisISaSECRET_1234NEEDLES'
