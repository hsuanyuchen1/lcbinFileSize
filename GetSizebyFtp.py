import os
import ftplib
import time

start_time = time.time()
megap_dir = ['0000', '0015', '0030', '0045', '0100', '0115', '0130', '0145', '0200', '0215', '0230', '0245', '0300', '0315', '0330', '0345', '0400', '0415', '0430', '0445', '0500', '0515', '0530', '0545', '0600', '0615', '0630', '0645', '0700', '0715', '0730', '0745', '0800', '0815', '0830', '0845', '0900', '0915', '0930', '0945', '1000', '1015', '1030', '1045', '1100', '1115', '1130', '1145', '1200', '1215', '1230', '1245', '1300', '1315', '1330', '1345', '1400', '1415', '1430', '1445', '1500', '1515', '1530', '1545', '1600', '1615', '1630', '1645', '1700', '1715', '1730', '1745', '1800', '1815', '1830', '1845', '1900', '1915', '1930', '1945', '2000', '2015', '2030', '2045', '2100', '2115', '2130', '2145', '2200', '2215', '2230', '2245', '2300', '2315', '2330', '2345']


########ftp information

ftp_addr = ['192.168.250.33'] 





#ftp username and password
usrname = "*****"
pw = "*****"

###########################################
#change to '//' !!!Reme
head_addr = '//'
####date information///ddmmyy
date = ['010320', '020320', '030320', '040320' ]

#File directory for lcbin file size results
txt_name = r'C:\Users\actix.service\Desktop\lcbinSize.txt'

for i in range(len(ftp_addr)):
    for j in range(len(date)):
        size = 0
        print(ftp_addr[i])
        #log in ftp
        ftp = ftplib.FTP(ftp_addr[i], usrname, pw, timeout=5)
        for d in range(len(megap_dir)):   
            #change directory
            t_addr = os.path.join(head_addr + date[j], megap_dir[d])
            try:
                ftp.cwd(t_addr)
                print(t_addr)
                for f in ftp.nlst(t_addr):
                    size += ftp.size(f)
                    print('>', end='')
            except:
                size += 0
                 
        print('{0:s}, {1:s}, {2:.2f} GB'.format(ftp_addr[i], date[j], size/1024/1024/1024))
        with open(txt_name, 'a') as result:
            print('{0:s}, {1:s}, {2:.2f}GB'.format(ftp_addr[i], date[j], size/1024/1024/1024), file=result)

        
print("--- %s seconds ---" % (time.time() - start_time))

