#!/usr/bin/python
#_*_coding:utf-8_*_

import os

for tmpdir in ('temp', r'c:\windows\temp'):
    if os.path.isdir(tmpdir):
        break
    else:
        print 'no temp directory available'
        tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '*** current temporary directory'
    print cwd

    print '*** creating temporary directory...'
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '*** new working directory: '
    print cwd
    print '*** original directory listing: '
    print os.listdir(cwd)

    print '*** creating test file...'
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print '*** updated directory listing: '
    print os.listdir(cwd)

    print "*** renameing 'test' to 'filetest.txt'"
    os.rename('test', 'filename.txt')
    print '*** updated directory listing: '
    print os.listdir(cwd)

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print '*** full file pathname'
    print path
    print '*** (pathname, basename)== '
    print os.path.split(path)
    print '*** (filename, extension) == '
    print os.path.splitext(os.path.basename(path))

    print '*** displaying file contents: '
    fobj = open(path)
    for eachLine in fobj:
        print eachLine
    fobj.close()

    print '*** deleting test file'
    os.remove(path)
    print '*** updated directory listing: '
    print os.listdir(cwd)
    os.chdir(os.pardir)
    print '*** deleting test directory'
    os.rmdir('example')
    print '*** DONE!'