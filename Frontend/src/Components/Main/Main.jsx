import { useState } from "react";
import { useRef } from "react";

const axios = require('axios').default

const Main = () => {
  // selectedFile contains information on the currently picked file.
  // isFilePicked determines if a file has been picked or not.
  const [selectedFile, setSelectedFile] = useState();
  const [isFilePicked, setIsFilePicked] = useState(false);
  const inputFile = useRef(null);

  // Handle get the file name
  const changeHandler = (event) => {
    setSelectedFile(event.target.files[0]);
    setIsFilePicked(true);
  };
  
  const handleSubmission = () => {
    if(!isFilePicked) return;
    console.log(selectedFile);
    var headers1 = {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': 'true'
      //'http://localhost:5000/barcodeImage'
    }
    axios.post("http://localhost:5000/barcodeImage", selectedFile, {
      headers: headers1
    });
    setSelectedFile(null);
  };

  const onButtonClick = () => {
    inputFile.current.click();
  };

  return (
    <div>
      <input
        type="file"
        onChange={changeHandler}
        ref={inputFile}
        style={{ display: "none" }}
      />
      <button onClick={onButtonClick}>Select file</button>
      <div>
        <button onClick={handleSubmission}>Submit</button>
      </div>
    </div>
  );
};

export default Main;
