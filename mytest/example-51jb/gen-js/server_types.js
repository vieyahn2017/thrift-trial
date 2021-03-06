//
// Autogenerated by Thrift Compiler (0.10.0)
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//


message = function(args) {
  this.seqId = null;
  this.content = null;
  if (args) {
    if (args.seqId !== undefined && args.seqId !== null) {
      this.seqId = args.seqId;
    }
    if (args.content !== undefined && args.content !== null) {
      this.content = args.content;
    }
  }
};
message.prototype = {};
message.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.I32) {
        this.seqId = input.readI32().value;
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRING) {
        this.content = input.readString().value;
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

message.prototype.write = function(output) {
  output.writeStructBegin('message');
  if (this.seqId !== null && this.seqId !== undefined) {
    output.writeFieldBegin('seqId', Thrift.Type.I32, 1);
    output.writeI32(this.seqId);
    output.writeFieldEnd();
  }
  if (this.content !== null && this.content !== undefined) {
    output.writeFieldBegin('content', Thrift.Type.STRING, 2);
    output.writeString(this.content);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

