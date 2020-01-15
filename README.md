# PITCHAPP
PitchApp is a web application that allows people pitch themselves or present their ideas and practice making great first impressions in one minute

## Author
Loise Muthoni

## Features
As a user of the application, you will be able to:

- See different pitches posetd by other people
- Post your own pitch
- Vote for other people's posts
- Comment on other people's pitches
- create an account, login and update your profile
## BDD
| Behaviour             |                Input                |                                                                       Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------------: |
| Load the page         |          **On page load**           |                               Get all posts, Select between signup and login |
| Select SignUp         | **Email**,**Username**,**Password** |                                                            Redirect to login |
| Select Login          |    **Username** and **password**    | Redirect to page with app pitches based on categories and commenting section |
| Select comment button |             **Comment**             |                                             Form that you input your comment |
| Click on submit       |                                     |       Redirect to all comments tamplate with your comment and other comments |

# Getting started

## Prerequisites
- python
- Virtual environment
- pip
## Cloning
Navigate into the folder you want the application to be In your terminal, run the commands

$ git clone https://github.com/loisemuthoni/pitch.git

$ cd PitchApp

## Live Link
- https://pitcherloise.herokuapp.com/

## Technologies used
- Python 
- Flask 
- Html 
- Bootstrap

## Copyright (c) 2020 Loise Muthoni
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. Copyright (c) 2020 loisemuthoni