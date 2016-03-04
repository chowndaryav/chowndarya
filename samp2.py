import pexpect
import sys

child = pexpect.spawn ('ftp ftp.openbsd.org')
child.expect ('Name .*: ')
child.sendline ('anonymous')
child.expect ('Password:')
child.sendline ('chowndarya94@gmail.com')
#child.expect ('ftp> ')

nom=len(sys.argv)
i=1
while(i<nom):
  child.expect('ftp> ')
  red="get" +" " +str(sys.argv[i])
  child.sendline(red)
  i=i+1

#child.sendline ('get robots.txt')
#child.expect('ftp> ')
#child.sendline ('get ls-lR.gz')
child.expect('ftp> ')
child.sendline ('bye')
