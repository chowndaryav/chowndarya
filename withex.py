import pexpect
import sys
import re

class conn_error(RuntimeError):
  def __init__(self,args):
     self.args=args
class file_error(RuntimeError):
  def __init__(self,arg):
     self.args=arg
class close_error(RuntimeError):
  def __init__(self,arg):
     self.args=arg

   
try:
 child = pexpect.spawn ('ftp ftpopenbsd.org')
 if not child:
  raise conn_error("ftp_con")
 index=child.expect (['Name .*: ','name.*:','ftp>'])
 if index==0 or index==1:
   child.sendline ('anonymous')
   hey1=child.expect ('Password:','ftp>')
   if hey1==0:
    child.sendline ('chowndarya94@gmail.com')
    
#child.expect ('ftp> ')

 nom=len(sys.argv)
 i=1
 while(i<nom):
   child.expect('ftp> ')
   red="get" +" " +str(sys.argv[i])
   mat=re.match(r'get (.*)\.(txt|bin|asc|csv)',red,re.I)
   if not mat:
     raise file_error("file_name")
   child.sendline(red)
   i=i+1
 child.expect('ftp> ')
 if child.isalive():
   child.sendline('exit') 
   
 if child.isalive():
   raise close_error("closing")
 else:
   print "ftp closed successfully"

except conn_error:
 print "connection not established"

except file_error:
 print "file name unknown"

except close_error:
 print "ftp not closed successfully"
 child.sendline('exit')

except pexpect.TIMEOUT :
 print "we timedout"

except pexpect.EOF:
 print "end of file reached"




    


