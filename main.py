from time import sleep


def input_slice(string):
    list1 = []
    list1[:0] = string
    return list1


def ip_to_bin():
    sleep(1)
    ip = input("\nIP to convert: ")
    sleep(1)

    if ip == "99":
        print("Exiting!")
        exit()

    elif not 7 <= len(ip) <= 15:
        print("\nThis IP is Invalid")

    else:
        for _ in input_slice(ip):
            if not _ in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                print("\nThis is not an IP")
                break
            else:
                binary = " ".join(format(ord(char), "b") for char in ip)
                sleep(1)

                enc_out = f"\nIp          : {ip} \n\nBinary Code : {binary}"

                print(enc_out)
                break


def bin_to_ip():
    sleep(1)
    bin_code = input("\nBinary Code to convert: ")
    sleep(1)

    if bin_code == "99":
        print("Exiting!")
        exit()

    elif not 48 <= len(bin_code) <= 109:
        print("\nThis is for an invalid ip")

    elif bin_code == "110010 110101 110101 101110 110010 110101 110101 101110 110010 110101 110101 101110 110010 110101 110101":
        print(f"\nBinary Code : {bin_code} \n\nIp          : 255.255.255.255 (Broadcast IP)")
        
    else:
        for _ in input_slice(bin_code):
            if not _ in ["1", "0", " "]:
                print("\nThis is not a Binary Code")
                break
            else:
                ip = "".join(chr(int(k, 2)) for k in bin_code.split(" "))

                sleep(1.5)

                dec_out = f"\nBinary Code : {bin_code} \n\nIp          : {ip}"

                print(dec_out)
                break


while True:
    try:
        mode = input('''
|-PRESS-----------------|
| 1 - Ip to Binary      |
| 2 - Binary to IPv4/v6 |
| 99 - Quit             |
|-----------------------|
|--> ''')

        if mode == "1":
            ip_to_bin()

        elif mode == "2":
            bin_to_ip()

        elif mode == "99":
            print("Exiting!")
            exit()

    except KeyboardInterrupt:
        print("Alright!")
