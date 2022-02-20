const axios = require('axios').default
import FormData from 'form-data';

const sendImage = (imageFile) => {
    axios.post("http://localhost:5000/barcodeImage", imageFile, {
        headers: {'Content-Type':imageFile.type}
    });
};

module.exports = sendImage;