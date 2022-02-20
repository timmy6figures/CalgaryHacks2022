import fetch from 'node-fetch';
// const fetch = require('node-fetch');

const flaskURL = "";

const readInfo = async (image) => {
    const response = await fetch(flaskURL, 
        {
            method: 'post',
            mode: 'cors',
            body: JSON.stringify(image), 
            headers: {'Content-Type':'application/json'}
        }
    );
    const data = await response.json();
    return data;
};

module.exports = readInfo;