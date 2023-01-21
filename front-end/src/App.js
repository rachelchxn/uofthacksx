import './App.css';
import { useState } from 'react';

function App() {
  const [link, setLink] = useState('');
  const handleChange = (e) =>{
    setLink(e.target.value);
  }
  const handleClick = async (e) => {
    console.log('http://127.0.0.1:8000/downloadyoutube/?link=' + link);
    const res = await fetch ('http://127.0.0.1:8000/downloadyoutube/?link=' + link);
    await res.json();
  }
  return (
    <div className="App">
      <head>
        <meta name = 'viewport' content = 'with = device-width' initial-scale = '1.0'></meta>
        <link rel = "stylesheet" href = "App.css"></link>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"></link>
        <link rel="preconnect" href="https://fonts.googleapis.com"></link>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin></link>
        <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300&display=swap" rel="stylesheet"></link>
      </head>
  
      <section class = 'header'>
          <nav>
            <div class = 'logo-img'>
              <u1>
                <a href = "index.html"><img src = ""></img></a>
              </u1>
            </div>
            <div class = 'nav-bar'>
              <ul>
                <li><a href = ''>HOME</a></li>
                <li><a href = ''>APPLICATION</a></li>
                <li><a href = ''>PROCESS</a></li>
                <li><a href = ''>CONTACT</a></li>
              </ul>
            </div>
          </nav>
          <h1 class ='upload'>Video Upload</h1>
          <form action = "./" method = ''>
            <div class = "search-bar">
              <input value={link} onChange={handleChange}type="text" id = "link-input" class="search-bar-input" name="upload" placeholder="Upload Files"></input>
              <button onClick={handleClick} type = 'button' class = 'search-bar-button  '>
                <i class = "material-icons">upload</i>
              </button>
            </div>
          </form>
      </section>
      <section class = 'nav-application'>
          <section class = 'application-title'>
            Real World Application
          </section>
          <section class = 'application-paragraph'>
            This program allows for educational videos/lectures to be converted into notes. This allows students to be able to save time when writing down information. 
          </section>
      </section>
      <section class = 'nav-process'>
          <section class = 'process-paragraph'>
            THE INFORMATION IS FED THROUGH COHERE AND THEN BOOM BAM NOTES!!!
          </section>
          <section class = 'process-title'>
            The Process
          </section>
      </section>
      <section class = 'our-team'>
        <section class = 'team-title'>
          
        </section>
      </section>
    </div>
  );
}

export default App;
