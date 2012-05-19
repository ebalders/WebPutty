# coding=utf-8
 
import os

debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')
debug_profiler_enabled = False
appname = 'WebPutty OSS'
appversion_raw = [1, 3, 0]
appversion = '.'.join([str(num) for num in appversion_raw])
invite_sender_email = '%s Invitation <erikb@datarg.com>' % appname
incoming_sender_email = '%s Incoming Mail <erikb@datarg.com>' % appname
log_all_incoming = True
# List of admins to forward mail to.
forward_mail_to = ['erikb@datarg.com']
jquery_url = '//ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js'
# Generate this once by calling os.urandom(24)
secret_key = "p\xb8\xbcd\x0b\xc5\xab\xfd$\xe7\xc8uY\x923\x1c\xe2\xcd\xf5\xf4\xa8d\xad{"

# Name of the Google Cloud Storage bucket
use_google_cloud_storage = True
google_bucket = 'webputtyerikb'

available_locales = [
    ('en', u'English'),
    ('fr', u'Français'),
]

# API Keys for url2png.com
url2png = dict(
    user = 'ebalders',
    password = 'Stopgate1717',
    bounds = '300x300',
)
