# -*- coding: utf-8 -*-
#!/usr/bin/env python

import urllib
import hmac
import hashlib
import base64
import logging
logger = logging.getLogger('LifeApi')

from config import settings

delimiter = '?'
sign_attr = '&signature='

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
    string = ''.join((method, delimiter, query, sign_attr))
    digest = hmac.new(self.settings['application_key'], string, hashlib.sha1).digest()
    sign = base64.b64encode(digest) 
    return ''.join((self.settings['api_url'], string, sign))
