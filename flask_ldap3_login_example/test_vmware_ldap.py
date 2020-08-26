from flask_ldap3_login import LDAP3LoginManager, AuthenticationResponseStatus
import getpass

config = dict()

# Setup LDAP Configuration Variables. Change these to your own settings.
# All configuration directives can be found in the documentation.

# Hostname of your LDAP Server
config['LDAP_HOST'] = 'ldap://ldap.vmware.com'

# Base DN of your directory
config['LDAP_BASE_DN'] = 'CN=Users,DC=vmware,DC=com'

config['LDAP_BIND_DIRECT_CREDENTIALS'] = True
# config['LDAP_BIND_DIRECT_SUFFIX'] = '@vmware.com'
config['DEBUG'] = True

# config['LDAP_BIND_USER_DN'] = 'CN=rshende,CN=Users,DC=vmware,DC=com'
# config['LDAP_BIND_USER_PASSWORD'] = getpass.getpass("Password for bind :")

username = input("Email :")
password = getpass.getpass(prompt="Enter Password:")

# # Users DN to be prepended to the Base DN
# config['LDAP_USER_DN'] = 'ou=users'
#
# # Groups DN to be prepended to the Base DN
# config['LDAP_GROUP_DN'] = 'ou=groups'
#
#
# # The RDN attribute for your user schema on LDAP
# config['LDAP_USER_RDN_ATTR'] = 'cn'
#
# # The Attribute you want users to authenticate to LDAP with.
# config['LDAP_USER_LOGIN_ATTR'] = 'mail'

# Setup a LDAP3 Login Manager.
ldap_manager = LDAP3LoginManager()

# print('LDAP Manager - ', ldap_manager)
# Init the mamager with the config since we aren't using an app
ldap_manager.init_config(config)
# print('LDAP Manager Config Initialized ')


# Check if the credentials are correct
response = ldap_manager.authenticate(username, password)

if response.status == AuthenticationResponseStatus.success:
    print("Correct Credentials")
elif response.status == AuthenticationResponseStatus.fail:
    print("Incorrect Credentials...")
else:
    print(response.status)
    print("Something went wrong")

# print(response.user_id)
# print(response.user_dn)
# print(response.user_groups)
# print(response.user_info)

# print(ldap_manager.get_group_info(config['LDAP_BASE_DN']))
# print(ldap_manager.get_user_info(config['LDAP_BASE_DN']))
