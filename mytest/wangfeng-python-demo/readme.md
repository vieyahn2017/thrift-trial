# python thrift 服务端与客户端使用
// 出自 “IT民工--小枫” 博客， http://wangfeng7399.blog.51cto.com/3518031/1696108

# 一、简介
thrift是一个软件框架，用来进行可扩展且跨语言的服务的开发。它结合了功能强大的软件堆栈和代码生成引擎，以构建在 C++, Java, Python, PHP, Ruby, Erlang, Perl, Haskell, C#, Cocoa, JavaScript, Node.js, Smalltalk, and OCaml 这些编程语言间无缝结合的、高效的服务。

# 二、安装
1.下载地址    

2.安装
```bash
[root@localhost ~]# yum -y groupinstall "Development Tools"
[root@localhost ~]# yum -y install libevent-devel zlib-devel openssl-devel autoconf automake
[root@localhost ~]#  wget http://ftp.gnu.org/gnu/bison/bison-2.5.1.tar.gz 
[root@localhost ~]# tar xf bison-2.5.1.tar.gz
[root@localhost ~]# cd bison-2.5.1
[root@localhost ~]# ./configure --prefix=/usr
[root@localhost ~]# make
[root@localhost ~]# make install
[root@localhost ~]# tar xf thrift-0.9.2.tar.gz 
[root@localhost ~]# cd thrift-0.9.2
[root@localhost thrift-0.9.2]# ./configure -with-lua=no
```

3.安装python插件   
pip install thrift

# 三、准备服务器端
1.编辑接口文件 helloworld.thrift:
```cpp
service HelloWorld {
    string ping(),
    string say(1:string msg)
}
```

2.编辑 server.py
```python
# -*- coding:utf-8 -*-
#!/usr/bin/env python 
import socket
import sys
sys.path.append('./gen-py') 
from helloworld import HelloWorld 
from helloworld.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
class HelloWorldHandler:  
    def ping(self):   
        return "pong"   
    def say(self, msg):
        ret = "Received: " + msg    
        print ret    
        return ret
#创建服务端
handler = HelloWorldHandler()
processor = HelloWorld.Processor(handler)
#监听端口
transport = TSocket.TServerSocket("localhost", 9090)
#选择传输层
tfactory = TTransport.TBufferedTransportFactory()
#选择传输协议
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
#创建服务端 
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory) 
print "Starting thrift server in python..."
server.serve()
print "done!"

```
 
# 四、准备客户端
```python
# -*-coding:utf-8 -*-
#!/usr/bin/env python
 
import sys
sys.path.append('./gen-py')
 
from helloworld import HelloWorld #引入客户端类
 
from thrift import Thrift 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
 
try:
    #建立socket
    transport = TSocket.TSocket('localhost', 9090)
    #选择传输层，这块要和服务端的设置一致
    transport = TTransport.TBufferedTransport(transport)
    #选择传输协议，这个也要和服务端保持一致，否则无法通信
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    #创建客户端
    client = HelloWorld.Client(protocol)
    transport.open()
 
    print "client - ping"
    print "server - " + client.ping()
 
    print "client - say"
    msg = client.say("Hello!")
    print "server - " + msg
    #关闭传输
    transport.close()
except Thrift.TException, ex:
    print "%s" % (ex.message)

```


 
