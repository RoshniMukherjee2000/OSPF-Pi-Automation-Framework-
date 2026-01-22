import subprocess
import paramiko
import  threading
import time

def iperf_server():
    proc = subprocess.Popen(
        ["iperf3", "-s"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print("iperf server started")
    time.sleep(10)
    # print(proc.stdin.read())
    proc.terminate()



def iperf_client():
    time.sleep(2)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect("192.168.10.200", username="mirafra", password='admin@123')  # connect

    stdin, stdout, stderr = ssh.exec_command("iperf3 -c 192.168.11.24 -b 100m -t 5 --bidir")
    print(stdout.read())


if __name__ == "__main__":
    t1= threading.Thread(target=iperf_server)
    t2 = threading.Thread(target=iperf_client)
    t1.start()
    t2.start()
    t2.join()
    t1.join()
    print('n')
    