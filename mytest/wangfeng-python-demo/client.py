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
