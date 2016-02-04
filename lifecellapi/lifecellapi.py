# -*- coding: utf-8 -*-
#!/usr/bin/env python

import urllib
import requests
import random
import hmac
import hashlib
import base64
import logging
logger = logging.getLogger('LifeApi')

from config import settings

DELIMITER = '?'
SIGNATURE = '&signature='
USER_AGENTS = ('Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)',
               'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true',
               'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10',
               'BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba',
              )

class LifecellApi():
  """Class for acess lifecell api"""
  def __init__(self, msisdn, password, lang = 'uk'):
    self.num = msisdn
    self.pwd = password
    self.lang = lang
    self.settings = settings
    logger.debug('Init %s done.', __name__)

  def createSignedUrl(self, method, params):
    query = urllib.urlencode(params)
    string = ''.join((method, DELIMITER, query, SIGNATURE))
    digest = hmac.new(self.settings['application_key'], string, hashlib.sha1).digest()
    sign = base64.b64encode(digest) 
    return ''.join((self.settings['api_url'], string, sign))

  def request(self, method, params):
    logger.debug('{0} request: {1}'.format(method, params))
    url = self.createSignedUrl(method, params)
    try:
      return requests.get(url, headers={'User-Agent': random.choice(USER_AGENTS)}).text
    except requests.exceptions.Timeout as e:
      logger.debug('Request timeout.')
      raise e
    except requests.exceptions.RequestException as e:
      logger.debug('Request error.')
      raise e