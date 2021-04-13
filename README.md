# Criminal Occurrences Visualization
This tool is intended to create a crime map visualization from a smartphone burglary dataset.

## Technology

- Front-End
    - HTML5
    - CSS3
    - Leaflet.js

- Back-End
    - Python
    - Pandas
    - Flask

- Dataset
    - The dataset was downloaded from São Paulo state <a href="http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx">open data site.</a>

 ## Usage / Setup
To use the crime_occur_vis, use Linux or Windows, and install the following requirements.

- Latest version: 

- `Apache or Nginx`
- `Python3`
- `pip3`
- `Linux`

Install our requirements:

```
pip3 install -r requirements.txt
```

## 01 - Installation

- The tool is divided into two parts: the front-end and the API.

### API

- First, go to the API directory:

    - Change to directory `api/`

- Then run the API with the following python script:

```
python3 api/routes.py
```

 - The API will run in the following address:

```
http://localhost:5000/getoccur?ini_month=Julho&brand=APPLE
```

### Front-end

- Before opening the visualization in a web-browser check the API address.

- Using your favorite IDE open the following file `assets/js/site.js`

 - Go to line 15 and change the API address:
 
```
xhttp.open("GET", "http://api.crimevis.work
```

## 02 - Execution

- Using your favorite web-browser open `index.html`

- Select month and smartphone brand.

- After loading data, it is possible to check, location, brand, and the kind of occurrence.


## 03 - Live demo

- There is a live demo available at <a href="http://crimevis.work">crimevis.work</a>

## Preliminaries

This work is still under construction, in the future a paper must be written to describe the methodology used in the study to construct the tool.