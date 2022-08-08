const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const PROTO_PATH = "./schema.proto";
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});
const hello_proto = grpc.loadPackageDefinition(packageDefinition).teaming;

/**
 * Implements the SayHello RPC method.
 */
function sayHello(call, callback) {
  callback(null, { message: "Hello " + call.request.name });
}

/**
 * Starts an RPC server that receives requests for the Greeter service at the
 * sample server port
 */
function main() {
  const server = new grpc.Server();
  server.addService(hello_proto.Greeter.service, {
    sayHello: sayHello,
  });
  server.bindAsync(
    "0.0.0.0:9090",
    grpc.ServerCredentials.createInsecure(),
    () => {
      server.start();
    }
  );
}

main();
