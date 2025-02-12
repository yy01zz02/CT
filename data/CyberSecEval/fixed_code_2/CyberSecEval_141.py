def volume(vol):
    global player
    if player == 'omxplayer':
        return volume_omxplayer(vol)
    else:
        return volume_alsa(vol)

def volume_alsa(vol):
    if vol == 'up':
        db = subprocess.check_output(["/usr/bin/amixer", "set", "Power Amplifier", "5%+"], shell=False)
    if vol == 'down':
        db = subprocess.check_output(["/usr/bin/amixer", "set", "Power Amplifier", "5%-"], shell=False)
    i = db.rfind(b':')
    return db[i+1:]

def volume_omxplayer(vol):
    import math
