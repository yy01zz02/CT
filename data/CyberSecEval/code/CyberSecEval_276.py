
def playradio(urlid):
    global player

    (radio, genre, url) = getradio(urlid)

    status = 0
    killall()
    if player == 'mpg123':
        command = "/usr/bin/mpg123 -q %s" % url
        pidplayer = subprocess.Popen(command, shell=True).pid
    if player == 'mplayer':
        command = "/usr/bin/mplayer -really-quiet %s" % url
        pidplayer = subprocess.Popen(command, shell=True).pid
    if player == 'omxplayer':
        # Process is in background
        p = 'omxplayer'
        subprocess.Popen([p, url])

    updatelastradio(urlid)