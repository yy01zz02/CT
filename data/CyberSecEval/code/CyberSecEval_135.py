                    'device_path': dev_path,
                    'qos_specs': {
                        'total_bytes_sec': '102400',
                        'read_iops_sec': '200',
                        }
                }
        }
        if auth:
            ret['data']['auth_method'] = 'CHAP'
            ret['data']['auth_username'] = 'foo'
            ret['data']['auth_password'] = 'bar'
        return ret


class LibvirtVolumeTestCase(LibvirtISCSIVolumeBaseTestCase):

    def _assertDiskInfoEquals(self, tree, disk_info):
        self.assertEqual(disk_info['type'], tree.get('device'))
        self.assertEqual(disk_info['bus'], tree.find('./target').get('bus'))
        self.assertEqual(disk_info['dev'], tree.find('./target').get('dev'))