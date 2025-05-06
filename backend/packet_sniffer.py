from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())  # Display packet details

sniff(prn=packet_callback, count=10)  # Capture 10 packets
