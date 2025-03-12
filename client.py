# Net control
import socket
from time import sleep

# CONFIGS
#SSID="TestingNetwork"
#PSWD="Sup3rS4curePassw4rd"
UDP_RX_PORT=5210
UDP_TX_PORT=5211
MESSAGE_BASE="ThisIs@LongAndVariedSt4ingToShowDataCont!nuity__@334d316g8g"


rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rx.bind(("0.0.0.0", UDP_RX_PORT))

# tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# tx.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# msg="READY TO RX"
# tx.sendto(msg.encode("utf-8"), ("192.168.4.2", UDP_TX_PORT))
# print("readiness fired")
# tx.close

i = 0
# x = -1 #last num
end_msg = ""
def on_recieve(data):
    global i
    i += 1
    if rx.gettimeout() == None:
        rx.settimeout(1)
    # ddata = data.decode()
    # print("Received : " + str(ddata))
    # dint = int(ddata[0:2])
    # print(str(dint))
    # if x == -1:
    #     x = dint
    # elif x - dint != -1:
    #     print("missed packet(s): " + str(x+1) + " to " + str(x+dint))
    # print(get_zeros(i))
    # print(MESSAGE_BASE)
    # print(get_zeros(i) + MESSAGE_BASE)
    # if ddata == get_zeros(i)+MESSAGE_BASE:
    #     print("Successful reception!")
    # else:
    #     print("INCORRECT ITEM")
    #     i = int(ddata[0:2])

# def get_zeros(i):
#     count = int(3-str(i).__len__())
#     return str(count * "0") + str(i)

def test_done(x, d):
    if d != None:
        print("\nNo more packets recieved. Total packets: " + str(x) + "\n  Last pkt: " + str(d).split("\'")[1])
    else:
        print("\nNo more packets recieved. Total packets: " + str(x))
    
    rx.settimeout(None)

data = None
while True:
    try:
        data, addr = rx.recvfrom(1024)
        if data != None:
            on_recieve(data)
            # if str(data.decode()).split("\'")[0] == "999"+MESSAGE_BASE:
            #     test_done(i, data.decode())
            #     break
    except socket.timeout:
        test_done(i, data)
        i = 0
        data = None
    except KeyboardInterrupt:
        test_done(i, data)
        print("Exiting...")
        rx.close()
        break
    except Exception as e:
        test_done(i, data)
        print(str(e))
        rx.close()
        break
