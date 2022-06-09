import subprocess
import platform
import threading

if not platform.system().lower() == "linux":
    print("the script only works under linux(parrot)")
    exit(1)
decoding: str = "utf-8"
net_part: str = ".".join(subprocess.check_output(["hostname","-I"]).decode(decoding).split(" ")[0].split(".")[0:3])


def check_device(host_portion: str):
    ip: str = net_part + "." + host_portion
    command: str = "ping " + ip + " -c 1"
    try:
        output: str = subprocess.check_output(command.split(" ")).decode(decoding)
        ttl: int = int(output.split(" ")[11].split("ttl=")[1])
        if ttl <= 64 and ttl >= 32:
            os: str = "Unix/Linux"
        elif ttl >= 64 and ttl <= 128:
            os: str = "Windows"
        else:
            os: str = "Solaris/AIX"
        print("Device found " + ip + " " + os + " " + subprocess.check_output(["date"]).decode(decoding).strip())
    except subprocess.CalledProcessError:
        return

if __name__ == "__main__":
    for index in range(1, 255):
        threading.Thread(target=lambda: check_device(str(index))).start()
