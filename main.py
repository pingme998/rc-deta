import os
os.system("curl $name >/home/rclone.conf")
os.system("/home/rclone rcd --rc-serve --config=/home/rclone.conf")
