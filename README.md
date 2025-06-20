# fishing-log

![Website main image](/static/images/lake_sunset.jpg)

Fishing Log is an Website making it possible for fisherman to make their catch a little more exiting! Log your session and track your progress through chart and statistics to be a better fisherman. 

Live site of the view is being deployed at heroku. [Here!](https://fishing-log-ecfc8a6f98ec.herokuapp.com/)

A Test account has been created for all of u to use if you don't want to create an own ofcourse!

Username: Test

Password: Logintest

***
## Contents

1 [User Experience (UX)](#UX)

  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
  * [Database schema](#database-schema)
  * [Wireframes](#wireframes)
  * [Color Scheme and Font](#styles)


2 [Features](#features)

 * [Database](#database)
 * [NavBar](#navbar)
 * [Footer](#footer)
 * [Flash Messages](#flash-messages)
 * [Page Features](#page-features)
 * [404 page](#404-page)


3 [Technologies Used](#technologies-used)

4 [Credits](#credits)

4 [Testing](#testing)

5 [Deployment](#deployment)


***
## User Experience (UX) <a name="UX"></a>

### Project Goals <a name="project-goals"></a>

* Make a website to enable fisherman to track their sessions.

* Make users be able to create an personla account and store it in the database.

* Retrive their information and display it in graphs and statistics charts.

*  Have clear instructions and user interface

***

### User stories <a name="user-stories"></a>


* As a user of the site I want to be able create an account

* as a user of the site I want to be able to save my fishing sessions with the number of fish I cought and save it.

* as a user of the site I want to be able to see my logged sessions

* as a user of the site I want to be able to track my progress and compare number of fish I caought per month.


***

### Database schema <a name="database-schema"></a>


[dbdiagram](https://dbdiagram.io/home)  was used to create a database schema and wireframes for the project.

![Databas_schema](/static/images/data_schema.jpg.png)

The database is a simple design with a single user having one or more sessions and each session containing one or more fishing logs. An email and password are included for users to allow the user to login.

***

### Wireframes <a name="wireframes"></a>

### Mobile and desktop wireframes

![screenshot of wireframes](/static/images/wireframe.jpg.png)

***

### Colour Scheme and Font <a name="styles"></a>

#### The color scheme for the site

![Color scheme](/static/images/color_scheme.jpg.png)

The colors used in this website is a combination of black, white and orange. Where all text has the color white, buttons and navlinks uses ornage color. And I use black color as the background

#### The font used for the site

The font "Edu SA Hand" from [Google fonts](https://fonts.google.com/) is used for the site, with Cursive set as a back-up if it can't be loaded.
This font is used in a variety of weights across the site, it is clear for users to read and the titles are easily read against the background image.

***

## Features <a name="features"></a>


### Database <a name="database"></a>


#### Relational vs Non-Relational Databases

For this project I was required to use a database and implement CRUD functionality.

- Create: Adding new data or records to the database.

- Read: Retrieving or querying data from the database.

- Update: Modifying or editing existing data or records.

- Delete: Removing data or records from the database.

#### CRUD Functionality 

My app demonstrates CRUD functionality as outlined below:

#### Create:

- Creating user account
- Creating fishing sessions


#### Read:

- Reading from Sessions table to display recent sessions on dashboard page and sessions page
- Reading from Users table for logging in
- Reading from Sessions table for displaying fishing information on sessions page and for creating interactive graphs/charts on session_list page


#### Update:

- Edeting fishing session by clicking edit button under all fishing session
- Can change all content logged

#### Delete:

- Deleting fishing rocords in log fishing session before save
- Deleting every stat on the dashboard page
- Deleting fishing session inside edeting form

<br>

#### 1. Relational Databases

Structured Model: Utilize a table-based format, organizing data into rows and columns.

Data Organization: Manage structured data efficiently with well-defined relationships.

Complex Relationships: Ideal for applications that require handling intricate 
relationships between data.

Consistency: Ensure strong data consistency and integrity.

#### 2. Non-Relational Databases

Flexible Models: Offer various data models like documents, key-value pairs, or graphs.

Scalability: Designed to scale horizontally and handle dynamic, unstructured data.

Adaptability: Well-suited for applications with rapidly changing data requirements and unstructured content.

***

### NavBar <a name="navbar"></a>

Navbar for mobile screensizes, contains a button to expand and show available pages, site title is in top left which links back to home page.

![NavBar mobile](/static/images/navbar_mobile.png)

Navbar for mobile screensizes when expanded shows current page options depending on user login status.

![NavBar mobile expanded](/static/images/navbar_mobile_expandedjpg.png)

Larger screen size navbar displays Sign up and a log in link.

![NavBar](/static/images/navbar_logged_out_desktop.png)

Larger screen size navbar for when users are logged in, displaying the users name and log out link


![NavBar logged in](/static/images/navbar_desktop.jpg.png)

***

### Footer  <a name="footer"></a>

Footer contains icons for social media, which are clickable links opening up these pages in new tabs

![Footer](/static/images/social_media.jpg.png)

***

### Flash Messages <a name="flash-messages"></a>

The site contains a number of flash messages which display as a banner under the navbar, these provide feedback to the user to let them know that operations have been performed successfully when they interact with the page

- flash message for when user logs out of their profile

![logged out flash message](/static/images/sign_out_message.jpg.png)

- flash message for when the user logs into their profile

![logged in flash message](/static/images/sign_in_message.jpg.png)

- flash message when fishing session has been logged.

![Logges fishing session](/static/images/logged_session.jpg.png)



***

### Page Features <a name="page-features"></a>

***

#### Homepage

The homepage features the hero image, this is present across the whole site.

The homepage is the first page the user is presented with when visiting the site, it contains three cards, one has a short explanation of the site, one prompts them to create a user account and the other to log in if they already have an account.
Both of these options are also displayed for quick access on the navbar.

Once the user is logged in the cards then change one for logging a fishing session, one for viewing the latest session and the last alla of their session with graphs and  statistic.

##### Home page when user not logged in

![Home page not logged in](/static/images/home_page_not_logged_in.jpg.png)

##### Homepage when user logged in

![Home page logged in](/static/images/home_page_user_logged_in.jpg.png)


##### Page purpose card

  ![Details of page purpose](/static/images/welcome_card.jpg.png)

##### Link to create account card

  ![Home page link to create account](/static/images/create_account.jpg.png)

##### Link to login card

  ![Home page link to login](/static/images/log_in_card.jpg.png)

##### Most recent session cards

  ![Home page recent sessions link](/static/images/your_recent_session.jpg.png)


##### Link to log a new fishing session card

  ![link to log a new climbing session](/static/images/log_fishing_session_card.jpg.png)

##### Link to view all sessions card

  ![link to track your records](/static/images/track_your_records_card.jpg.png)

***

#### Create user page

The create user page contains a form which gathers information required to set up an account, the page layout revolves around the hero image.
It has features which ensure the password must be entered twice and match before the form can be submitted.There is also user feedback through flash messages discussed above, these ensure already existing usernames/emails cannot be used again. There is also feedback which tells the user when they have successfully created an account. 

##### Create user page 

![create user page form](/static/images/create_account.jpg.png)



***

#### Login Page 


The login page allows user to enter their login details to access the site features which require login.
It has flash messages, discussed in details above, which appear to provide feedback to the user. To notify them of using an incorrect password, using and incorrect username and when they successfully log in.

##### Login page

![Login page](/static/images/log_in_card.jpg.png)

***

#### Delete Account Page

The delete user account page allows user to delete their account removing all their information from the database
It also contains explanation that doing so will be permanent and that logged data will not be able to be retrieved and password confirmation is required for this step to protect the user.


##### Delete account page

![Delete account page](/static/images/delete_acount.jpg.png)



***

#### View Recent session

The view recent session allows the user to see their current logged fishing session with date, location, total of fish cought.

##### View sessions page large screen sizes

![View session page on large screens](/static/images/last_fishing_session_desktop.jpg.png)

##### View sessions page small screen sizes

![View session page on small screens](/static/images/last_fishing_session_mobile.jpg.png)



##### Delete all stats

![View session delete climb modal](/static/images/delete_stats.jpg.png)

***

#### Edit Fishing logs

The edit fishing session allows the user to edit a current session logged or delete it completly

![Edit fishing session page](/static/images/edit_fishing_session.jpg.png)



#### Track your records

The track your rocords page enables the user to see all of their logged session with an maximum of 5 off the latests logs with and button to view more if you want to se them all. You can also see an record with statistics over how many fish in total you have catched and a graph of how many fish per month you have caought.

![Record session page](/static/images/track_records.jpg.png)



#### Add fishing session

The log fishing page the user can fill in current location, date, species in the dropdown menu and number of fish they catch. After they clicked the add button they can choose to fill in another type of species if they cought more than one.



![Add fishing log](/static/images/log_fishing_session.jpg.png)




***



## Technologies used <a name="technologies-used"></a>


This Project uses the following languages:

* HTML
* CSS
* JavaScript
* Python

[PostgreSQL](https://www.postgresql.org/) was used as the database to store and manage application data.

[Django](https://www.djangoproject.com/) backend framework was used to build the back end for this project.


[Bootstrap](https://getbootstrap.com/) was used to assist in creating a responsive layout and for prebuilt components such as the accordions and header/footer.

[Git](https://git-scm.com/) and [GitHub](https://github.com/) for version control and as a repository.

[Google Fonts](https://fonts.google.com/) was used to browse, select and as a source of the font I used on this site.

[FontAwesome](https://fontawesome.com/) was used for social media icons in the footer.



Please see the requirements.txt for a full list of the packages used and versions in my project.

<br>

## Credits <a name="credits"></a>

The background image used on the site was taken by me, and I own all rights to it.

When creating my project I frequently used the docs for
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Django](https://docs.djangoproject.com/en/5.2/)




## Testing  <a name="testing"></a>

Testing was performed and documented in detail in a separate file.

The testing documentation can be viewed [here](/TESTING.md)

<br>

## Deployment

This project was developed using Microsoft Visual Studio Code, committed to Git and pushed to GitHub using the terminal with in VS code.

The final Live version of site is hosted on Heroku and can be found [here]()

###  Deploying to Heroku

The project was deployed to Heroku, below are the steps taken:

1. Create a requirements.txt file.
pip freeze --local > requirements.txt

2. Create a Procfile details on [heroku here](https://devcenter.heroku.com/articles/procfile#:~:text=The%20Procfile%201%20Procfile%20naming%20and%20location%20The,type%20examples%20...%207%20Procfile%20and%20heroku.yml%20).

3. Add and commit the changes with git, and push the project to GitHub.

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the new button in your dashboard. 

5. Confirm the linking of the Heroku app to the correct GitHub repository.

6. In the Heroku dashboard for the application, click on settings then reveal config vars and set up the configs.

7. From the Heroku dashboard of your newly created application, click deploy then deployment Method and select GitHub.

8. In the manual deployment section of this page, make sure the master branch is selected and then click deploy branch.

9. On the Heroku dashboard, click deploy.

10. Open the console on Heroku and run a python3 terminal, create the db using db.create_all()


