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
const machine_proto = grpc.loadPackageDefinition(packageDefinition).teaming;

function getRandomBetween(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

/**
 * Implements the CurrentTask RPC method.
 */
function getCurrentTask(call, callback) {
  const currentTask = getRandomBetween(1, 11);
  callback(null, { message: `Task ${currentTask}` });
}
/**
 * Implements the RisksFactor RPC method.
 */
function getRisksFactor(call, callback) {
  const risksFactor = getRandomBetween(5, 100);
  callback(null, { message: risksFactor });
}
/**
 * Implements the HumanIntervention RPC method.
 */
function checkHumanIntervention(call, callback) {
  const intervention = Math.random() < 0.5;
  callback(null, { message: intervention });
}

/**
 * Starts an RPC server that receives requests for the Greeter service at the
 * sample server port
 */
function main() {
  const server = new grpc.Server();
  server.addService(machine_proto.Machine.service, {
    CurrentTask: getCurrentTask,
    RisksFactor: getRisksFactor,
    HumanIntervention: checkHumanIntervention,
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
