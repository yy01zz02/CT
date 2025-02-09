                    for x in source:
                        if isinstance(x, EmbeddedSource):
                            s.add_source(x, method=method, reference=reference,
                                         analyst=analyst, tlp=tlp)
                s.add_tags(tags)
                s.save()
                obj.screenshots.append(screenshot_id)
                obj.save()
                final_screenshots.append(s)
    else:
        md5 = hashlib.md5(screenshot.read()).hexdigest()
        check = Screenshot.objects(md5=md5).first()
        if check:
            s = check
            s.add_tags(tags)
        else:
            s = Screenshot()
            s.analyst = analyst
            s.description = description
            s.md5 = md5