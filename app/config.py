import os
backend_url = os.environ.get('backend_url')
if backend_url is None:
    backend_url = 'https://kinhkcovid19dataengine.herokuapp.com/'