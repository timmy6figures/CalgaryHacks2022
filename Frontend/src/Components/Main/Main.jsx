import { useState } from "react";
import { useRef } from "react";
const Main = () => {
  // selectedFile contains information on the currently picked file.
  // isFilePicked determines if a file has been picked or not.
  const [selectedFile, setSelectedFile] = useState();
  const [isFilePicked, setIsFilePicked] = useState(false);
  const inputFile = useRef(null);

  // Handle get the file name
  const changeHandler = (event) => {
    console.log("Called");
    setSelectedFile(event.target.files[0]);
    setIsFilePicked(true);
  };

  const handleSubmission = () => {
    console.log(selectedFile);
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
