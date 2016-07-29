import subprocess
import sys
import time
import config
from pushetta import Pushetta

nmap1 = "nmap -sn 192.168.0.1/24 | grep MAC >macs1"
nmap2 = "nmap -sn 192.168.0.1/24 | grep MAC >macs2"
diff = "diff macs1 macs2 >diff"


x = subprocess.call( nmap1, shell=True)

while True:
    x = subprocess.call( nmap2, shell=True)
    x = subprocess.call( diff,shell=True)

    lines = open("diff", "r") 
    for line in lines:
	if ( line[0] == '>') :
		info =  " %s has JOINED" % line
		ps = Pushetta(config.API_KEY)
    		ps.pushMessage(config.CHANNEL_NAME, info)
	if ( line[0] == '<') :
		info =  " %s has LEFT" % line
		ps = Pushetta(config.API_KEY)
    		ps.pushMessage(config.CHANNEL_NAME, info)

    
    x = subprocess.check_output( "cp macs2 macs1", shell=True)
    time.sleep(10)
