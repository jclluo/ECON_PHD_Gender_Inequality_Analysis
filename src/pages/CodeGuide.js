import React from "react";

const CodeGuide = () => {
  return (
    <div>
      <h2 id="code-guide---refer-to-files-with-brief-description">Code Guide</h2>
      <h3>Data Scraping using Python</h3>
      <p>Here is a <strong>very</strong> brief overview of how data scraping works with Python.</p>
      <ol>
        <li><strong>Import Required Packages</strong>:
          <pre><code>
{`import requests
from bs4 import BeautifulSoup
`}
          </code></pre>
        </li>
        <li><strong>Fetch Webpage Content</strong>:
          <pre><code>
{`response = requests.get("https://example.com")
html_content = response.text
`}
          </code></pre>
        </li>
        <li><strong>Parse HTML Content</strong>:
          <pre><code>
{`soup = BeautifulSoup(html_content, "html.parser")
`}
          </code></pre>
        </li>
        <li><strong>Extract Data</strong>:
          <pre><code>
{`data = soup.find_all('div', class_='data-class')
`}
          </code></pre>
        </li>
        <li><strong>Clean and Structure Data</strong>:
          <p>Process extracted data into a structured format (list or dictionary).</p>
        </li>
        <li><strong>Save Data to CSV</strong>:
          <pre><code>
{`import pandas as pd
df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)
`}
          </code></pre>
        </li>
      </ol>

      <h4>Corresponding Files</h4>
      <p>Please refer to the file_guide spreadsheet for more details:</p>
      <div className="table-responsive">
        <table className="table table-striped table-bordered align-middle">
          <thead className="table-dark">
            <tr>
              <th>School</th>
              <th>File Name</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>NYU</td>
              <td>
                <code>NYU_code.py</code>
              </td>
              <td>Scrapes NYU JMC data and performs analysis.</td>
            </tr>
            <tr>
              <td>UCB and UChicago</td>
              <td>
                <code>UCB_UCHICAGO_SCRAPE.ipynb</code>
              </td>
              <td>Scrapes JMC information and processes data.</td>
            </tr>
            <tr>
              <td>UC Davis Economics PhD</td>
              <td>
                <code>UCD_EconPhD.ipynb</code>
              </td>
              <td>Extracts and processes Economics PhD data.</td>
            </tr>
            <tr>
              <td>UC Davis Political Science PhD</td>
              <td>
                <code>UCD_PoliSciPhD.ipynb</code>
              </td>
              <td>Handles Political Science PhD data scraping and processing.</td>
            </tr>
            <tr>
              <td>UC Merced Economics PhD</td>
              <td>
                <code>UCM_EconPhD.ipynb</code>
              </td>
              <td>Analyzes Economics PhD data.</td>
            </tr>
            <tr>
              <td>UC Merced Political Science PhD</td>
              <td>
                <code>UCM_PoliSciPhD.ipynb</code>
              </td>
              <td>Scrapes and processes Political Science PhD data.</td>
            </tr>
            <tr>
              <td>UCSD Business PhD</td>
              <td>
                <code>UCSD_BusinessPhD.ipynb</code>
              </td>
              <td>Analyzes Business PhD data.</td>
            </tr>
            <tr>
              <td>UCSD Economics PhD</td>
              <td>
                <code>UCSD_EconPhD.ipynb</code>
              </td>
              <td>Extracts and cleans Economics PhD data.</td>
            </tr>
            <tr>
              <td>UCSD Political Science PhD</td>
              <td>
                <code>UCSD_PoliSciPhD.ipynb</code>
              </td>
              <td>Analyzes Political Science PhD candidate data.</td>
            </tr>
            <tr>
              <td>University of Chicago</td>
              <td>
                <code>chicago8.py</code>
              </td>
              <td>Processes PhD candidate information.</td>
            </tr>
            <tr>
              <td>Northwestern Economics</td>
              <td>
                <code>nwecon2.py</code>
              </td>
              <td>Processes Economics candidate data.</td>
            </tr>
            <tr>
              <td>Stanford</td>
              <td>
                <code>stanford.py</code>
              </td>
              <td>Scrapes PhD candidate data and extracts website links.</td>
            </tr>
            <tr>
              <td>General-purpose</td>
              <td>
                <code>test6.py</code>
              </td>
              <td>Extracts data and performs processing.</td>
            </tr>
            <tr>
              <td>University of Chicago (advanced)</td>
              <td>
                <code>u_chicago_v9.py</code>
              </td>
              <td>Handles advanced data processing for PhD candidates.</td>
            </tr>
            <tr>
              <td>University of Pennsylvania Economics</td>
              <td>
                <code>upenn_econ.csv</code>
              </td>
              <td>Contains Economics PhD candidate data.</td>
            </tr>
            <tr>
              <td>Yale</td>
              <td>
                <code>yale_econ_jm_candidates.ipynb</code>
              </td>
              <td>Script for current (2023-2024) Yale Economics PhD scraping.</td>
            </tr>
            <tr>
              <td>Yale</td>
              <td>
                <code>yale_econ_jm_candidates_v2.ipynb</code>
              </td>
              <td>Script for past (2019-2022) Yale Economics PhD scraping.</td>
            </tr>
            <tr>
              <td>Yale</td>
              <td>
                <code>yale_econ_jm_placements.ipynb</code>
              </td>
              <td>Script for Yale Economics PhD job placements.</td>
            </tr>
            <tr>
              <td>Yale</td>
              <td>
                <code>yale_econ_jm_candidates_wayback_links.csv</code>
              </td>
              <td>Wayback Machine links for past Yale Economics PhD candidates.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default CodeGuide;
