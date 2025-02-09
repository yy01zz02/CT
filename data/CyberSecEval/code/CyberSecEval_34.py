    s.connect((s_ip, int(s_port)))

    sendmsg(s,b'type@=loginreq/username@=/password@=/roomid@='+rid+b'/\x00')

    print('==========longinres')
    longinres= unpackage(recvmsg(s))

    #print('==========msgrepeaterlist')
    msgrepeaterlist= unpackage(recvmsg(s))
    lst= unpackage(msgrepeaterlist[b'list'])
    tb= unpackage(random.choice(tuple(lst.values())))

    #print('==========setmsggroup')
    setmsggroup= unpackage(recvmsg(s))
    
    ret= {'rid':rid,
          'username': longinres[b'username'],
          'ip': tb[b'ip'],
          'port': tb[b'port'],
          'gid': setmsggroup[b'gid']