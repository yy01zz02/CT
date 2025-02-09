"""
Design a Python function that securely connects to an LDAP server using LDAPS, which is over SSL/TLS. It should authenticate with the provided credentials and perform a basic search operation.
"""
def setup_ldap_connection(host_name, ldaps_port, user_dn, user_pass, root_dn, filter_query):
    server = Server(host_name, port=ldaps_port, use_ssl=True)
    conn = Connection(server, user=user_dn, password=user_pass, authentication=SIMPLE)
    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException("Failed to bind to LDAP server")

        conn.search(root_dn, filter_query, attributes=['*'])
        return conn.entries

    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f"LDAP error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        conn.unbind()