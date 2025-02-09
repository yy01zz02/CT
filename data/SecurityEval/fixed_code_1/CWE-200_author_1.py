import logging

def isAuthorizedUser(userId):
    pass

def getUserBankAccount(userId, connection):
    if isAuthorizedUser(userId):
        try:
            sql = "SELECT * FROM user_bank_account WHERE user_id = ?"
            result = connection.execute(sql, (userId,))
            return result
        except Exception as e:
            logging.error("Unable to retrieve account information from database.")
            raise e
    else:
        return None
