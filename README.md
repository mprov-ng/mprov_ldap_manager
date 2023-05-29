# mprov_ldap_manager
This is an mPCC python module add-on that will allow the mPCC to manage an LDAP directory.


# Installation
Follow these easy steps to enable this module in the mPCC

1. Go into `/var/www/mprov_control_center` and run `source bin/activate` from a bash prompt.
2. `pip install mprov_ldap_manager` This will install the python module into your mPCC environment
3. Edit the `/var/www/mprov_control_center/mprov_control_center/settings.py` file and add `mprov_ldap_manager` to the bottom of the `INSTALLED_APPS` array.
4. In your `/var/www/mprov_control_center/.env` file, add the following:
```
LDAPMGR_URL=ldaps://ldapserver/
LDAPMGR_USER="cn=root,dc=cluster,dc=local"
LDAPMGR_PASS='password'
LDAPMGR_DN='dc=cluster,dc=local'
# if your LDAP uses a self signed cert, add this line.
LDAPMGR_TLS_SELFSIGNED=1
```


5. Run `touch /var/www/mprov_control_center/mprov_control_center/wsgi.py` to refresh the mPCC or restart your webserver.