            notify.sync()
    notify.close()

def happiness_detect(info) :
    """Checks to see if a smiley is in the message"""
    for emotion in [":)", ":D", "C:", "=D", "=)", "C=", "(=", "(:" "xD", ":p", ";p", "=p", ":(", "D:", "=(", "D=", "):", ")=", "=C", ":C", ":P"] :
        if emotion in info["message"] : return True
    return False
def on_ACTION(connection, info) :
    """Runs every time somebody does an action (/me)"""
    badwords = shelve.open("badwords.db", writeback=True)
    if badwords.has_key(connection.host) :
        if badwords[connection.host].has_key(info["channel"]) :
            nosay = badwords[connection.host][info["channel"]]["badwords"]
            for word in nosay :
                if word in [message.replace(".", "").replace("!","").replace("?", "") for message in info["message"].lower().split(" ")] :
                    if info["sender"] not in badwords[connection.host][info["channel"]]["users"] :
                        badwords[connection.host][info["channel"]]["users"][info["sender"]] = 0
                        badwords.sync()
#                    if badwords[connection.host][info["channel"]]["users"][info["sender"]] > 0 :