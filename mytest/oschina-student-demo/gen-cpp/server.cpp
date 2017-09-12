#include <concurrency/ThreadManager.h> //zml
#include <concurrency/PosixThreadFactory.h> //zml
#include "Serv.h"
#include <protocol/TBinaryProtocol.h>
#include <server/TSimpleServer.h>
#include <transport/TServerSocket.h>
#include <transport/TBufferTransports.h>
#include <server/TNonblockingServer.h> //zml    
using namespace ::apache::thrift;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace ::apache::thrift::server;    
using namespace::apache::thrift::concurrency; //zml        
using boost::shared_ptr;	

#define THREAD_NUM 2
const int g_port = 9090;
class ServHandler : virtual public ServIf {
 public:
  ServHandler() {
	// Your initialization goes here
  }
  int32_t put(const Student& s) {
	// Your implementation goes here
	printf("put student.sno=%d\n", s.sno);
	return s.sno;
  }
};

int thrift_server_run()
{
	//创建thrift server
	shared_ptr<ServHandler> handler(new ServHandler());
	shared_ptr<TProcessor> processor(new ServProcessor(handler));
	shared_ptr<TProtocolFactory> protocolFactory(new TBinaryProtocolFactory());
	
	shared_ptr<ThreadManager> threadManager = ThreadManager::newSimpleThreadManager(THREAD_NUM);
	shared_ptr<PosixThreadFactory> threadFactory = shared_ptr<PosixThreadFactory> (new PosixThreadFactory()); //PosixThreadFactory可以自定义（继承于ThreadFactory）
	threadManager->threadFactory(threadFactory);
	threadManager->start();		
	TNonblockingServer server(processor, protocolFactory, g_port, threadManager);
	try {
		server.serve();
	}
	catch(TException e) {
		printf("Server.serve() failed\n");
		exit(-1);
	}
	return 0;
}

int main(int argc, char **argv) {
	thrift_server_run();
	while(1) {
		sleep(10);
	}
	return 0;
}
