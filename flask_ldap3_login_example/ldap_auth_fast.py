from flask_ldap3_login import LDAP3LoginManager, AuthenticationResponseStatus
import getpass
import time
import logging

logger = logging.getLogger('flask_ldap3_login')
logger.setLevel(logging.DEBUG)


def authenticate_ldap(email, password):
    # Check if the credentials are correct
    response = ldap_manager.authenticate_search_bind(email, password)

    if response.status == AuthenticationResponseStatus.success:
        return True
    else:
        return False


config = dict()

# Setup LDAP Configuration Variables. Change these to your own settings.
# All configuration directives can be found in the documentation.

# Hostname of your LDAP Server
config['LDAP_HOST'] = 'ldap://ldap.eng.vmware.com'
# config['LDAP_PORT'] = 636

# Base DN of your directory
config['LDAP_BASE_DN'] = 'DC=vmware,DC=com' #'CN=Users,DC=vmware,DC=com'

config['LDAP_BIND_DIRECT_CREDENTIALS'] = True
# config['LDAP_BIND_DIRECT_SUFFIX'] = '@vmware.com'
config['DEBUG'] = True

# Users DN to be prepended to the Base DN
config["LDAP_USER_DN"] = "ou=users"

# Groups DN to be prepended to the Base DN
config["LDAP_GROUP_DN"] = "ou=groups"

# The RDN attribute for your user schema on LDAP
config["LDAP_USER_RDN_ATTR"] = "cn"

# The Attribute you want users to authenticate to LDAP with.
config["LDAP_USER_LOGIN_ATTR"] = "mail"

# The Username to bind to LDAP with
config["LDAP_BIND_USER_DN"] = 'None'

# The Password to bind to LDAP with
config["LDAP_BIND_USER_PASSWORD"] = None

# Setup a LDAP3 Login Manager.
ldap_manager = LDAP3LoginManager()

# Init the mamager with the config since we aren't using an app
ldap_manager.init_config(config)


if __name__ == '__main__':
    email_id = 'rshende@vmware.com' #input("Email :")
    passwd = getpass.getpass(prompt="Enter Password:")
    start = time.time()
    print(authenticate_ldap(email_id, passwd))
    print('Time Taken:', time.time() - start)