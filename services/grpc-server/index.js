const express = require("express");

const app = express();

// Setup basic GET request
app.get("/", (req, res) => {
  res.send("<h2> Hi there!!! </h2>");
});

// Use the Env variable PORT or, in case, the 3000 port
const port = 8089;

app.listen(port, () => console.log(`Listening on port ${port}`));
