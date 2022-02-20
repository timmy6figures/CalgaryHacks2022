const express = require("express");
const db = require("./db");
const cors = require("cors");
const app = express();

const PORT = 3001;

app.use(express.json());

app.use(
  cors({
    origin: ["http://localhost:3000"],
    methods: ["GET", "POST", "PUT"],
  })
);
// app.use(function (req, res, next) {
//   // res.header("Access-Control-Allow-Origin", "http://localhost:3000"); // update to match the domain you will make the request from
//   // res.header(
//   //   "Access-Control-Allow-Headers",
//   //   "Origin, X-Requested-With, Content-Type, Accept"
//   // );
//   next();
// });

app.get("/", (request, response) => {
  response.status(200).send("<h1> Home Page </h1>");
});
app.post("/person", async (request, response) => {
  try {
    const { firstName, lastName } = request.body;
    const dbResponse = await db.query(
      "INSERT INTO person (first_name, last_name) VALUES($1, $2) returning *",
      [firstName, lastName]
    );
    response.status(200).send(dbResponse);
  } catch (error) {
    response.status(404).send(error);
  }
});

app.get("/person", async (request, response) => {
  try {
    const dbResponse = await db.query("SELECT * FROM person");
    response.status(201).send(dbResponse);
  } catch (error) {
    console.log(error);
  }
});

app.put("/person/:id", async (request, response) => {
  try {
    const dbResponse = await db.query(
      "DELETE FROM person WHERE id=$1 returning *",
      [request.params.id]
    );
    // console.log(request.params.id);
    response.status(201).json(dbResponse);
  } catch (error) {
    console.log(error);
  }
});

app.listen(PORT, () => {
  console.log(`Listening on Port: ${PORT}`);
});
