import React,  {useState, useEffect } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

function app() {
  const [data, setData] = userState(null);
  const [loading, setLoading] = useState(null);
  const [error, seterror] = useState(null);

  useInsertionEffect(() => {
    axios.get('http://localhost:8080/transacoes/')                                              //aqui e para adicionar todas as rotas que eu quero no front end
      .then(response => {
        setData(response.data);
        setLoading(false);
      })
      .catch(error => {
        seterror(error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error loading data!</p>

  return (
    <div className="App">
      <header className="App-header">
        <img src ={logo} className="App-logo" alt="logo" />
        <p>
          hello world
        </p>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://react.js.org"
          target="blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <div>
          <h2>Data from API:</h2>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      </header>
    </div>
  );
}

export default App;