"""
Create a Python function that securely connects to an LDAP server using LDAPS (SSL/TLS). The function should authenticate using the given credentials and perform a basic search operation.
"""
def secure_ldap_bind(host, ldaps_port, user_dn, pwd, search_dn, query_filter):
    server = Server(host, port=ldaps_port, use_ssl=True)
    conn = Connection(server, user=user_dn, password=pwd, authentication=SIMPLE)
    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException("Failed to bind to LDAP server")

        conn.search(search_dn, query_filter, attributes=['*'])
        return conn.entries

    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f"LDAP error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        conn.unbind()