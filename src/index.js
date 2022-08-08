import "./style.css";
import "./assets/machine.jpg";

import mqtt from "precompiled-mqtt";
const options = {
  // Clean session
  clean: true,
  connectTimeout: 4000,
  reconnectPeriod: 0, // Disable automatic reconnection
  // Auth
  clientId: "frontend_test",
  username: "streamsheets",
  password: "vVIGFFZBne",
};
const mqttClient = mqtt.connect("ws://localhost:9001", options);
const topic = "cedalo/operator-hmi/machine";

// MQTT setup
mqttClient.on("connect", function () {
  console.log("Connected");
  document.getElementById("status-field").classList.remove("disconnected");
  document.getElementById("status-field").classList.add("connected");

  mqttClient.subscribe(topic, function (err) {
    if (!err) {
      console.log(`Subscribed to topic: ${topic}`);
      document.getElementById(
        "topic-field"
      ).innerHTML += `Subscribed to ${topic}`;
    }
  });
});

mqttClient.on("message", function (topic, message) {
  // const data = {
  //   "Machine Data": { Speed: 46, Power: 2007, Alarm: false },
  // };
  // Parse the MQTT message
  const response = JSON.parse(message.toString())["Machine Data"];
  //   console.log(response);
  // Update field values
  document.getElementById(
    "temp-field"
  ).innerText = `Temperature: ${response.temp} [°C]`;
  document.getElementById(
    "power-field"
  ).innerText = `Power: ${response.power} [W]`;
  // Check for alarms
  if (response.alarm) {
    document
      .getElementById("alarm-field")
      .classList.replace("alarm-deactive", "alarm-active");
  } else document.getElementById("alarm-field").classList.replace("alarm-active", "alarm-deactive");
});

// gRPC setup
const proxyPort = 8089;
const proxyUrl = `http://localhost:${proxyPort}`;

function sendgRPCRequest(type) {
  // Fetch data
  fetch(proxyUrl + `/?type=${type}`)
    .then((res) => res.json())
    .then((res) => {
      document.getElementById("grpc-response").innerHTML = res;
    });
}

document.getElementById("call-btn").addEventListener("click", () => {
  const field = document.getElementById("grpc-req-list");
  const requestType = field.value;
  sendgRPCRequest(requestType);
});
