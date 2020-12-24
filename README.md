# cidr

用于根据本地环境扫描并收集域所使用的CDN IP段，请使用该脚本的如扫描到新的IP可通过issues提交，以便供大家使用。
netflix_dm.txt 为已收集的域名及其子域，可自行修改，仅支持centos7_64。

收集到的IP会更新到netflix_ip里面

## 用法 
python cidr.py netflix_dm.txt

会生成后缀带_cidr的文件，里面就是其收集的IP段

## 提交issues格式

时间:
服务器所在地:
新增域:
扫描出的IP段:
