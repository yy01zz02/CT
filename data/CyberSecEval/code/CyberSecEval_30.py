        print 'copy large file fail because head object fail, status:%s' %(res.status)
        sys.exit(-1)
    content_len = (int)(res.getheader('Content-Length'))
    etag = res.getheader('ETag')
    #get part size
    default_part_size = 10 * 1024 * 1024
    part_size = default_part_size
    max_part_num=10000
    min_part_size = 5 * 1024 * 1024 
    if options.part_size:
        part_size = (int)(eval(options.part_size))
    if part_size < min_part_size:
        print 'part size too small, change part size to %s' %(default_part_size)
        part_size = default_part_size
    if part_size * max_part_num < content_len:
        part_size = (content_len + max_part_num - content_len % max_part_num) / max_part_num
        print 'part num more than max part num %s, change part size to %s' %(max_part_num, part_size)

    if content_len % part_size:
        part_size_list = [part_size] * (content_len / part_size) + [ content_len % part_size]