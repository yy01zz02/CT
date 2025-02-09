        if ret != 0:
            logging.error("QTTSSessionEnd failed, error code:{}".format(ret))

        return ('wav', fname)


if __name__ == '__main__':
    tts = iflytekTTS()
    def md5sum(contents):
        import hashlib
        hash = hashlib.md5()
        hash.update(contents)
        return hash.hexdigest()

    import sys
    basename = md5sum(sys.argv[1])
    t, f = tts.get_tts_audio(sys.argv[1], basename, 'zh');

    def mplayer(f):
        import commands