const app = require("express")();

app.get("/", (req, res) => {
    res.json("ok");
});

app.listen(5000)