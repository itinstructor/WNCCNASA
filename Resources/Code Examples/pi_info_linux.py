import sys
import subprocess

cmd = "cat /proc/device-tree/model"
model = subprocess.check_output(cmd, shell=True).decode("utf-8")
print(model)

print("Python: " + sys.version)
cmd = "hostname -I"
IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
print("IP: " + IP)

cmd = "vcgencmd measure_temp"
temp = subprocess.check_output(cmd, shell=True).decode("utf-8")
print(temp)

cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
print(CPU)

cmd = "free -m | awk 'NR==2{printf \"Memory usage: %s/%s MB %.2f%%\", $3,$2,$3*100/$2 }'"
MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
print(MemUsage)

cmd = "df -h | awk '$NF==\"/\"{printf \"Disk usage: %d/%d GB %s\", $3,$2,$5}'"
DiskUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
print(DiskUsage)