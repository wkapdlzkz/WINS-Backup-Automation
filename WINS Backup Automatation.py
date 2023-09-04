import csv
import sys
import logging
import paramiko
import socket
import os, time, datetime
from stat import S_ISDIR

class SSHSession(object):


        def __init__(self, hostname, portnumber, username):

                self.hostname = hostname
                self.portnumber = portnumber

                self.transport = paramiko.Transport((self.hostname, self.portnumber))
                self.k = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
                self.username = username
                self.transport.connect(username = self.username, pkey = self.k)
                self.sftp = paramiko.SFTPClient.from_transport(self.transport)

        def get(self,remotefile,localfile):
        #  Copy remotefile to localfile, overwriting or creating as needed.
                self.sftp.get(remotefile,localfile)

        def sftp_walk(self,remotepath):
        # Kindof a stripped down  version of os.walk, implemented for
        # sftp.  Tried running it flat without the yields, but it really
        # chokes on big directories.
                path=remotepath
                files=[]
                folders=[]

                for f in self.sftp.listdir_attr(remotepath):
                        if S_ISDIR(f.st_mode):
                                folders.append(f.filename)
                        else:
                                files.append(f.filename)
                
                yield path,folders,files
                for folder in folders:
                        new_path = os.path.join(remotepath,folder)
                        for x in self.sftp_walk(new_path):
                                yield x

        def get_all(self,remotepath,localpath):


                self.sftp.chdir(os.path.split(remotepath)[0])
                parent=os.path.split(remotepath)[1]

                try:
                        os.mkdir(localpath)
                except:
                        pass
                for walker in self.sftp_walk(parent):
                        try:
                                os.mkdir(os.path.join(localpath,walker[0]))
                        except:
                                pass
                        for file in walker[2]:
                                self.get(os.path.join(walker[0],file),os.path.join(localpath,walker[0],file))






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
