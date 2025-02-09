            title=u"Hinet系統公告",
            link="http://www.hinet.net/pu/notify.htm",
            description=u"此RSS內容取自Hinet網頁，依照著作權法之合理使用原則節錄部份內容。\
            本RSS僅供參考，Hinet或任何人都不對內容負責",
            lastBuildDate=mtime,
            items=items)

        output = StringIO.StringIO()
        rss.write_xml(output,encoding='utf-8')

        etag = hashlib.sha1(output.getvalue()).hexdigest()

        memcache.set('hinet_rss', output.getvalue(), time=3600)
        memcache.set('h_mtime', mtime, time=3600)
        memcache.set('h_etag', etag, time=3600)

        self.set_headers()
        self.response.headers['ETag'] = '"%s"' % (etag,)
        self.output_content(output.getvalue(), serve)
