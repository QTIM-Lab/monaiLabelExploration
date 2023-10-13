import React, { useState } from 'react';

import GetImgIdArea from './GetImgIdArea';
import GetInfoArea from './GetInfoArea';
import DisplayImgArea from './DisplayImgArea';

// import logo from './logo.svg';
import '../App.css';

const MainContent = () => {

    const [imgIdData, setImgIdData] = useState(null);

  return (
    <div className="App">

        <GetInfoArea />
        <GetImgIdArea setData={setImgIdData} imgIdData={imgIdData} />
        <DisplayImgArea imgId={imgIdData?.id} />

    </div>
  );
}

export default MainContent;


