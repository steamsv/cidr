# cidr

用于根据本地环境扫描并收集域所使用的CDN IP段，请使用该脚本的如扫描到新的IP可通过issues提交，以便供大家使用。
netflix_dm.txt 为已收集的域名及其子域，可自行修改，仅支持centos7_64。

收集到的IP会更新到netflix_ip里面

## 子域收集

可通过客户端及服务端日志查看具体访问子域

## 用法 

python cidr.py netflix_dm.txt

会生成后缀带_cidr的文件，里面就是其收集的IP段,建议多次扫描，每次扫描的结果保存。

备注:如执行后没有收集到，则删除netflix_dm.txt，用vi命令新建文本，并复制netflix_dm.txt内容粘贴进去即可，然后重新执行

## 提交issues格式

时间:

服务器所在地:

新增域:

扫描出的IP段:
