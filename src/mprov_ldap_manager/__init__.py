import sys


sys.path.append('/var/www/mprov_control_center')
from django.conf import settings
# add in the icons to JAZZMIN
settings.JAZZMIN_SETTINGS['icons']['mprov_ldap_manager'] = "far fa-address-book"
settings.JAZZMIN_SETTINGS['icons']['mprov_ldap_manager.ldapuser'] = "fas fa-user-tag"
settings.JAZZMIN_SETTINGS['icons']['mprov_ldap_manager.ldapgroup'] = "fas fa-users"

import ldap
import os

ldapdb = {
  'ldap': {
      'ENGINE': 'ldapdb.backends.ldap',
      'NAME': os.environ.get('LDAPMGR_URL', 'ldaps://localhost/') ,
      'USER': os.environ.get('LDAPMGR_USER','cn=root,dc=cluster,dc=local'),
      'PASSWORD': os.environ.get('LDAPMGR_PASS', 'password'),
      'BASEDN': os.environ.get('LDAPMGR_DN', 'dc=cluster,dc=local'),      
    },
}

for i in settings.DATABASES.keys():
   ldapdb[i] = settings.DATABASES[i]


if os.environ.get('LDAPMGR_TLS_SELFSIGNED', '0') == '1':
    ldapdb['ldap']['CONNECTION_OPTIONS'] = {
          ldap.OPT_X_TLS_REQUIRE_CERT: ldap.OPT_X_TLS_NEVER
      }
# add in our config    
settings.DATABASES = ldapdb
if hasattr(settings, 'DATABASE_ROUTERS'):
  settings.DATABASE_ROUTERS.append('ldapdb.router.Router')
else:
  setattr(settings, 'DATABASE_ROUTERS', ['ldapdb.router.Router'])