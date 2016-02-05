settings = {
  'access_key_code': '7',
  'application_key': 'E6j_$4UnR_)0b',
  'api_url': 'https://api.life.com.ua/mobile/'
}

API_METHODS = {
  'callMeBack':                 ('msisdnB'),
  'changeLanguage':             ('newLanguageId'),
  'changeSuperPassword':        ('oldPassword', 'newPassword'),
  'getAvailableTariffs':        (),
  'getBalances':                (),
  'getExpensesSummary':         ('monthPeriod'),
  'getLanguages':               (),
  'getPaymentsHistory':         ('monthPeriod'),
  'getServices':                (),
  'getSummaryData':             (),
  'getToken':                   ('msisdn', 'subId'),
  'getUIProperties':            (),
  'refillBalanceByScratchCard': ('secretCode'),
  'requestBalanceTransfer':     ('msisdnB'),
  'signIn':                     ('msisdn', 'superPassword'),
  'signOut':                    ('msisdn', 'subId')
}

RESPONSE_CODES = {
  '0': 'SUCCESSFULY_PERFORMED',
  '-1': 'METHOD_INVOCATION_TIMEOUT',
  '-2': 'INTERNAL_ERROR',
  '-3': 'INVALID_PARAMETERS_LIST',
  '-4': 'VENDOR_AUTHORIZATION_FAILED',
  '-5': 'VENDOR_ACCESS_KEY_EXPIRED',
  '-6': 'VENDOR_AUTHENTICATION_FAILED',
  '-7': 'SUPERPASS_CHECKING_FAILED',
  '-8': 'INCORRECT_SUBSCRIBER_ID',
  '-9': 'INCORRECT_SUBSRIBER_STATE',
  '-10': 'SUPERPASS_BLOCKED',
  '-11': 'SUBSCRIBER_ID_NOT_FOUND',
  '-12': 'TOKEN_EXPIRED',
  '-13': 'CHANGE_TARIFF_FAILED',
  '-14': 'SERVICE_ACTIVATION_FAILED',
  '-15': 'OFFER_ACTIVATION_FAILED',
  '-16': 'GET_TARIFFS_FAILED',
  '-17': 'GET_SERVICES_FAILED',
  '-18': 'REMOVE_SERVICE_FROM_PREPROCESSING_FAILED',
  '-19': 'LOGIC_IS_BLOCKING',
  '-20': 'TOO_MANY_REQUESTS',
  '-40': 'PAYMENTS_OR_EXPENSES_MISSED',
  '-21474833648': 'INTERNAL_APPLICATION_ERROR',
}