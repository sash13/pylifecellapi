# -*- coding: utf-8 -*-
#!/usr/bin/env python

from config import settings

import urllib
import requests
import random
import xmltodict
import hmac
import hashlib
import base64
import logging
logger = logging.getLogger('LifeApi')

DELIMITER = '?'
SIGNATURE = '&signature='
USER_AGENTS = (
  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)',
  'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true',
  'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10',
  'BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba',
)
API_CALL = 'apiCall'
OS_TYPE = 'ANDROID'


class LifecellApi(object):
  __slots__ = ('_session', 'n', '_args')

  def __init__(self, session, **args):
    self._session = session
    self._args = args

  def __getattr__(self, n):
    return Request(self, n)

  def __call__(self, obj):
    return getattr(self._session, API_CALL)(obj)


class Request(object):
  __slots__ = ('_api', '_name', '_args')

  def __init__(self, api, name):
    self._api = api
    self._name = name

  def __call__(self, **args):
    self._args = args
    return self._api(self)


class LifecellSession(object):
  """Class for acess lifecell api"""

  def __init__(self, msisdn, password, lang='uk'):
    self.num = msisdn
    self.pwd = password
    self.lang = lang
    self.settings = settings
    self.osType = OS_TYPE
    self.token = ''
    self.subId = ''
    self.user_agent = random.choice(USER_AGENTS)
    logger.debug('Init %s done.', __name__)

  def getParameters(self, params={}):
    default = {'msisdn': self.num,
           'languageId': self.lang,
           'osType': self.osType,
           'token': self.token,
           'accessKeyCode': self.settings['access_key_code']
           }
    return dict(default.items() + params.items())

  def createSignedUrl(self, method, params={}):
    query = urllib.urlencode(params)
    string = ''.join((method, DELIMITER, query, SIGNATURE))
    digest = hmac.new(
      self.settings['application_key'],
      string,
      hashlib.sha1).digest()
    sign = base64.b64encode(digest)
    return ''.join((self.settings['api_url'], string, sign))

  def request(self, method, params={}):
    logger.debug('{0} request: {1}'.format(method, params))
    url = self.createSignedUrl(method, params)
    logger.debug('Sign url: %s', url)

    try:
      return requests.get(
        url, headers={
          'User-Agent': self.user_agent}).text
    except requests.exceptions.Timeout as e:
      logger.exception('Request timeout.')
      raise e
    except requests.exceptions.RequestException as e:
      logger.exception('Request error.')
      raise e

  def apiCall(self, methods):
    params = self.getParameters(methods._args)
    req = self.request(methods._name, params)
    return xmltodict.parse(req)

  def signIn(self):
    params = {'msisdn': self.num,
          'superPassword': self.pwd,
          'accessKeyCode': self.settings['access_key_code']
          }
    req = self.request('signIn', params)
    parse = xmltodict.parse(req)
    self.token = parse['response']['token']
    self.subId = parse['response']['subId']
