const express = require("express");
const cors = require("cors");
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const PROTO_PATH = "./schema.proto";
const app = express();
const port = 8089;

app.use(cors());

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});
const machine_proto = grpc.loadPackageDefinition(packageDefinition).teaming;

const client = new machine_proto.Machine(
  "grpc-server:9090",
  grpc.credentials.createInsecure()
);

app.get("/", function (req, res) {
  // const name = req.query.type;

  switch (req.query.type) {
    case "task":
      client.CurrentTask({}, function (err, response) {
        res.send(JSON.stringify(`${response.message}`));
      });
      break;
    case "ergonomic":
      client.RisksFactor({}, function (err, response) {
        res.send(JSON.stringify(`${response.message}`));
      });
      break;
    case "intervention":
      client.HumanIntervention({}, function (err, response) {
        res.send(JSON.stringify(`${response.message}`));
      });
      break;
  }
});

app.listen(port, function () {
  console.log(`Proxy: listening on port ${port}`);
});
