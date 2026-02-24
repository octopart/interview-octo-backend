import express from "express";
import { partOffers } from "#utils/jsondata.js";

const app = express();
const port = "3000";

app.get("/health", (req, res) => {
  res.send("OK");
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
