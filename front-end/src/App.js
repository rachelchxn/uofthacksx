import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [link, setLink] = useState('');
  const [data, setData] = useState({'class_notes': '', 'keywords': ''})
  
  useEffect(() => {
    }, [data])
  
  const handleChange = (e) =>{
    setLink(e.target.value);
  }
  
  const handleClick = async (e) => {
    e.preventDefault()
    console.log('http://127.0.0.1:8000/downloadyoutube/?link=' + link);
    const res = await fetch ('http://127.0.0.1:8000/downloadyoutube/?link=' + link);
    const dat = await res.json();
    setData(dat);
  
  }

  return (
    <div className="App">
      <head>
        <meta name = 'viewport' content = 'with = device-width' initial-scale = '1.0'></meta>
        <link rel = "stylesheet" href = "App.css"></link>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"></link>
        <link rel="preconnect" href="https://fonts.googleapis.com"></link>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin></link>
<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@200&display=swap" rel="stylesheet"></link>
      </head>
  
      <section class = 'header'>
          <div class = 'title1'>Too Long;</div>
          <div class = 'title2'>Didn't Watch...</div>
          <div class = 'subtitle'>Fully Developed by Jonathan Chen</div>
          <div class = 'rectangle1'></div>
          <div class = 'rectangle2'></div>
          <nav>
            <div class = 'logo-img'>
              <u1>  
                <a href = "index.html"><img src = ""></img></a>
              </u1>
            </div>
            <div class = 'logo'>
              <ul>
                <li><a href = '/'>TL;DW</a></li>
              </ul>
            </div>
            <div class = 'nav-bar'>
              <ul>
                <li><a href = '/'>Home</a></li>
                <li><a href = '#application'>Application</a></li>
                <li><a href = '#process'>Process</a></li>
                {/* <li><a href = '/'>Contact</a></li> */}
              </ul>
            </div>
          </nav>

          <div class='wrapper'>

          <form onSubmit={handleClick} action = "./" method = ''>
            <section class = 'input-output'>
              <div class = "search-bar">
                <h1 class ='upload'>Copy and Paste Link Here</h1>
                <div class='input-wrapper'>
                  <input value={link} onChange={handleChange} type="text" id = "link-input" class="search-bar-input" name="upload" placeholder="Past Youtube link here"></input>
                  <button type = 'submit' class = 'search-bar-button'>
                    <i class = "material-icons">upload</i>
                  </button>
                </div>
              </div>
              <div class = "output">
                <h1 class = 'notes'>TL;DW</h1>
                <textarea type = 'textarea' rows='18' id = 'output-text' class = 'output-bar' name = 'output1' placeholder  = "Converted notes..." value={data["class_notes"]} />
              </div>
            </section>
          </form>

          </div>
          
      </section>

        <section id = 'application' class = 'info-container'>
            <section class = 'application-title'>
              Real World Application
            </section>
            <section class = 'application-paragraph'>
              This program allows for educational videos/lectures to be converted into notes. Students will be able to save time!!!!!!!
            </section>
        </section>
        <section id = 'process' class = 'info-container'>
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
