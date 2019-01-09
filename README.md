<a href="https://codeclimate.com/github/HarrietAkot/I-Reporter/maintainability"><img src="https://api.codeclimate.com/v1/badges/b49b18e11ea041b54c99/maintainability" /></a>
[![Coverage Status](https://coveralls.io/repos/github/HarrietAkot/I-Reporter/badge.svg?branch=master)](https://coveralls.io/github/HarrietAkot/I-Reporter?branch=master)
[![Build Status](https://travis-ci.org/HarrietAkot/I-Reporter.svg?branch=develop)](https://travis-ci.org/HarrietAkot/I-Reporter)





# I-Reporter
I-Reporter is a platform where people can report incidents of corruption.

## Project overview
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

## Functionality
- Create a red-flag record
- Get all red flag records
- Get specific red flag record
- Edit a red-flag's location
- Edit a red-flag's comment
- Delete red flag record

## Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   |/api/v1/red-flags/ |Create red flag|
| GET    |/api/v1/red-flags/all|Get all red flags|
| GET    |/api/v1/red-flags/<int:red_flag_id>/|Get specific red flag|
| PATCH  |/api/v1/red-flags/<int:red_flag_id>/location/|Edit red flag location|
| PATCH  |/api/v1/red-flags/<int:red_flag_id>/comment/|Edit red flag comment|
| DELETE |/api/v1/red-flags/<int:red_flag_id>/|Delete red flag|



### Authors
Akot Harriet Peace
