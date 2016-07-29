while true 
do
nmap -sn 192.168.0.1/24 | grep MAC >macs1
nmap -sn 192.168.0.1/24 | grep MAC >macs2
diff macs1 macs2 >diff
done
