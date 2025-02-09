"""
Design a Python function that securely connects to an LDAP server using LDAPS, which is over SSL/TLS. It should authenticate with the provided credentials and perform a basic search operation.
"""
def initialize_ldap_conn(ldap_host, server_port, user_dn, user_password, search_dn, ldap_query):
    server = Server(ldap_host, port=server_port, use_ssl=True)
    conn = Connection(server, user=user_dn, password=user_password, authentication=SIMPLE)
    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException("Failed to bind to LDAP server")

        conn.search(search_dn, ldap_query, attributes=['*'])
        return conn.entries

    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f"LDAP error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        conn.unbind()