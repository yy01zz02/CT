        message = "== Getting templates | "
    else:
        message = "== Submmting solutions | "
    print (message + assignmentName)

# Get JWT token to access REST API
def getToken():
    if os.path.isfile(TOKEN_PICKLE_FILE_NAME):
        try:
            with open(TOKEN_PICKLE_FILE_NAME, 'rb') as accesstoken:
                token_file = pickle.load(accesstoken)
                return token_file['token'], token_file['username']
        except EOFError:
            print ("Existing access_token is NOT validated")
            return None, None
    else:
        return None,None


def getLoginInformation():