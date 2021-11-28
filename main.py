from scapy.all import *
from concurrent.futures import ThreadPoolExecutor
import json

Kmac = "3E:80:2D:48:22:B8".lower()

Dmac = "E0:DC:FF:F3:4E:01".lower()

Cmac = "5C:17:CF:89:44:D7".lower()

Nmac = "80:B0:3D:0D:7E:93".lower()



# win = tk.Tk()
# win.title("Ausgangsposition")
# win.minsize(800, 600)

# i=0
# d_label = tk.StringVar()
# n_label = tk.StringVar()
# k_label = tk.StringVar()
# c_label = tk.StringVar()

# def window():
    
#     frame1 = tk.LabelFrame(win, text="", fg="white", padx=15, pady=15)
#     frame1.grid(row=0, column=0)
#     l1 = tk.Label(frame1, textvariable=d_label, bg="red", fg="white")
#     frame2 = tk.LabelFrame(win, text="", padx=15, pady=15)
#     frame2.grid(row=0, column=1)
#     l2 = tk.Label(frame2, textvariable=k_label, bg="red")
#     frame3 = tk.LabelFrame(win, text="",fg="white", padx=15, pady=15)
#     frame3.grid(row=1, column=0)
#     l3 = tk.Label(frame3, textvariable=c_label, bg="red", fg="white")
#     frame4 = tk.LabelFrame(win, text="", padx=15, pady=15)
#     frame4.grid(row=1, column=1)
#     l4 = tk.Label(frame4, textvariable=c_label, bg="red")
#     l1.pack()
#     l2.pack()
#     l3.pack()
#     l4.pack()
    
#     # lab.place(x=20, y=30)
#     main()
    # win.mainloop()
    
def search_addr(ip):
    KAJETAN = False
    DAVID = False
    CLEMENT = False
    NATHAN = False
    mac = scan(ip)
    if mac == Dmac:
        DAVID = True
        
    if mac == Kmac:
        KAJETAN = True
        
    if mac == Cmac:
        CLEMENT = True
        
    if mac == Nmac:
        NATHAN = True
        
    l = [DAVID,NATHAN,CLEMENT,KAJETAN]
    return l


def util():
    resp = []
    # for i in range(5):
    ls = [("10.0.0."+str(i)) for i in range(55)]
    with ThreadPoolExecutor(32) as exec:
        resp = exec.map(search_addr, ls)
        # print("--- %s seconds ---" % (time.time() - start_time))

    d_list = []
    k_list = []
    n_list = []
    c_list = []
    for list in resp:
        
        d_list.append(list[0])
        n_list.append(list[1])
        c_list.append(list[2])
        k_list.append(list[3])
    data = {}
    data=[]
    data.append({
        'name': 'David',
        'present':any(d_list),
    })
    data.append({
        'name': 'Nathan',
        'present':any(n_list),
    })
    data.append({
        'name': 'Kajetan',
        'present':any(k_list),
    })
    data.append({
        'name': 'Clement',
        'present':any(c_list),
    })
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    if any(d_list):
        print('david is here')
      
    else:
        print('david is not here')

    if any(k_list):
        print('kajetan is here')

    else:
        print('kajetan is not here')

    if any(n_list):
        print('nathan is here')

    else:
        print('nathan is not here')

    if any(c_list):
        print('clement is here')

    else:
        print('clement is not here')

    return  data

    #  win.destroy()

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=1,
                            verbose=False)[0]
    return answered_list[0][1].hwsrc 

def scan(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=5,
                            verbose=False)[0]

    clients_list = []
    client_dict = {}
    for element in answered_list:
        client_dict = {"mac": element[1].hwsrc}
    
        clients_list.append(client_dict)
    mac = client_dict.get("mac")
    # print(mac)
    # print(ip)
    return mac
   


util()
