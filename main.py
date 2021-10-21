import os
import subprocess
import time
import re






def run_command(command):

    text_command = f"gem install {command}"

    print(text_command)

    os.system(text_command)




while True:
    command = "msfconsole &> text_command.txt"
    os.popen(command)
    time.sleep(1)

    ct = open('text_command.txt',"r")


 

    for line in ct.readlines():

        if "Could not find" in line:
            before_keyword, keyword, after_keyword  = line.partition("Could not find")
            command = after_keyword.split(" ")[1]
            version = command.split("-")[-1]
            # run_command(command,version)

            command = re.sub(r'-\d.+$','',command)
            command = f"{command}:{version}"
            run_command(command)

                    

                    





