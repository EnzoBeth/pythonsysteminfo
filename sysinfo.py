import platform, psutil, urllib.request

__author__ = "EnzoBeth"
hdd = psutil.disk_usage('/')


# We check if user is connected to Internet here !
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


print("=" * 40, "システム情報", "=" * 40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
print("Free disk space: %d GiB" % (hdd.free // (2 ** 30)))
print('Connected to Internet' if connect() else 'No internet access !')
print("=" * 92)
