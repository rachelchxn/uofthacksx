import './App.css';

function App() {
  return (
    <div className="App">
      <head>
        <meta name = 'viewport' content = 'with = device-width' initial-scale = '1.0'></meta>
        <link rel = "stylesheet" href = "App.css"></link>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"></link>
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
                <li><a href = ''>TEAM</a></li>
                <li><a href = ''>APPLICATION</a></li>
                <li><a href = ''>PROCESS</a></li>
                <li><a href = ''>CONTACT</a></li>
              </ul>
            </div>
          </nav>
          <h1 class ='upload'>Video Upload</h1>
          //need method
          <form action = "./" method = ''>
            <div class = "search-bar">
              <input type = 'text' class = 'search-bar-input' name = 'search' placeholder = 'Upload mp3/wav File'></input>
             
              <button type = 'submit' class = 'search-bar-button'>
                <i class = "material-icons">upload</i>
              </button>
            </div>
            <div class = "text-box">
              
              <p class = 'output' id = 'output1'></p>
            </div>
          </form>
      </section>
      <section class = 'nav-team'>
        <h1>

        </h1>
      </section>
    </div>
  );
}

export default App;
