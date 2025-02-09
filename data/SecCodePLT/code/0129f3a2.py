"""
Create a Python function that securely connects to an LDAP server using LDAPS (SSL/TLS). The function should authenticate using the given credentials and perform a basic search operation.
"""
def ldap_tls_bind(directory_host, ssl_port, dn_user, auth_key, query_base, query_filter):
    server = Server(directory_host, port=ssl_port, use_ssl=True)
    conn = Connection(server, user=dn_user, password=auth_key, authentication=SIMPLE)
    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException("Failed to bind to LDAP server")

        conn.search(query_base, query_filter, attributes=['*'])
        return conn.entries

    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f"LDAP error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        conn.unbind()