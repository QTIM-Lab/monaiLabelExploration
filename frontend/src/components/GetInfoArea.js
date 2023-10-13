import React, { useState } from 'react';

const GetInfoArea = () => {

  const [responseData, setResponseData] = useState(null);

  const handleClick = () => {
    // Define the URL and headers
    const url = 'http://0.0.0.0:8000/info/';
    const headers = {
      'Accept': 'application/json',
    };

    // Send a GET request using the fetch API
    fetch(url, {
      method: 'GET',
      headers: headers,
    })
      .then(response => response.json())
      .then(data => {
        setResponseData(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };



  return (
    <div>

    <button onClick={handleClick}>Get App Info</button>
      {responseData && (
        <div>
          Response:
          {JSON.stringify(responseData, null, 2)}
        </div>
      )}
    </div>
  );
}

export default GetInfoArea;