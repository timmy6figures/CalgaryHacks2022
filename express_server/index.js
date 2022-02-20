const express = require("express");
const path = require("path");
const ExpressError = require("./utils/ExpressError");
const catchAsync = require("./utils/catchAsync");
const readInfo = require('./data/flaskConnect');

const app = express();
app.use(express.urlencoded({ extended: true }));

// home page
app.get('/', (req, res) => {
    res.send('hello world');
});

// a user can post an image to this url
app.post(
    '/image',
    catchAsync(async(req, res) => {
        if(!req.body.image) throw new ExpressError("No image passed or image was invalid!", 400);
        const image = req.body.image;
        const data = await readInfo(image);
        console.log(data);
        res.status(200).send('works');
    })
);

app.all("*", (req, res, next) => {
	next(new ExpressError("Page Not Found", 404));
});

app.use((err, req, res, next) => {
	const { statusCode = 500 } = err;
	if (!err.message) err.message = "Something went wrong!";
	res.status(statusCode).render("error", { err });
});

app.listen(3000, () => {
	console.log("serving on port 3000");
});