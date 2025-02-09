    conf['LOGIN']['password'] = pwd
    with open('config.ini', 'w') as configfile:
        conf.write(configfile)
    print('写入成功')


# 读取用户数据
config = configparser.ConfigParser()
config.read('config.ini')
username = ''
password = ''
if 'LOGIN' in config:
    username = config['LOGIN']['username']
    password = config['LOGIN']['password']
else:
    print('确保已完成登陆.请填写用户名和密码.')

# 接入新浪接口基本信息
api_key = '3842240593'
api_secret = '93f0c80150239e02c52011c858b20ce6'