import { useState } from "react";
import { useRef } from "react";

import styles from "./main-style.module.scss";

const axios = require("axios").default;

const Main = () => {
	// selectedFile contains information on the currently picked file.
	// isFilePicked determines if a file has been picked or not.
	const [selectedFile, setSelectedFile] = useState();
	const [isFilePicked, setIsFilePicked] = useState(false);
	// const [hasInfo, setHasInfo] = useState(false);
	const [infoData, setInfoData] = useState({ Enter: "Food" });
	const inputFile = useRef(null);

	// Handle get the file name
	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsFilePicked(true);
	};

	const handleSubmission = () => {
		if (!isFilePicked) return;
		console.log(selectedFile);
		axios.post("http://localhost:5000/barcodeImage", selectedFile, {
			headers: {
				"Content-Type": selectedFile.type,
				"Access-Control-Allow-Origin": "*", //'http://localhost:5000/barcodeImage'
			},
		});
		setSelectedFile(null);
	};

	const onButtonClick = () => {
		inputFile.current.click();
	};

	console.log(Object.keys(infoData))
	console.log(typeof(Object.keys(infoData)))

	return (
		<div className={styles.container}>
			<div className={styles.buttonContainer}>
				<input type="file" onChange={changeHandler} ref={inputFile} style={{ display: "none" }} />
				<button className={styles.button} onClick={onButtonClick}>Upload Image</button>
				<button className={styles.button} onClick={handleSubmission}>Submit</button>
			</div>
			<Table className={styles.info} infoData={infoData} />
		</div>
	);
};

const Table = (infoData) => {
	return (
		<>
			<table>
				<thead>
					<th>Nutrition</th>
					<th>Info</th>
				</thead>
				<tbody>
					<tr>
						<td>Sugar</td>
						<td>3g</td>
					</tr>
					<tr>
						<td>Protein</td>
						<td>13g</td>
					</tr>
					<tr>
						<td>Carbs</td>
						<td>26g</td>
					</tr>
					<tr>
						<td>Fat</td>
						<td>5g</td>
					</tr>
				</tbody>
			</table>
		</>
	);
};

export default Main;
