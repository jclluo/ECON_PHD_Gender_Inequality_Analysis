import React from "react";

const Home = () => {
  return (
    <div className="home-section">
      <h1 className="mb-4">
        Overview of Possible Gender Inequality Among TOP 20 Economics PhD Programs
      </h1>
      <h2 id="project-overview">Project Overview</h2>
      <p>
        <strong>About:</strong> For this project, we collected comprehensive data on job market
        candidates from the top 20 Economics PhD programs in the United States, including information
        on gender, fields of study, and dissertation topics. Additionally, we gathered job placement data
        from the same institutions to analyze the employment outcomes (e.g., company or institution, position)
        of graduating PhD students.
      </p>
      <p>
        Our analysis involved generating summary statistics and conducting regression analyses to examine 
        the relationship between gender and job placement outcomes.
      </p>

      <h3>Contributions:</h3>
      <ul>
        <li>Lea Angelakos</li>
        <li>Samantha Chan</li>
        <li>Amy Dao</li>
        <li>Chris Luo</li>
        <li>Jia Yi (Tracy) Zhao</li>
      </ul>
    </div>
  );
};

export default Home;
