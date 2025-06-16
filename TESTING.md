 # Testing Climbing Log
  ***
  ## Contents
  
  * [Code Validation](#code-validation)
    * [CSS code validation](#css-validation)
    * [HTML code validation](#html-validation)
    * [JavaScript validation](#javascript-validation)
    * [python code validation](#python-validation)

  * [Lighthouse Testing](#lighthouse-testing)

  * [Manual Testing](#manual-testing)
    * [Testing across different devices and browsers](#testing-across-different-devices-and-browsers)
    * [Testing Navbar](#testing-navbar-page)
    * [Testing Homepage](#testing-home-page)
    * [Testing Add User Page](#testing-add-user-page)
    * [Testing Login Page](#testing-login-page)
    * [Testing Delete Account Page](#testing-delete-account-page)
    * [Testing View Sessions Page](#testing-view-sessions-page)
    * [Testing Edit Climb Page](#testing-edit-climb-page)
    * [Testing Record Session Page](#testing-record-session-page)
    * [Testing Add Climb Page](#testing-add-climb-page)
    * [Testing Session Info Page](#testing-session-info-page)
    * [Testing 404 page](#testing-404-page)
    
  * [Bugs](#bugs)

  * [Testing Stories](#testing-user-stories)

***

### Code validation <a name="code-validation"></a>

#### CSS validation <a name="css-validation"></a>

My CSS code passed validation with no errors

![CSS validation](/static/images/css_validation.jpg.png)

#### HTML validation <a name="html-validation"></a>

My HTML code has a number of errors as seen below, these were due to a number of trailing slashes, br elements being used in lists and an unclosed div.

![HTML validation before 1](/climbing_log/static/images/html_validation.jpg)

![HTML validation before 2](/climbing_log/static/images/html_validation1.jpg)

![HTML validation before 3](/climbing_log/static/images/html_validation2.jpg)

I rectified all these issues and my code passed as can be seen below

![HTML validation after](/climbing_log/static/images/html_validation_pass.jpg)


#### JavaScript validation <a name="javascript-validation"></a>

JSHint JavaScript validator highlighted two warnings to not use "new" as a side effect

![JavaScript validation](/static/images/js_validation.jpg.png)



#### Python validation

The [Code Institute](https://pep8ci.herokuapp.com/#) python linter was used to ensure my
python code was PEP8 compliant

This highlighted one issue with a line too long

![python validation](/static/images/python_validator.jpg.png)



### Lighthouse testing <a name="lighthouse-testing"></a>

Lighthouse testing was good scores for all parts

![lighthouse score](/static/images/lighthouse.jpg.png)


***

### Manual testing <a name="manual-testing"></a>

#### Testing across different devices and browsers  <a name="testing-devices-browsers"></a>

Browser | Outcome | Pass/Fail  
--- | --- | ---
Google Chrome | Site functioned as expected, design appearance correct and responsive across different screen sizes | Pass
Microsoft Edge | Site functioned as expected, design appearance correct and responsive across different screen sizes | Pass
Mozilla Firefox | Site functioned as expected, design appearance correct and responsive across different screen sizes | Pass


#### Testing site features  <a name="testing-site-features"></a>

#### Testing Navbar Page  <a name='testing-home-page'></a>

##### User not logged in Navbar

Feature | Outcome | Pass/Fail  
--- | --- | ---
Fishing log text link | clicking Text link reloaded homepage | Pass
Create account page link | clicking link loaded create account form | Pass
Login link | clicking link loaded user login form | Pass

##### User logged in Navbar

Feature | Outcome | Pass/Fail  
--- | --- | ---
Fishing log text link | clicking text link reloaded dashboard | Pass
View your recent session link | clicking link loaded recent session | Pass
Log a session | clicking link log a session | Pass
Logout link | clicking link logges out user  | Pass
Delete account link | clicking link delete user views a confirmation text| Pass


#### Testing Home Page  <a name='testing-home-page'></a>

##### Not logged in:

Feature | Outcome | Pass/Fail  
--- | --- | ---
Page content | All page content loaded correctly and visible to user | Pass
Sign up here button | clicking button loaded create account form | Pass
Login to your account button | clicking button loaded user login form | Pass

##### Logged in:

Feature | Outcome | Pass/Fail  
--- | --- | ---
Page content | All page content loaded correctly and visible to user | Pass
Log a session button | clicking button loaded new session form | Pass
View recent sessions button | clicking button loaded view recent sessions page | Pass
track your progress | views all content with charts, statistic and edit button for recent session | Pass



#### Testing Add User Page  <a name='testing-add-user-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---
Page content | All page content loaded correctly and visible to user | Pass
Add user form | Form submitted correctly created user in database | Pass
Password check | Password must be correctly entered twice, two different passwords flash error message, length must be greater than 8 | Pass
Username check | Flashed error when tried to use a username which already existed in database | Pass
Complete form | Couldn't submit incomplete form | Pass


#### Testing Login Page  <a name='testing-login-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---
Page content | All page content loaded correctly and visible to user | Pass
Login form | Successfully logged user into site | Pass
username field | Incorrect username entered flashed correct error message | Pass
Password field | Incorrect password entered flashed correct error message | Pass



#### Testing your recent session <a name='testing-view-sessions-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  


#### Testing Edit logged sessions  <a name='testing-edit-climb-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
Get fishing details from database | All fishing details correctly retrieved from database and filled into form | Pass
Edit fishing form submission | correctly updated climb information upon submission | Pass  
clicking save button| clicking button returned user to dashboard and flashed message | Pass  

#### Testing log a fishing session  <a name='testing-record-session-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
log a fishing session | correctly recorded new session upon submission | Pass  
dashboard button | clicking button returned user to homepage without saving session | Pass  



#### Testing track your records page   <a name='testing-session-info-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
Graphs and statistics | All graphs and statistics shows | Pass  
View button | clicking the view more button shows all logged records| Pass  
Edit button | clicking edit button redirects user to edit page | Pass
Dashboard | clicking the button takes you back to dashboard page | Pass





***

### Testing User Stories <a name="testing-user-stories"></a>

#### User Story 1: Creating account 
*As a user of the site I want to be able create an account*

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Create new account | User can create a useraccount and logg in. | Pass 


#### User Story 2: Log a fishing session 
*as a user of the site I want to be able to save my fishing sessions with the number of fish I cought and save it.*

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Log fishing session | User can create a fishing session and log it to the database| Pass 
Number of fishes cougt | User can log how many fishes they cought | Pass 
Spicies | User can enter wich type of fish they cought | Pass 
 

#### User Story 3: Logged sessions 
*as a user of the site I want to be able to see my logged sessions*

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Current session | User can see their current session being logged in detail | Pass 
All sessions | User can view all of their sessions they logged | Pass 


#### User Story 4: Track records 
*as a user of the site I want to be able to track my progress and compare number of fish I caought per month..*

Feature | Outcome | Pass/Fail  
--- | --- | ---  
All sessions| User can view all logged sessions| Pass 
Chart | User can see charts ant statistics over all cought fish, fish cought per month | Pass 


