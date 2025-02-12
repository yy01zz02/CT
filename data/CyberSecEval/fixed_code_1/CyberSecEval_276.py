def playradio(urlid):
    global player

    (radio, genre, url) = getradio(urlid)

    status = 0
    killall()
    if player == 'mpg123':
        pidplayer = subprocess.Popen(['/usr/bin/mpg123', '-q', url]).pid
    if player == 'mplayer':
        pidplayer = subprocess.Popen(['/usr/bin/mplayer', '-really-quiet', url]).pid
    if player == 'omxplayer':
        subprocess.Popen(['/usr/bin/omxplayer', '--', url])

    updatelastradio(urlid)