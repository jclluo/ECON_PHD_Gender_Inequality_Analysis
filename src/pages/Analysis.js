import React from "react";

const Analysis = () => {
  return (
    <div>
      <h2 id="analysis">Analysis</h2>
      <h3>Key Insights</h3>
      <p><strong>Placement by Type:</strong></p>
      <ul>
        <li>60.48% of candidates were placed in academic positions.</li>
        <li>13.73% went to industry roles.</li>
        <li>11.08% of candidates became postdocs.</li>
      </ul>

      <h4>Tabular Representation of Gender Composition</h4>
      <div className="table-responsive">
        <table className="table table-bordered align-middle text-center">
          <thead className="table-dark">
            <tr>
              <th>Gender</th>
              <th>Overall (%)</th>
              <th>Academic (%)</th>
              <th>Postdoc (%)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Male</td>
              <td>70.65</td>
              <td>69.60</td>
              <td>68.57</td>
            </tr>
            <tr>
              <td>Female</td>
              <td>29.35</td>
              <td>30.40</td>
              <td>31.43</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>
        The table indicates males comprise ~70% of the overall dataset, with slightly lower proportions 
        in academic and postdoc roles. Females are ~29.3% overall, with a slight rise in academic/postdoc 
        representation.
      </p>
      <p>
        For detailed results, see <em>Gender Gap PhD STEM Analysis</em>.
      </p>
    </div>
  );
};

export default Analysis;
