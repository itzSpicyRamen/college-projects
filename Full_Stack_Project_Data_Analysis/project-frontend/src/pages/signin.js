import React from 'react';
import './signin.css';
import {useState} from 'react';

const Signin = () => {
  const [status, setStatus] = useState(undefined);
  const [data,setData] = useState({
    username:"",
    password:""
  });
  const submitHandler = e => {
    var jsonData = {"username": username, "password" : password}
    e.preventDefault();
    console.log(data);
    let setResp = this;
    // Send data to the backend via PUT
    fetch('http://localhost:5000/signin', {  // Enter your IP address here

      method: 'PUT', 
      mode: 'cors', 
      body: JSON.stringify(jsonData) // body data type must match "Content-Type" header

    }).then(response => {
      if(!response.ok) setStatus({ type: 'error' });
      else setStatus({ type: 'success' });
      return response.json();
    }) 
    .catch(error => console.log(error));
  }
  const changeHandler = e => {

    setData({...data,[e.target.name]:[e.target.value]});
    
  }

  const {username,password} = data;

  return (
    <div>
      <form className = 'signinform' onSubmit={submitHandler}>
      <input type="text" name="username" value={username}
      onChange={changeHandler}/><br />
      <input type="password" name="password" value={password}
      onChange={changeHandler}/><br />
      <input type="submit" name="submit" />
      </form>
      <>{status?.type === 'success' && <div style={{color: "White", padding: "15px"}}>Admin login successful!
    <h1>Upload your CSV file</h1>
    <form method="PUT" action="" enctype="multipart/form-data">
      <p><input type="file" name="file"></input></p>
      <p><input type="submit" value="Submit"></input></p>
    </form>
      </div>}
      {status?.type === 'error' && <div style={{color: "White", padding: "15px"}}>Login failed</div>}</>
    </div>
  );
};
  
export default Signin;