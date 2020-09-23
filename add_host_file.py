#!/usr/bin/python
import os, re
from shutil import copyfile

def hosts_append(originalfile, appendfile):

    ## backup originalfile
    copyfile(originalfile, originalfile+'.bak')
    ## read originalfile into list
    f = open (originalfile, 'r')
    content_list = f.readlines()
    f.close()
    ## Find path of original file
    detailpath=os.path.abspath(originalfile)
    ## remove originalfile content, delimiter ###+++ and ###***
    start = "###***" + " " + detailpath
    end = "###+++" + " " + detailpath
    flag = True
    new_content_list = []
    for line in content_list:
        if (flag == True):
            new_content_list.append(line)
        if (start in line):
            flag = False
            new_content_list.remove(line)
        elif (end in line):
            flag = True
    ## append addfile content to original file
    f_append = open (appendfile,'r')
    replacement=f_append.read()
    f_append.close()
    new_content_list.append(start+'\n')
    new_content_list.append(replacement)
    new_content_list.append('\n'+end+'\n')
    f = open (originalfile,'w')
    f.writelines(new_content_list)
    f.close()
if __name__ == '__main__':

    originalfile = "hosts"
    appendfile = "hosts.append"
    hosts_append(originalfile, appendfile)