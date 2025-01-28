import React from "react";

const DataProcessing = () => {
  return (
    <div>
      <h2 id="data-processing-steps">Data Processing Steps</h2>
      <h3>Identifying the Attribute</h3>
      <p>
        Before gathering data, we first decided on the targeted variables for each dataset:
      </p>
      <div className="table-responsive">
        <table className="table table-striped table-bordered align-middle">
          <thead className="table-dark">
            <tr>
              <th>Column Name</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>name</td>
              <td>Full name</td>
            </tr>
            <tr>
              <td>gender_guess</td>
              <td>Gender using <code>gender_guesser</code></td>
            </tr>
            <tr>
              <td>school_website</td>
              <td>School website</td>
            </tr>
            <tr>
              <td>field</td>
              <td>Field of interest</td>
            </tr>
            <tr>
              <td>paper_name</td>
              <td>Job market paper name</td>
            </tr>
            <tr>
              <td>paper_link</td>
              <td>Link to job market paper</td>
            </tr>
            <tr>
              <td>chair</td>
              <td>Chair</td>
            </tr>
            <tr>
              <td>committee_members</td>
              <td>Committee members</td>
            </tr>
            <tr>
              <td>year</td>
              <td>Year of completion</td>
            </tr>
            <tr>
              <td>university</td>
              <td>University name</td>
            </tr>
            <tr>
              <td>department</td>
              <td>Department</td>
            </tr>
            <tr>
              <td>cv_link</td>
              <td>Link to CV</td>
            </tr>
            <tr>
              <td>thesis</td>
              <td>Dummy if thesis is downloaded</td>
            </tr>
            <tr>
              <td>personal_website</td>
              <td>Personal website</td>
            </tr>
            <tr>
              <td>placement</td>
              <td>Where candidates were placed</td>
            </tr>
            <tr>
              <td>placement_type</td>
              <td>Type of placement</td>
            </tr>
            <tr>
              <td>academic</td>
              <td>Dummy if <code>placement_type</code> is academic</td>
            </tr>
            <tr>
              <td>postdoc</td>
              <td>Dummy if placement was postdoc</td>
            </tr>
            <tr>
              <td>gender_manual</td>
              <td>Manual fixes for gender</td>
            </tr>
            <tr>
              <td>thesis_name</td>
              <td>Name of thesis</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Data Scraping</h3>
      <p>This table shows our results with retrieving the relevant data (simplified snippet here):</p>
      <p>
        <em>Note:</em> For brevity, not all columns are displayed.
      </p>
      <p>
        <strong>Data Cleaning:</strong> We merged all data into a single dataset,
        performing additional cleaning such as standardizing column names, fixing
        known gender misclassifications, and removing duplicates.
      </p>
    </div>
  );
};

export default DataProcessing;
