import string
import os
POSSIBLE_BUGS = ('shift left overflow',)
#POSSIBLE_BUGS = ('buffer overflow', 'signed multiplication overflow', 'division by zero', 'signed subtraction overflow', 'signed addition overflow', 'null pointer dereference', 'pointer overflow', 'shift left overflow', 'shift right overflow', 'bugon-free', 'bugon-bounds', 'bugon-null')
BUG_SEPARATOR = '---'
EXTENSION = '-poptck.txt'
DIR_NAME = 'poptcks/'

class StackReport(object):

    def __init__(self, package_name, report):
        self.package_name = package_name
        self.total = 0
        self.freqs = {}
        for b in POSSIBLE_BUGS:
            n = report.count(b)
            if n > 0:
                self.total += n
                self.freqs[b] = n

    def __str__(self):
        return '%s, info: %s' % (self.package_name, str(self.freqs))


if __name__ == '__main__':

    reports = []
    for f in os.listdir(DIR_NAME):
       f_name = os.path.join(DIR_NAME, f)
       if os.path.getsize(f_name) > 0:
          fd = open(f_name)
          reports.append(StackReport(f[:-len(EXTENSION)], fd.read()))
          fd.close()

    reports.sort(key = lambda x: x.total, reverse=True)

    print 'Total statistics:'
    freqs = dict((k, 0) for k in POSSIBLE_BUGS)
    s = 0
    for r in reports:
        s += r.total
        for k in r.freqs:
            freqs[k] += r.freqs[k]

    print 'Total %d, Distribution: %s' % (s, str(freqs))

    for r in reports:
        if len(r.freqs):
            print r

#with s as open("poptcks/4digits-poptck.txt"):
#   yaml.load(s) 
