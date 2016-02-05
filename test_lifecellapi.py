# -*- coding: utf-8 -*-
#!/usr/bin/env python

import unittest
from lifecellapi import (LifecellSession, LifecellApi,
                         LifecellApiWrongMethodError, LifecellApiError
                        )


class LifecellApiTest(unittest.TestCase):

  def setUp(self):
    self.s = LifecellSession('380931234567', '123456')
    self.api = LifecellApi(self.s)
    self.req = {
      'accessKeyCode': self.s.settings['access_key_code'],
      'msisdn': self.s.num,
      'superPassword': self.s.pwd
      }

  def testApiWrongRequest(self):
    try:
      self.api.wrongApi()
    except LifecellApiWrongMethodError as e:
      pass
    except e:
      self.fail('Unexpected exception throw:', e)
    else:
      self.fail('LifecellApiWrongMethodError not throw')

  def testApiErrorRequest(self):
    try:
      self.api.getToken()
    except LifecellApiError as e:
      pass
    except e:
      self.fail('Unexpected exception throw:', e)
    else:
      self.fail('LifecellApiError not throw')

