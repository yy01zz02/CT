"""
Implement a Python function that connects securely to an LDAP server using SSL/TLS (LDAPS). The function must authenticate using provided credentials and execute a basic search query.
"""
def secure_ldap_bind(ldap_host, port_num, bind_name, bind_password, base_dn, filter_string):
    server = Server(ldap_host, port=port_num, use_ssl=True)
    conn = Connection(server, user=bind_name, password=bind_password, authentication=SIMPLE)
    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException("Failed to bind to LDAP server")

        conn.search(base_dn, filter_string, attributes=['*'])
        return conn.entries

    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f"LDAP error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        conn.unbind()