const express = require("express");
const cors = require("cors");
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const PROTO_PATH = "../grpc-server/schema.proto";
const app = express();

app.use(cors());

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});
const hello_proto = grpc.loadPackageDefinition(packageDefinition).teaming;

const client = new hello_proto.Greeter(
  "localhost:9090",
  grpc.credentials.createInsecure()
);

app.get("/", function (req, res) {
  //   console.log(req);
  const name = req.query.name;
  client.SayHello({ name: name }, function (err, response) {
    res.send(JSON.stringify(`${response.message}`));
  });
});

app.listen(3000, function () {
  console.log("Proxy: listening on port 3000");
});
