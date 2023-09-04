import csv
import sys, traceback
import paramiko
import getpass
import time
import datetime
import logging


class SENDMessage(object):


        def __init__(self, hostname, portnumber):
                self.nowDate = datetime.datetime.now()

                self.hostname = hostname
                self.portnumber = portnumber
                #sys.stdout = open(self.hostname + self.nowDate.strftime("_%Y-%m-%d_%H%M") + ".txt","w")

                self.cli=paramiko.SSHClient()
                self.cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.cli.connect(self.hostname, username='root', key_filename='/root/.ssh/id_rsa', port=self.portnumber, look_for_keys=False, allow_agent=False)

                self.DEVICE_ACCESS = self.cli.invoke_shell()
                self.DEVICE_ACCESS.settimeout(650000)

                time.sleep(1)
                self.DEVICE_ACCESS.send(b'find /backup/ -name \'LogFiles_20*.tar.gz\' -mtime +150 -delete \n')
                time.sleep(1)
                self.DEVICE_ACCESS.send(b'cd /backup/Config_Gathering\n')
                time.sleep(1)
                self.DEVICE_ACCESS.send(b'find /backup/Config_Gathering/ -name \'*_ISCONFIG.txt\' -mtime +150 -delete \n')
                time.sleep(5)
                self.DEVICE_ACCESS.send(b'find /backup/Config_Gathering/ -name \'*_config_gathering.txt\' -mtime +150 -delete \n')
                time.sleep(5)
                self.DEVICE_ACCESS.send(b'rm -f backup.tar.gz\n')
                time.sleep(5)
                self.DEVICE_ACCESS.send(b'tar cvfz backup.tar.gz /home1/sniper/config\n')
                time.sleep(25)
                self.DEVICE_ACCESS.send(b'config_gathering\n')

                self.status='Normal'
                while self.status!='End':
                        time.sleep(1)
                        self.resp = str(self.DEVICE_ACCESS.recv(650000))
                        print(self.resp)
                        if self.resp.count('here>>>')>0:
                                self.status='End'
                                time.sleep(5)



                DEVICE_ACCESS.close()
                #sys.stdout.close()



def main():


        logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)



        filename = datetime.datetime.now().strftime("/backup_home/logs/message_%Y%m%d%H%M%S.log")
        fileHandler = logging.FileHandler(filename, encoding="utf-8")
        fileHandler.setFormatter(logFormatter)
        logger.addHandler(fileHandler)

        with open('/backup_home/list/list.csv', 'r') as reader:
                for line in reader:
                        fields = line.strip().split(':')
                        tt_h = fields[0]
                        tt_p = int(fields[1])

                        try:

                                ssh = SENDMessage(tt_h, tt_p)
                                pass



                        except Exception:
                                pass






if __name__ == '__main__':
        main()







def main():

        logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)



        filename = datetime.datetime.now().strftime("/to.. path .. /backup_message_%Y%m%d%H%M%S.log")
        fileHandler = logging.FileHandler(filename, encoding="utf-8")
        fileHandler.setFormatter(logFormatter)
        logger.addHandler(fileHandler)

        with open('/backup_home/list.csv', 'r') as reader:
                for line in reader:
                        fields = line.strip().split(':')
                        tt_h = fields[0]
                        tt_p = int(fields[1])





                        try:
                                ssh = SSHSession(tt_h, tt_p, 'root')
                                #ssh.get_all('/var/log','/sftp_home/IDPS/' + tt_h + '/' + time.strftime('%Y-%m-%d_%H-%M-%S'))
                                os.makedirs('/to.. path .. /' + tt_h + '/' + time.strftime('%Y-%m-%d_%H-%M'), exist_ok = True)
                                #os.makedirs('/sftp_home/IDPS/' + tt_h + '/' + time.strftime('%Y-%m-%d_%H-%M') + '/sniper/', exist_ok = True)
                                ssh.get_all('/to.. path .. ','/to.. path .. /' + tt_h + '/' + time.strftime('%Y-%m-%d_%H-%M'))


                        except Exception:
                                pass




        with open('/backup_home/list/list.csv', 'r') as reader:
                for line in reader:
                        fields = line.strip().split(':')
                        tt_h = fields[0]
                        tt_p = int(fields[1])





                        try:
                                ssh = SSHSession(tt_h, tt_p, 'root')
                                #ssh.get_all('/var/log','/sftp_home/IDPS/' + tt_h + '/' + time.strftime('%Y-%m-%d_%H-%M-%S'))
                                os.makedirs('/to.. path .. /' + tt_h + '/' + time.strftime('%Y-%m-%d_%H-%M'), exist_ok = True)
                                #os.makedirs('/sftp_home/IDPS/' + tt_h + '/' + time.strftime('%Y-%m-%d_%H-%M') + '/sniper/', exist_ok = True)
                                ssh.get_all('to.. path .. ','/to.. path .. /' + tt_h + '/' + time.strftime('%Y-%m-%d_%H-%M'))


                        except Exception:
                                pass




if __name__ == '__main__':
        main()









