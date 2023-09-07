import os,platform
os.system('git pull')
os.system('xdg-open https://chat.whatsapp.com/GWvXgZ6ko0CDSjRmtWMIKy')
 
trt=platform.architecture()[0]
if trt=="32bit":
    __import__("zf1")
elif trt=="64bit":
    __import__("zf1")
