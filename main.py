
from time import sleep


def ip_to_bin():
    sleep(1)
    ip = input("\nIP to convert: ")
    sleep(1)

    binary = " ".join(format(ord(char), "b") for char in ip)
    sleep(1)

    enc_out = f"\nIp          : {ip} \n\nBinary Code : {binary}"

    print(enc_out)


def bin_to_ip():
    sleep(1)
    bin_code = input("\nBinary Code to convert: ")
    sleep(1)

    ip = "".join(chr(int(k, 2)) for k in bin_code.split(" "))

    sleep(1.5)

    dec_out = f"\nBinary Code : {bin_code} \n\nIp          : {ip}"

    print(dec_out)


while True:
    try:
        print("\n1 - Ip to Binary  |  2 - Binary to IPv4/v6 |  Q - Quit")
        get_input = input("\nWhat Do You Want? : ")

        if get_input == "1":
            ip_to_bin()

        elif get_input == "2":
            bin_to_ip()

        elif get_input == "q" or "Q":
            print("Exiting!")
            exit()

    except KeyboardInterrupt:
        print("Alright!")
