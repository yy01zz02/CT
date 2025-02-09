

def coraid_volume_size(gb):
    return '{0}K'.format(to_coraid_kb(gb))


fake_esm_ipaddress = "192.168.0.1"
fake_esm_username = "darmok"
fake_esm_group = "tanagra"
fake_esm_group_id = 1
fake_esm_password = "12345678"

fake_coraid_repository_key = 'repository_key'

fake_volume_name = "volume-12345678-1234-1234-1234-1234567890ab"
fake_clone_name = "volume-ffffffff-1234-1234-1234-1234567890ab"
fake_volume_size = 10
fake_repository_name = "A-B:C:D"
fake_pool_name = "FakePool"
fake_aoetarget = 4081