    latest = data["object"]["sha"]
    
    #ind = page.find('class="sha btn btn-outline"')
    #latest = page[ind + 38:ind + 45]
    #print(latest)
    
    #CHECK IF LATEST IS PROPER
    
    try:
        f = open("Update/current.version", "rb")
        current = pickle.load(f)
        f.close()
    except:
        print("create new file")
        try:
            os.mkdir("Update")
        except:
            pass
        f = open("Update/current.version", "wb")
        current = 0000