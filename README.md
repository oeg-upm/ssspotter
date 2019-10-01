# ssspotter
[![Build Status](https://semaphoreci.com/api/v1/ahmad88me/ssspotter/branches/master/badge.svg)](https://semaphoreci.com/ahmad88me/ssspotter)
[![codecov](https://codecov.io/gh/oeg-upm/ssspotter/branch/master/graph/badge.svg)](https://codecov.io/gh/oeg-upm/ssspotter)

Simple Subject Column Spotter


|endpoint|method|description|
|---------|---------|------------|
|`/spot`| `GET`|a view that allow uploading a table and the system will spot the subject column|
|`/spot`| `POST`| To spot the subject column of a given table (see the parameters below)|


## Parameters:
* `table`: the file
* `technique`: the technique to be use to identify the subject column (see below).
* `callback`: a `POST` callback url to be called by the system when the subject column is identified.


#### Techniques
* `left_most`: pick the left most column
* `left_most_non`: pick the left most non-numeric column 
* `most_distinct`: pick the most distinct non-numeric column with average length less than 4 characters (T2K)
