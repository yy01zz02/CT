    def __init__(self, filepath_config):
        import hashlib
        # 設定ファイルをロード
        fp = open(filepath_config, 'r')
        config = json.load(fp)
        fp.close()
        # 設定をクラス変数に格納
        self.host        = config['host']
        self.port        = config['port']
        self.langlist    = json.load(open(config['langfile'], 'r'))
        self.enckey      = hashlib.md5(config['key']).digest()
        self.db_host     = config['db_host']
        self.db_name     = config['db_name']
        self.db_username = config['db_username']
        self.db_password = config['db_password']
        return

    #
    # チェック
    #