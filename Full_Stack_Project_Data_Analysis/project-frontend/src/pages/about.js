
import React from 'react';
import './about.css';

const About = () => {
  return (
    <div
      style={{
        justifyContent: 'Right',
        alignItems: 'Right',
        height: '100vh'
      }}
    >
      {/* <p style="color: #ffffff"> </p> */}
      <h1>About</h1>
      <h3>Our product is a Baltimore City COVID-19 and Crime Data Visualizer. The main functionalities of this product include the ability to view approximately 200,000 crime cases visualized on an interactive heatmap and the ability to view approximately 200,000 COVID cases and 4,000 deaths on interactive charts and graphs. Our goal in creating these functionalities are to allow the user to explore the relationship between COVID-19 and Crime in Baltimore City. To enable the user to explore this relationship further, we have implemented various data filtering options - for example, the capability to filter by year, type of crime, district, or gender. 
</h3>
      <h3>Our sources for all the data are below:
      <li><a href="https://data.baltimorecity.gov/datasets/baltimore::part-1-crime-data-/explore?location=39.310722%2C-76.584862%2C15.52&showTable=true">Crime Data</a></li>
      <li><a href="https://coronavirus.maryland.gov/datasets/maryland::mdcovid19-casesbycounty/explore">COVID Cases Data</a></li>
      <li><a href="https://coronavirus.maryland.gov/datasets/maryland::mdcovid19-confirmeddeathsbycounty/explore?filters=eyJCYWx0aW1vcmUiOlswLDI2MTJdLCJCYWx0aW1vcmVfQ2l0eSI6WzAsMTg1M119">COVID Deaths Data</a></li>
      </h3>


      
<h1>Our Team</h1>
<div class="row">
  <div class="column">
    <div class="card">
      <div class="container">
        <h2>Tristan Galcik</h2>
        <p class="title">Sprint Leader/Frontend Developer</p>
        <p>tgalcik1@umbc.edu</p>
      </div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <div class="container">
        <h2>Caleb Luke</h2>
        <p class="title">Frontend Developer</p>
        <p>cluke1@umbc.edu</p>
      </div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <div class="container">
        <h2>Roberto Villanueva</h2>
        <p class="title">Backend Developer</p>
        <p>robertv1@umbc.edu</p>
      </div>
    </div>
  </div>
</div>

<div class="row">
<div class="column">
    <div class="card">
      <div class="container">
        <h2>Opeyemi Kusemiju</h2>
        <p class="title">Backend Developer</p>
        <p>opeyemk1@umbc.edu</p>
      </div>
    </div>
  </div>

<div class="column">
    <div class="card">
      <div class="container">
        <h2>Obinna Ezejiofor</h2>
        <p class="title">Frontend Developer</p>
        <p>obinnae1@umbc.edu</p>
      </div>
    </div>
  </div>
</div>
    </div>
  );
};
  
export default About;