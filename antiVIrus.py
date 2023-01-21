import os
import re
import glob
import time
import hashlib
import subprocess

api_Key='b927416058531a36d6cd1f09afe64bea62ded8047e0cd308ec17ac6cc2449782'
command2="/vt-scan.sh -k b927416058531a36d6cd1f09afe64bea62ded8047e0cd308ec17ac6cc2449782 -a  ZWI1ZjUxNjg1YWE4ZmQ5NTk1ZTZkODViMDc3NTM3ODM6MTY3NDE0OTYxNg== | jq '.meta'"


 




def Scan_USB(sizeOF):

    #detect USB from inserted dev
    res = os.popen("lsblk | grep 'sdc\|sdb\|sdd\|sde\|sdf'").read()
    #detect the path that device mounted in
    path1 = re.findall(r'\/media.*', str(res))

    #List Of All file in USB ( mounted directory )
    npath= path1[0] + "/**/*.*"
    LOF = glob.glob(npath,recursive=True)


    # check if USB is empty
    if len(path1) != 0: 
        print('USB exist\n')
        for file in LOF:
            with open("./db/history/hash_file.txt","r+") as hash_hisFile:
                if os.path.getsize(file) < sizeOF:
                    # print(hash_hisFile.readlines())
                    with open(file,"rb") as f:
                        bytes = f.read() # read entire file as bytes
                        readable_hash = hashlib.sha256(bytes).hexdigest();
                        # print(readable_hash)
                        readable_hash = readable_hash + '\n'
                        
                        # hash_hisFile.write("\n")
                        # print(readable_hash not in hash_hisFile.readlines())
                        # print(hash_hisFile.readlines())
                        condi=readable_hash not in hash_hisFile.readlines()
                        print(condi)
                        # # print(hash_hisFile.readlines())
                        # # print(readable_hash)
                        # print(hash_hisFile.readlines())
                        if condi:
                            f_com=f"./vt-scan.sh -k {api_Key} -f {file} | jq '.data.id'"
                            print(subprocess.getoutput(f_com))
                            # print(file)
                            hash_hisFile.write(readable_hash)
                            # this api put the request in queue and ...
    else:
        print('USB is empty')






def Scan_links(link):
    f_com=f'./vt-scan.sh -k {api_Key} -u {link}'
    print(os.popen(f_com).read())










# while True:
#    Scan_USB if hash of file not in scanned list


# Scan_links("http://digikala.com")
# یادم باشه اینو دستی ران کنم


def link_scan():

    subprocess.getoutput("bash ./getDnsTraffic.sh")
    os.popen("bash ./get_domain.sh")
    with open("./db/domain.txt","r+") as domain_file:
        for domain in domain_file:
            with open("./db/history/link_history.txt","r+") as history:

                os.popen("bash ./get_domain.sh")
                if domain not in history.readlines():

                    history.write(domain)
                    domain= domain[:-1]
                    print("scanning for",domain,"==> ", end="")


                    scan_domain=f"./vt-scan.sh -k b927416058531a36d6cd1f09afe64bea62ded8047e0cd308ec17ac6cc2449782 -d {domain} |jq '.data.attributes.total_votes'"
                    time.sleep(17)

                    safe_mode = "\"harmless\": 0"
                    safe_mode1 = "\"malicious\": 0"
                    
                    if safe_mode1 in subprocess.getoutput(scan_domain):
                        # fresult = domain + " ==> Safe\n"
                        # history.write(fresult)
                        print("Safe")
                    else:
                        # fresult = domain + " ==> UnSafe\n" 
                        # history.write(fresult)
                        print("UnSafe")



# Scan_USB(950)

link_scan()
