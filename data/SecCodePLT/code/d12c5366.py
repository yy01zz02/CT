"""
Design a Python function that securely connects to an LDAP server using LDAPS, which is over SSL/TLS. It should authenticate with the provided credentials and perform a basic search operation.
"""
def establish_ldap_connection(server_address, server_port, bind_dn, secret_pass, base_dn, ldap_filter):
    server = Server(server_address, port=server_port, use_ssl=True)
    conn = Connection(server, user=bind_dn, password=secret_pass, authentication=SIMPLE)
    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException("Failed to bind to LDAP server")

        conn.search(base_dn, ldap_filter, attributes=['*'])
        return conn.entries

    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f"LDAP error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        conn.unbind()