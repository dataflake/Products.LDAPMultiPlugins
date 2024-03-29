Active Directory support
========================

ActiveDirectory Multi Plugin
----------------------------
Aditional properties of the ADMultiPlugin instance:

- groupid_attr - the LDAP attribute used for group ids.

- grouptitle_attr - the LDAP attribute used to compose group titles.

- group_class - the LDAP class of group objects.

- group_recurse - boolean indicating whether to determine group
  memberships of a user by unrolling nested group relationships
  (expensive). This feature is not guaranteed to work at this moment.


Active Directory configuration hints
------------------------------------
In order for groups support to work correctly, you may have to set the
following properties. Every situation is different, but this has helped
some people succeed:

- On the "Properties" tab for the ActiveDirectoryMultiPlugin, set the
  groupid_attr property to "name".

- On the contained LDAPUserFolder's "Configure" tab, choose a
  property other than "objectGUID", e.g. "sAMAccountName" for the
  User ID property. To get to the LDAPUserFolder, click on the
  ActiveDirectoryMultiPlugin "Content" tab.

Please see the `LDAPUserFolder FAQ 
<https://productsldapuserfolder.readthedocs.io/en/latest/faq.html#microsoft-active-directory>`_ for additional information.
