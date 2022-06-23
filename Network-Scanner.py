import subprocess

network_portion: str = ".".join(
    subprocess.check_output(["hostname", "-I"]).decode(encoding="utf-8").split(" ")[0].split(".")[0:3])


def check_address(host_portion: str):
    ip4: str = network_portion + "." + host_portion
    try:
        output: str = subprocess.check_output(["nslookup", ip4]).decode(encoding="utf-8")
        name: str = output.split("name = ")[1].strip().replace("\n", " ")
        print("Device found " + ip4, name)
    except:
        return


if __name__ == "__main__":
    for index in range(256):
        check_address(str(index))
