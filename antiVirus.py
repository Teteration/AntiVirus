import os
import re
import glob

api_Key='b927416058531a36d6cd1f09afe64bea62ded8047e0cd308ec17ac6cc2449782'




cmd = "lsblk | grep 'sdc\|sdb'"
res = os.popen(cmd).read()
# print(str(res))
# # print(len(res))
# path = os.popen('grep /media')

path1 = re.findall(r'\/media.*', str(res))
# print(path1[0])


# command1="./vt-scan.sh a -k b927416058531a36d6cd1f09afe64bea62ded8047e0cd308ec17ac6cc2449782 -f ~/Desktop/exploit.sh"
command2="/vt-scan.sh -k b927416058531a36d6cd1f09afe64bea62ded8047e0cd308ec17ac6cc2449782 -a  ZWI1ZjUxNjg1YWE4ZmQ5NTk1ZTZkODViMDc3NTM3ODM6MTY3NDE0OTYxNg== | jq '.meta'"

# print(f_com)
#گام بعدی اینه که ریزالت اسکنر رو گرپ بزنیم و ... همچنین تایین سایز فایل برای اسکن هم مهمه
# برنامه طوری باشه که با کامند بشه همه چی رو کنترل کرد!


# com1 = f"ls -d '{path1[0]}'/*"
# com1 = 
# LOF = os.popen(com1).read()
# LOF = os.walk(path1[0]).read()
# print(LOF)





# # folder path

# # list to store files
# res = []

# # Iterate directory
# for path in os.listdir(path1[0]):
#     # check if current path is a file
#     if os.path.isfile(os.path.join(path1[0], path)):
#         res.append(path)
# print(res)


# dir_path = r'E:\account\*.*'
npath= path1[0] + "/**/*.*"
# print(npath)
LOF = glob.glob(npath,recursive=True)
# print(res[6])
#



if len(path1) != 0: # check if usb is empty
    # for filename in os.listdir(path1[0]):
    print('USB exist')
    for file in LOF:
        # print(file)
    # if os.path.isfile(file) == True:
        f_com=f'./vt-scan.sh -k {api_Key} -f {file}'
        print(os.popen(f_com).read())
        # print(file)

else:
    print('USB is empty')


