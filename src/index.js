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
const client = mqtt.connect("ws://localhost:9001", options);
const topic = "cedalo/operator-hmi/machine";
client.on("connect", function () {
  console.log("Connected");
  document.getElementById("status-field").classList.remove("disconnected");
  document.getElementById("status-field").classList.add("connected");

  client.subscribe(topic, function (err) {
    if (!err) {
      console.log(`Subscribed to topic: ${topic}`);
      document.getElementById(
        "topic-field"
      ).innerHTML += `Subscribed to ${topic}`;
    }
  });
});

client.on("message", function (topic, message) {
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

/*
function sendRequest() {
  const field = document.getElementById("inputTxt");
  const name = field.value;
  field.value = "";

  // Fetch data
  const url = "http://localhost:3000";

  fetch(url + `/?name=${name}`)
    .then((res) => res.json())
    .then((res) => {
      const elem = document.createElement("p");
      elem.innerHTML = res;
      document.getElementById("container").appendChild(elem);
    });
}
*/
