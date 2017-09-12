#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:slots
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport


class Iface(object):
    def Janky(self, arg):
        """
        Parameters:
         - arg
        """
        pass

    def voidMethod(self):
        pass

    def primitiveMethod(self):
        pass

    def structMethod(self):
        pass

    def methodWithDefaultArgs(self, something):
        """
        Parameters:
         - something
        """
        pass

    def onewayMethod(self):
        pass

    def declaredExceptionMethod(self, shouldThrow):
        """
        Parameters:
         - shouldThrow
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def Janky(self, arg):
        """
        Parameters:
         - arg
        """
        self.send_Janky(arg)
        return self.recv_Janky()

    def send_Janky(self, arg):
        self._oprot.writeMessageBegin('Janky', TMessageType.CALL, self._seqid)
        args = Janky_args()
        args.arg = arg
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_Janky(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = Janky_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "Janky failed: unknown result")

    def voidMethod(self):
        self.send_voidMethod()
        self.recv_voidMethod()

    def send_voidMethod(self):
        self._oprot.writeMessageBegin('voidMethod', TMessageType.CALL, self._seqid)
        args = voidMethod_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_voidMethod(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = voidMethod_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def primitiveMethod(self):
        self.send_primitiveMethod()
        return self.recv_primitiveMethod()

    def send_primitiveMethod(self):
        self._oprot.writeMessageBegin('primitiveMethod', TMessageType.CALL, self._seqid)
        args = primitiveMethod_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_primitiveMethod(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = primitiveMethod_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "primitiveMethod failed: unknown result")

    def structMethod(self):
        self.send_structMethod()
        return self.recv_structMethod()

    def send_structMethod(self):
        self._oprot.writeMessageBegin('structMethod', TMessageType.CALL, self._seqid)
        args = structMethod_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_structMethod(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = structMethod_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "structMethod failed: unknown result")

    def methodWithDefaultArgs(self, something):
        """
        Parameters:
         - something
        """
        self.send_methodWithDefaultArgs(something)
        self.recv_methodWithDefaultArgs()

    def send_methodWithDefaultArgs(self, something):
        self._oprot.writeMessageBegin('methodWithDefaultArgs', TMessageType.CALL, self._seqid)
        args = methodWithDefaultArgs_args()
        args.something = something
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_methodWithDefaultArgs(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = methodWithDefaultArgs_result()
        result.read(iprot)
        iprot.readMessageEnd()
        return

    def onewayMethod(self):
        self.send_onewayMethod()

    def send_onewayMethod(self):
        self._oprot.writeMessageBegin('onewayMethod', TMessageType.ONEWAY, self._seqid)
        args = onewayMethod_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def declaredExceptionMethod(self, shouldThrow):
        """
        Parameters:
         - shouldThrow
        """
        self.send_declaredExceptionMethod(shouldThrow)
        return self.recv_declaredExceptionMethod()

    def send_declaredExceptionMethod(self, shouldThrow):
        self._oprot.writeMessageBegin('declaredExceptionMethod', TMessageType.CALL, self._seqid)
        args = declaredExceptionMethod_args()
        args.shouldThrow = shouldThrow
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_declaredExceptionMethod(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = declaredExceptionMethod_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.xwamap is not None:
            raise result.xwamap
        raise TApplicationException(TApplicationException.MISSING_RESULT, "declaredExceptionMethod failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["Janky"] = Processor.process_Janky
        self._processMap["voidMethod"] = Processor.process_voidMethod
        self._processMap["primitiveMethod"] = Processor.process_primitiveMethod
        self._processMap["structMethod"] = Processor.process_structMethod
        self._processMap["methodWithDefaultArgs"] = Processor.process_methodWithDefaultArgs
        self._processMap["onewayMethod"] = Processor.process_onewayMethod
        self._processMap["declaredExceptionMethod"] = Processor.process_declaredExceptionMethod

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_Janky(self, seqid, iprot, oprot):
        args = Janky_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Janky_result()
        try:
            result.success = self._handler.Janky(args.arg)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("Janky", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_voidMethod(self, seqid, iprot, oprot):
        args = voidMethod_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = voidMethod_result()
        try:
            self._handler.voidMethod()
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("voidMethod", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_primitiveMethod(self, seqid, iprot, oprot):
        args = primitiveMethod_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = primitiveMethod_result()
        try:
            result.success = self._handler.primitiveMethod()
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("primitiveMethod", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_structMethod(self, seqid, iprot, oprot):
        args = structMethod_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = structMethod_result()
        try:
            result.success = self._handler.structMethod()
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("structMethod", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_methodWithDefaultArgs(self, seqid, iprot, oprot):
        args = methodWithDefaultArgs_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = methodWithDefaultArgs_result()
        try:
            self._handler.methodWithDefaultArgs(args.something)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("methodWithDefaultArgs", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_onewayMethod(self, seqid, iprot, oprot):
        args = onewayMethod_args()
        args.read(iprot)
        iprot.readMessageEnd()
        try:
            self._handler.onewayMethod()
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except:
            pass

    def process_declaredExceptionMethod(self, seqid, iprot, oprot):
        args = declaredExceptionMethod_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = declaredExceptionMethod_result()
        try:
            result.success = self._handler.declaredExceptionMethod(args.shouldThrow)
            msg_type = TMessageType.REPLY
        except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
            raise
        except ExceptionWithAMap as xwamap:
            msg_type = TMessageType.REPLY
            result.xwamap = xwamap
        except Exception as ex:
            msg_type = TMessageType.EXCEPTION
            logging.exception(ex)
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("declaredExceptionMethod", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class Janky_args(object):
    """
    Attributes:
     - arg
    """

    __slots__ = (
        'arg',
    )

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'arg', None, None, ),  # 1
    )

    def __init__(self, arg=None,):
        self.arg = arg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.arg = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Janky_args')
        if self.arg is not None:
            oprot.writeFieldBegin('arg', TType.I32, 1)
            oprot.writeI32(self.arg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class Janky_result(object):
    """
    Attributes:
     - success
    """

    __slots__ = (
        'success',
    )

    thrift_spec = (
        (0, TType.I32, 'success', None, None, ),  # 0
    )

    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Janky_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class voidMethod_args(object):

    __slots__ = (
    )

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('voidMethod_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class voidMethod_result(object):

    __slots__ = (
    )

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('voidMethod_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class primitiveMethod_args(object):

    __slots__ = (
    )

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('primitiveMethod_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class primitiveMethod_result(object):
    """
    Attributes:
     - success
    """

    __slots__ = (
        'success',
    )

    thrift_spec = (
        (0, TType.I32, 'success', None, None, ),  # 0
    )

    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('primitiveMethod_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class structMethod_args(object):

    __slots__ = (
    )

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('structMethod_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class structMethod_result(object):
    """
    Attributes:
     - success
    """

    __slots__ = (
        'success',
    )

    thrift_spec = (
        (0, TType.STRUCT, 'success', (CompactProtoTestStruct, CompactProtoTestStruct.thrift_spec), None, ),  # 0
    )

    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = CompactProtoTestStruct()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('structMethod_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class methodWithDefaultArgs_args(object):
    """
    Attributes:
     - something
    """

    __slots__ = (
        'something',
    )

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'something', None, 2, ),  # 1
    )

    def __init__(self, something=thrift_spec[1][4],):
        self.something = something

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.something = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('methodWithDefaultArgs_args')
        if self.something is not None:
            oprot.writeFieldBegin('something', TType.I32, 1)
            oprot.writeI32(self.something)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class methodWithDefaultArgs_result(object):

    __slots__ = (
    )

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('methodWithDefaultArgs_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class onewayMethod_args(object):

    __slots__ = (
    )

    thrift_spec = (
    )

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('onewayMethod_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class declaredExceptionMethod_args(object):
    """
    Attributes:
     - shouldThrow
    """

    __slots__ = (
        'shouldThrow',
    )

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'shouldThrow', None, None, ),  # 1
    )

    def __init__(self, shouldThrow=None,):
        self.shouldThrow = shouldThrow

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.shouldThrow = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('declaredExceptionMethod_args')
        if self.shouldThrow is not None:
            oprot.writeFieldBegin('shouldThrow', TType.BOOL, 1)
            oprot.writeBool(self.shouldThrow)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


class declaredExceptionMethod_result(object):
    """
    Attributes:
     - success
     - xwamap
    """

    __slots__ = (
        'success',
        'xwamap',
    )

    thrift_spec = (
        (0, TType.BOOL, 'success', None, None, ),  # 0
        (1, TType.STRUCT, 'xwamap', (ExceptionWithAMap, ExceptionWithAMap.thrift_spec), None, ),  # 1
    )

    def __init__(self, success=None, xwamap=None,):
        self.success = success
        self.xwamap = xwamap

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.xwamap = ExceptionWithAMap()
                    self.xwamap.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('declaredExceptionMethod_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        if self.xwamap is not None:
            oprot.writeFieldBegin('xwamap', TType.STRUCT, 1)
            self.xwamap.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, getattr(self, key))
             for key in self.__slots__]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)
