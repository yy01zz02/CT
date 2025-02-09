"""
Implement a Python function that connects securely to an LDAP server using SSL/TLS (LDAPS). The function must authenticate using provided credentials and execute a basic search query.
"""
def ldap_secure_bind(server_host, server_port, dn, bind_pass, search_dn, search_filter):
    server = Server(server_host, port=server_port, use_ssl=True)
    conn = Connection(server, user=dn, password=bind_pass, authentication=SIMPLE)
    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException("Failed to bind to LDAP server")

        conn.search(search_dn, search_filter, attributes=['*'])
        return conn.entries

    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f"LDAP error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        conn.unbind()