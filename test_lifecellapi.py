# -*- coding: utf-8 -*-
#!/usr/bin/env python

import unittest
from  lifecellapi import LifecellSession

class LifecellApiTest(unittest.TestCase):
  def setUp(self):
    self.api = LifecellSession('380931234567', '123456')

  def testSignedUrl(self):
    req = { 'accessKeyCode': self.api.settings['access_key_code'], 'msisdn': self.api.num, 'superPassword': self.api.pwd}
    answer = self.api.createSignedUrl('signIn', req)
    desired = 'https://api.life.com.ua/mobile/signIn?msisdn=380931234567&superPassword=123456&accessKeyCode=7&signature=JpDJ2UD8OHsZL19S9UOEePIRaN8='
    self.assertEqual(answer, desired,
                    'incorrect sign string')

  def testRequest(self):
    answer = self.api.request('signIn')
    desired = '''<?xml version="1.0" encoding="UTF-8"?>\n<response method="signIn"><responseCode>-10</responseCode></response>'''
    self.assertEqual(answer, desired,
                    'incorrect answer')
