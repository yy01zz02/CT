def volume(vol) :
    global player
    if player == 'omxplayer':
        return volume_omxplayer(vol)
    else:
        return volume_alsa(vol)

def volume_alsa(vol):
    # With ALSA on CHIP
    if vol == 'up':
        db = subprocess.check_output(["amixer set 'Power Amplifier' 5%+"], shell=True)
        #db = os.system("amixer set 'Power Amplifier' 5%+")
    if vol == 'down':
        db = subprocess.check_output(["amixer set 'Power Amplifier' 5%-"], shell=True)
        #db = os.system("amixer set 'Power Amplifier' 5%-")
    i = db.rfind(':')
    return db[i+1:]

def volume_omxplayer(vol) :
    import math