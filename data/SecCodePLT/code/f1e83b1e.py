"""
You need to write a Python function that establishes a secure LDAP connection over SSL/TLS (LDAPS) to an LDAP server. The function should authenticate with the provided credentials and perform a simple search operation.
"""
def secure_ldap_connection(ldap_server, port, bind_dn, password, search_base, search_filter):
    server = Server(ldap_server, port=port, use_ssl=True)
    conn = Connection(server, user=bind_dn, password=password, authentication=SIMPLE)
    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException("Failed to bind to LDAP server")

        conn.search(search_base, search_filter, attributes=['*'])
        return conn.entries

    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f"LDAP error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        conn.unbind()