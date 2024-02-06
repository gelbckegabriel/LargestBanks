<div>
  <h1><strong>Largest Banks Analysis - Data Engineering (ETL)</strong></h1>
  <p>The Largest Banks is a data engineering project from Coursera to test skills to complete an ETL (Extract, Transform and Load) pipeline for accessing data from a website and processing to meet requirements, the code written in here was made from me. To execute my code, you will need to install a few python packages, such as: <strong>requests, bs4, pandas, sqlite3, numpy & datetime</strong>.
  </p>
  <h4>Author: <a href=https://www.linkedin.com/in/gabrielgelbcke/ target="_blank">©GabrielGelbcke</a></h4>

  <br>

  <h2>:wrench: Programming Languages & Tools used:</h2>
  <div id="tools">
    <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt="Python Logo" height="40" width="40" />
    <img src="https://github.com/devicons/devicon/blob/master/icons/pycharm/pycharm-original.svg" alt="Pycharm Logo" height="40" width="40" />
  </div>

  <br>

  <h2>:open_file_folder: Project Scenario:</h2>
  <p>
    I have been hired as a data engineer by research organization. My boss has asked me to create a code that can be used to compile the list of the top 10 largest banks in
    the world ranked by market capitalization in billion USD. Further, the data needs to be transformed and stored in GBP, EUR and INR as well, in accordance with the exchange rate
    information that has been made available to me as a CSV file. The processed information table is to be saved locally in a CSV format and as a database table.
    <br><br>
    You can find the required data on <a href="https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks" target="_blank">this wikipedia
      webpage</a>.
    <br>
    The exchange rate can be found on <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"
                                        target="_blank">this link</a>.
  </p>

  <br>
  
  <h2>:round_pushpin: Objective:</h2>
  <p>
    My job is to create an automated system to generate the requested information so that the same can be executed in every financial quarter to prepare the report.
  </p>

  <br>

  <h2>:mag: My Mission:</h2>
  <ul>
    <li type="1">Write a function to extract the tabular information from the given URL under the heading By Market Capitalization, and save it to a data frame.</li>
    <li type="1">Write a function to transform the data frame by adding columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.</li>
    <li type="1">Write a function to load the transformed data frame to an output CSV file.</li>
    <li type="1">Write a function to load the transformed data frame to an SQL database server as a table.</li>
    <li type="1">Write a function to run queries on the database table.</li>
    <li type="1">Run the following queries on the database table:</li>
    <ul>
      <li type="a">Extract the information for the London office, that is Name and MC_GBP_Billion</li>
      <li type="a">Extract the information for the Berlin office, that is Name and MC_EUR_Billion</li>
      <li type="a">Extract the information for New Delhi office, that is Name and MC_INR_Billion</li>
    </ul>
    <li type="1">Write a function to log the progress of the code.</li>
    <li type="1">While executing the data initialization commands and function calls, maintain appropriate log entries.</li>
  </ul>

  <br>

  <h2>:memo: Branches:</h2>
  <ul>
  <li>main:</li>

  ```
  Contains the folder where is the main code to run etl_process and also where you can find the output from it.
  ```

  </ul>

  <br>

  <h2>:globe_with_meridians: Reference:</h2>
  <ul>
    <li><strong>Coursera reference:</strong> <a href="https://www.coursera.org/learn/python-project-for-data-engineering/ungradedLti/GbThS/final-project-acquiring-and-processing-information-on-worlds-largest-banks" target="_blank">Click Here</a></li>
    <li><strong>Wikipedia page:</strong> <a href="https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks" target="_blank">Click Here</a></li>
    <li><strong>Exchange Rate CSV:</strong> <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv" target="_blank">Click Here</a></li>
  </ul>

