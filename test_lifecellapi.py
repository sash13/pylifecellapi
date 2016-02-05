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

  def testSignedUrl(self):
    answer = self.s.createSignedUrl('signIn', self.req)
    desired = 'https://api.life.com.ua/mobile/signIn?msisdn=380931234567&superPassword=123456&accessKeyCode=7&signature=JpDJ2UD8OHsZL19S9UOEePIRaN8='
    self.assertEqual(answer, desired,
             'incorrect sign string')

  def testRequest(self):
    answer = self.s.request('signIn', self.req)
    desired = '''<?xml version="1.0" encoding="UTF-8"?>\n<response method="signIn"><responseCode>-10</responseCode></response>'''
    self.assertEqual(answer, desired,
             'incorrect answer')

  def testApiWrongRequest(self):
    try:
      self.api.wrongApi()
    except LifecellApiWrongMethodError, e:
      pass
    except e:
      self.fail('Unexpected exception throw:', e)
    else:
      self.fail('LifecellApiWrongMethodError not throw')
      
  def testApiErrorRequest(self):
    try:
      self.api.getToken()
    except LifecellApiError, e:
      pass
    except e:
      self.fail('Unexpected exception throw:', e)
    else:
      self.fail('LifecellApiError not throw')

