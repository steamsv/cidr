#!/usr/bin/env python
#coding: utf-8

import os, sys, commands, urllib2, json

# 是否输出运营商isp
isp = False

if len(sys.argv) != 2:
    print "python cidr.py 域名文件"
    exit()

if os.path.exists(sys.argv[1]):
    with open(sys.argv[1]) as file:
        fileStr = file.read()
else:
    print "文件不存在"
    exit()

output = commands.getoutput("dig")
if "command not found" in output:
    print "正在安装dig命令, 如果报错请手动执行 yum install -y bind-utils"
    commands.getoutput("yum install -y bind-utils")
output = commands.getoutput("whois")
if "command not found" in output:
    print "正在安装whois命令, 如果报错请手动执行 yum install -y whois"
    commands.getoutput("yum install -y whois")

domainArray = fileStr.split("\n")
cidrArray = []
for domain in domainArray:
    if domain.startswith("//") or domain == "":
        cidrArray.append(domain)
        continue
    output = commands.getoutput("dig +short " + domain)
    ipArray = output.split("\n")
    for index, ip in enumerate(ipArray):
        if ip == "":
            continue
        if "connection timed out" in ip:
            continue
        if index == 0 and isp:
            response = urllib2.urlopen("http://ip-api.com/json/" + ip)
            html = response.read()
            if html != "" and "fail" not in html:
                dict = json.loads(html)
                if dict["isp"] != "":
                    cidrArray.append("// " + dict["isp"].encode('ascii', 'ignore'))
        print "正在扫描: " + domain + " " + ip
        output = commands.getoutput("whois " + ip + "|grep CIDR")
        if output == "":
            output = commands.getoutput("whois " + ip + "|grep route:")
        print output
        array = output.split("\n")
        for str1 in array:
            if str1.startswith("CIDR:") or str1.startswith("route:"):
                str1 = str1.replace(" ", "")
                str1 = str1.replace("CIDR:", "")
                str1 = str1.replace("route:", "")
                if "," in str1:
                    array1 = str1.split(",")
                    for str2 in array1:
                        if str2 not in cidrArray:
                            cidrArray.append(str2)
                else:
                    if str1 not in cidrArray:
                        cidrArray.append(str1)
output = ""         
for str3 in cidrArray:
    output = output + str3 + "\n"
with open(sys.argv[1] + "_cidr", "w") as text_file:
    text_file.write(output)
