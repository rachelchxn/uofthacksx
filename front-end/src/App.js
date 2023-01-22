import './App.css';
import { useState, useEffect } from 'react';
import Logo from './imgs/logo.png'
import PDF from './imgs/tldw.pdf'

function App() {
  const [link, setLink] = useState('');
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState({'class_notes': '', 'keywords': ''})
  
  useEffect(() => {
    }, [data])
  
  const handleChange = (e) =>{
    setLink(e.target.value);
  }
  
  const handleClick = async (e) => {
    e.preventDefault()
    setLoading(true)
    console.log('http://127.0.0.1:8000/downloadyoutube/?link=' + link);
    const res = await fetch ('http://127.0.0.1:8000/downloadyoutube/?link=' + link);
    const dat = await res.json();
    setData(dat);
    setLoading(false)
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
          <nav>
            <div class = 'logo'>
              <ul>
                <li><a href = '/'><img className='logo' src={Logo} /></a></li>
              </ul>
            </div>
            <div class = 'nav-bar'>
              <ul>
                <li><a href = '/'>Home</a></li>
                <li><a href = '#application'>Application</a></li>
                <li><a href = '#process'>Process</a></li>
              </ul>
            </div>
          </nav>

          <div class='wrapper'>

          <div className='stupid'>
            <div class = 'title1'>Too Long;</div>
            <div class = 'title2'>Didn't Watch...</div>
            <div class = 'subtitle'>Learn Smarter, Not Harder.</div>
          </div>

          <section class = 'input-output'>
            <form onSubmit={handleClick} action = "./" method = ''>
            <div class = "search-bar">
                  <h1 class ='upload'>Copy and Paste Link Here</h1>
                  <div class='input-wrapper'>
                    <input value={link} onChange={handleChange} type="text" id = "link-input" class="search-bar-input" name="upload" placeholder="Past Youtube link here"></input>
                    <button type = 'submit' class = 'search-bar-button'>
                      <i class = "material-icons">upload</i>
                    </button>
                  </div>
                </div>
            </form>

              <div class = "output">
                <h1 class = 'notes'>TL;DW</h1>
                <textarea type = 'textarea' rows='12' id = 'output-text' class = 'output-bar' name = 'output1' placeholder  = "Converted notes..." value={data["class_notes"]+'\n'+data['keywords']} />
              </div>
              <a href={PDF} download='tldw.pdf'><button className='button' >Download TL;DW as pdf</button></a>
          </section>

          </div>
          
      </section>

        <section id = 'application' class = 'info-container'>
            <section class = 'application-title'>
              Real World Application
            </section>
            <section class = 'application-paragraph'>
              TLDW - Too Long; Didn't Watch is a simple and convenient web application that turns Youtube and user-uploaded videos into organized notes. It saves you time by turning long-form educational content into organized and digestible text so you can learn smarter, not harder.
            </section>
        </section>
        <section id = 'process' class = 'info-container'>
            <section class = 'process-paragraph'>
              First, our program either takes in a youtube link and converts it into an MP3 file or prompts the user to upload their own MP3 file. The audio file is then transcribed with Assembly AI's transcription API. The text transcription is then fed into Co:here's Generate, then Classify, then Generate again summarize the text, organize by type of point (main concept, point, example, definition), and extract keywords. The Python backend built with Django is connected to a ReactJS frontend for an optimal user experience.
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
