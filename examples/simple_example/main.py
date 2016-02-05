from  lifecellapi import LifecellApi, LifecellSession
import json

""" Change this """
msisdn = '380931234567'
pwd = '123456'

def main():
  import logging.config
  logging.config.fileConfig('logging.conf')
  logger = logging.getLogger('main')
  s = LifecellSession(msisdn, pwd)
  ansv = s.signIn()
  api = LifecellApi(s)
  logger.debug(ansv)

  ansv = api.getBalances()

  print json.dumps(ansv, indent=4)

if __name__ == '__main__':
  main()