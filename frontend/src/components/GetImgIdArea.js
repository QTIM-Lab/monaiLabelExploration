import React, { useState } from 'react';

const GetImgIdArea = (props) => {

  const handleClick = () => {
    // Define the URL and headers
    const url = 'http://0.0.0.0:8000/activelearning/first';
    const headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    };
  
    // Define the request body (data)
    const body = JSON.stringify({});
  
    // Send a POST request using the fetch API
    fetch(url, {
      method: 'POST',
      headers: headers,
      body: body,
    })
      .then(response => response.json())
      .then(data => {
        props.setData(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };



  return (
    <div>

    <button onClick={handleClick}>Get Image Id From Strategy</button>
      {props.imgIdData && (
        <div>
          Response:
          {JSON.stringify(props.imgIdData, null, 2)}
        </div>
      )}
    </div>
  );
}

export default GetImgIdArea;