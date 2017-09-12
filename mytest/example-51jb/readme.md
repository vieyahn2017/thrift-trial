# Thrift的安装方法和简单实例

// http://www.jb51.net/article/100567.htm



./configure   
make   
make install   

提示找不到相关库
cd /usr/local/lib   
执行ldconfig


# Thrift的简单示例 

首先创建Thrift的语法规则文件，命名为server.thrift，内容如下：
 
```cpp
struct message  
{  
  1:i32 seqId,  
  2:string content  
}  
   
service serDemo  
{  
  void put(1:message msg)  
}
 
```

在shell下面执行执行：   
 
thrift -gen cpp server.thrift     

该语句用于创建c++服务框架，创建成功后会在该目录下生成gen-cpp文件夹，然后修改该目录下的serDemo_server.skeleton.cpp，在put函数中添加如下代码：

```cpp

class serDemoHandler : virtual public serDemoIf {  
 public:  
 serDemoHandler() {  
  // Your initialization goes here  
 }  
   
 void put(const message& msg) {  
  // Your implementation goes here  
  printf("receive message: id: %d, content: %s\n", msg.seqId, msg.content.c_str());  
 }
 
```
然后进行编译就可以了: g++ -o server *.cpp -lthrift   

上面是server框架的代码，对于client的框架其实已经创建，但是现在需要添加client执行代码，可以在该目录下创建client.cpp，然后输入以下内容，下面的内容可以作为SimpleServer的client的模板，只需修改注释的部分。

```cpp

// -------------------------替换成对应service名字的.h 文件------------------------  
#include "serDemo.h"   
//------------------------------------------------------------------------------  
#include <transport/TSocket.h>   
#include <transport/TBufferTransports.h>   
#include <protocol/TBinaryProtocol.h>   
    
using namespace apache::thrift;   
using namespace apache::thrift::protocol;   
using namespace apache::thrift::transport;   
    
using boost::shared_ptr;   
    
int main(int argc, char **argv) {   
  boost::shared_ptr<TSocket> socket(new TSocket("localhost", 9090));   
  boost::shared_ptr<TTransport> transport(new TBufferedTransport(socket));   
  boost::shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));   
    
  transport->open();   
    
  // ----------------------------我们的代码写在这里------------------------------
  serDemoClient client(protocol);  
  message msg;  
  msg.seqId = 1;  
  msg.content = "client message";    
  client.put(msg);  
  //--------------------------------------------------------------------------  
   
  transport->close();   
    
  return 0;   
}

```

然后进行编译：g++ -o client *[^n].cpp - lthrift，   
也可以将serDemo_server.skeleton.cpp移动到其它目录，   
使用g++ -o client *.cpp - lthrift命令。

然后就可以执行了，启动server后，启动client，server执行如下：   

./server

输出：     
put   
receive message: id: 1, content: client message
