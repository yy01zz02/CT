    for x in range(json_dict["command_count"]):
        x = x + 1
        print '\033[91m' +"Line: ", x,'\n'
        print '\033[92m'+ "Comment: ", json_dict[str(x)]["comment"],'\n'
        print '\033[96m' + "Input: ", json_dict[str(x)]["command"][:-1]
        outfile = os.popen(json_dict[str(x)]["command"])
        output = outfile.read()
        return_val = outfile.close()
        if return_val != None:
            shell-scribe().send_call()
        print '\033[93m' + "Output: ", os.popen(json_dict[str(x)]["command"]).read() + '\033[0m'
        raw_input("-Press Enter-\n")
    #not sure what to do with the rest of this code. whether or not it is even necessary
    #with open('test.sh','r') as file:
    #          for row in file:
    #                print '\033[91m' + "\nCode for the row: " + '\033[96m' + row + '\033[92m'
    #                comment=raw_input('- ')
    #                tempDic = {'comment':comment,'command':row}
    #                dic.update({inc:tempDic})
    #                inc+=1