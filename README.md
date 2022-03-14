## Blog Master

#### Author: [Venus Kavunza](https://github.com/Venus-Kavunza)


* Link to live site: [blogmaster]()

## Description
This is a  blog website where you can create your own blog and other users can read and comment on them.It has a feature that displays random quotes to inspire users.

## My Blogs
The user would like to.... :
*  View the blog posts on the site
*  Comment on blog posts
*  View the most recent posts
*  An email alert when a new post is made by joining a        subscription.
* See random quotes on the site

The writer would like to... :

* see random quotes on the site
* sign in to the blog.
* create a blog from the application.
* delete comments that I find insulting or degrading.
* update or delete blogs I have created.




## Behaviour Driven Development
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View blog | Click on comment | Taken to the clicked post | Click on `Comment` | Taken to where you can comment | Signs In/ Signs Up |
| Click on `Click Add a blog` | If logged in, display form to add a blog| Redirected to the home page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
| Click on Sign Out | Redirects to the home page | Signs user out |


## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/Venus-Kavunza/blog_master.git
        $ cd blog_master

## Running the Application
* Install virtual environment using `$ python3.8 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.8 pip install -r requirements.txt`
* Create a `start.sh` file in the root of the folder and add the following code:

        export MAIL_USERNAME=<your-email-address>
        export MAIL_PASSWORD=<your-email-password>
        export SECRET_KEY=<your-secret-key>

* Edit the configuration instance in `manage.py` from `development` to `production`
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class file:

        $ python3.8 manage.py server
        
## Built With

* [Python3.8](https://docs.python.org/3/)
* Flask
* Boostrap
* HTML
* CSS

### License
MIT License

Copyright (c) 2022 Venus Mwende

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors Info
Email - [Venus Mwende](venusmwende@gmail.com)