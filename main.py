import os
os.system("curl $name >/home/rclone.conf")
os.system("/home/rclone rcd --rc-serve --rc-addr=0.0.0.0:8000 --config=/home/rclone.conf")
