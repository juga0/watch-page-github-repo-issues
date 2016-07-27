"""watch_url functions."""

import logging

logging.basicConfig(level=logging.DEBUG)
try:
    from config import LOGGING
    logging.config.dictConfig(LOGGING)
except:
    print 'No LOGGING configuration found.'
logger = logging.getLogger(__name__)


def generate_urls_data(agent_type, url, etag, last_modified,
                       content='', keyword=''):
    """
    https://store.openintegrity.org/...
    data = {
       "key": "https://api.github.com./..",
       "agent_ip": 1.2.3.4
       "agent_type": "watch-url",
       "timestamp_measurements": "20160623T120243Z",
       "header": {
           "etag": ""
           "last_modified": "Mon, 13 Jun 2016 19:01:36 GMT"
       },
       "content": "",
       'keyword': keyword
    }
    """
    data = {
        'key': url,
        'agent_ip':  obtain_public_ip(),
        'agent_type': agent_type,
        'timestamp_measurements': now_timestamp_str_nodashes(),
        'header': {
            'etag': etag,
            'last_modified': last_modified
            },
        'content': content,
        'keyword': keyword
        }
    return data
