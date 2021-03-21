# Criminal Occurrences Visualization
This tool is intended to create a crime map visualization from a smartphone burglary dataset.

## Technology

- Front-End
    - HTML5
    - CSS3
    - Leaflet.sj

- Back-End

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

### 01 - Installation

- Before executing the building, insert the Dockerfiles names in: `image_list.txt`

- To select what Dockerfiles to build `${ROOT_DIR}/notes/sizesortedlist-dockerfiles.txt`
    - The filename must have this format `sources/228568839.Dockerfile`

- To build Dockerfiles run the script:

```
./build_test.sh
```

- The generated logs will be located under directory `${ROOT_DIR}/logs/`. Logs for build failures
  will be at `${ROOT_DIR}/logs/fail` and logs of successful builds will be at `${ROOT_DIR}/logs/success`.

- Files that contain "returned a non-zero code" will be in `${ROOT_DIR}/results/files_to_analyze.log`

### 02 - Execution

- cd to directory `${ROOT_DIR}/query_proc`

- The following script processes a log file to generate a list of keywords and URLs 
that contains fix recommendations. Dockerfiles located in `${ROOT_DIR}/results/files_to_analyze.log` will be processed.

For example:

```
python3 keyword_creator.py
```

### 03 - Check query results

- Check the output at: 

```
${ROOT_DIR}/results/analyzed_query.json.
```

 - Analyzed query example:

 ```
 {
    "Hash: 154176094": [
        {
            "Log fragment": "E: The repository 'http://archive.ubuntu.com/ubuntu artful-updates Release' does not have a Release file.  E: The repository 'http://archive.ubuntu.com/ubuntu artful-backports Release' does not have a Release file.  \u001b[0mThe command '/bin/sh -c apt-get update -qq -y' returned a non-zero code: 100 ",
            "Query": "ubuntu release a e the repository http archive",
            "URLs": {
                "0": "https://askubuntu.com/questions/1120194/e-the-repository-http-archive-canonical-com-precise-release-is-not-signed",
                "1": "https://askubuntu.com/questions/996718/ubuntu-repository-does-not-have-a-release-file"
            }
        }
    ]
}
 ```

 ## Preliminaries

This repository work is in-flux, at this time there are only a few pre-results. The dataset of Dockerfiles must be in Context to avoid misconfiguration errors. We are using TF-IDF to generate the keywords, first, we tried to use the RAKE algorithm, but we can't get good results.