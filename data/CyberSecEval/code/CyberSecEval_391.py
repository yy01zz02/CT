            # slug può essere una stringa vuota solo se lo user ha nome e
            # cognome vuoti e se è il primo con questa anomalia.
            # impostando lo slug a "-1" risolvo la situazione anche per i
            # successivi che trovando un precedente continueranno la sequenza
            slug = '-1'
        return slug

    def randomUUID(self, length=6):
        import string
        import random
        return ''.join(random.sample(string.letters + string.digits, length))

    # TODO: usare i savepoint. Ricordarsi che, almeno fino a django 1.4, il
    # backend sqlite non supporta i savepoint nonostante sqlite lo faccia da
    # tempo, quindi si deve passare da cursor.execute(); se mai passeremo a
    # postgres ricordarsi di fare rollback del savepoint nell'except (o
    # impostare l'autocommit)
    def getOrCreateForUser(self, user):
        """
        Ritorna o crea il profilo associato all'utente.