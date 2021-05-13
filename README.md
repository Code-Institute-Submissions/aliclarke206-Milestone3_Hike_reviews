# MileStone Project Three
## Hike Life Review

This project is a simple and responsive design to allow users to easily search, navigate to find new hikes and also to share reviews of hikes that the user may have already completed. The key features of each hike are broken down for quick and easy comparison. Users can also search hikes, locations are available and an email contact service is provided for any concerns or questions.  

## Ux
### Strategy

The basic strategy behind this application was to build a simple and easy to navigate site where all the daily tasks are stored in one place. It’s broken down into different categories to allow the user to amend to different lists and segregate tasks so all the tasks within one list are relevant to one another. It allows for better organisation of daily tasks.
The objectives behind building the site were to create a single place where users could come to track and organise their daily tasks and habits.

**User Stories**

As a user of this application: 

* I would like one place to track and store daily tasks.
* An ability to view sub categories and broken down tasks within these categories.
* Ability to add and remove tasks.
* Ability to check off when complete.
* Monitoring of the progression of completed tasks.
* Simplifies big tasks into smaller actions that compound over time. 
* Creates a visual cue with a progression bar that encourages you to act.
* Satisfying to record progress and check off tasks throughout the day. 
* Easy to use on desktop and mobile.
* Simple design with no complicated format. 


### Scope
The specifications and requirements for the site to adhere to the user stories include:
* A form to easily create new task categories
* A form to easily add new tasks to associated category
* A checkbox to check and uncheck completed tasks
* A button to clear completed tasks
* A button to clear a category
* A responsive counter to display tasks remaining
* A progress bar to display progression of tasks completed


### Structure
To ensure not to overload the user with all the tasks at once, the corresponding tasks linked to the category are displayed responsively. Once the user clicks on a category the corresponding task list changes.  This interaction design makes it very easy for the user to navigate through their category lists and corresponding task lists. 
All the data is stored in local storage so when the user goes back to the page the completed and uncompleted tasks are still there along with the categories they fall under.

### Skeleton
The structure of the site was designed in such a way that everything should be visible on the one page. There is no need to navigate away from the page and all the information is visible all together. The categories list is arranged on the left hand side in a smaller box and when clicked the corresponding task box appears on the right in a larger box. This is to accommodate left to right design and also as there typically would be more tasks than categories, the bigger task box allows for the larger task list to be seen clearer. 
The structure mock ups were roughly done on [Balsamiq WireFrames](https://balsamiq.com/) . 

[Home Page](wireframes/home_page.png)

[Add/Edit Page](wireframes/add_edit_page.png)

[Contact Us Page](wireframes/contact_us.png)

[Hike Detail Page](wireframes/detail_page.png)

[Login/register Page](wireframes/Login_register.png)

[User profile](wireframes/users_profile.png)


### Surface
The surface of the site should be clean and simple. As the content is all on one page it should not be overloaded with graphics and animations. Easy to follow and neutral colours as bright colours can come across alarming especially if there are many tasks appearing on the screen. 


## Features
### Existing Features
* Easy, simple design to allow for seamless navigation.
* Hike detail section to see key features of hike in bullet points.
* Ability to customize hike details and add any extra relevant information. 
* Hikes created by the user can be deleted using the delete hike button and added new hike using the “add new hike".
* The user can contact the site creator directly by email. EmailJS sends the designated email address to let them know about the query. A screenshot of the recieved image is here [Email correspondence]()
* Location is available through google maps API to compliment the key features of hike om details page.


### Features Left to Implement

* Adding a calender feature API to link with google calander so appointments automatically link to tasks. 
* Along with the calender, tasks could then be integrated with a time stamp so  the day could be better planned out i.e tasks could have an added time frame to have task completed by.
* For a mobile app, reminder notifications could also be installed to pop up if tasks were due to be completed at a certain time.
* An ability to add links to other apps. For example, if 10,000 steps was a task to be completed, there would be an option to link your FitBit account to allow for seamless and automatic task completion without having to manually check it off. 
## Technologies Used

1. CSS programming language
2. HTML programming language
3. Javascript Programming language.
4. [Materilize](https://materializecss.com/)
* To create a responsive structure for the website. 
5. [Balsamiq wireframes](https://balsamiq.com/wireframes/)
* used to create mock ups of what the site will look like
6. [Google Font](https://fonts.google.com/)
* Was used to style the fonts used in the website
7. [Gitpod](https://gitpod.io/workspaces/)
* To build and develop code
8. [w3schools](w3schools.com)
* To help with formatting and styles.
9. [Stackoverflow](https://stackoverflow.com/)
* The forums were useful for styling and functionality issues.
10. [HTML Formater](https://www.freeformatter.com/html-formatter.html#ad-output)
* To beatify HTML code
11. [W3C validator Service](https://validator.w3.org/#validate_by_input)
* To validate HTML code
12. [W3C CSS validator service](https://jigsaw.w3.org/css-validator/validator)
* To validate CSS code
13. [Python code validator](http://pep8online.com/))
* To validate Python code
14. [JQuery](https://jquery.com/)
* To add Javascript functionality
15. [Javascript Validator](https://jshint.com/)
* To validate Javascript code
16. [EmailJS](https://www.emailjs.com/)
* To facilitate email requests
17. [Google Maps API](https://developers.google.com/maps)
* To facilitate location functionality
18. [Jinga templating language](https://jinja.palletsprojects.com/en/3.0.x/)
* To help extend templates and iterate through objects. 
19. [Mongo DB](https://www.mongodb.com/)
* The database to store data 
## Testing

The HTML was checked using the [W3C validator Service](https://validator.w3.org/#validate_by_input).
The CSS was checked using the [W3C CSS validator service](https://jigsaw.w3.org/css-validator/validator).
The Javascript was checked using the [Javascript Validator](https://jshint.com/).
The Python was checked using the [Python code validator](http://pep8online.com/).


Manual testing was carried out to ensure the site carries out the intentions of the user stories.
On opening the page the category list is clear and visible and when a new category is typed into the form box a new category is created. Multiple categories can be created by continually adding to list.

A pointer cursor is evident when mouse hovers over categories prompting the user that they are clickable. Also the opacity lowers to highlight the category being hovered over to again prompt the item to be clicked.

The opacity also lowers when the user attempts to type in the new category form box to encourage the user to add a category.

When a category is selected the category font weight increases and stays in this highlighted state to signal to the user that this is the category selected.

When category is selected the corresponding task list appears. User is able to add to task list with form button as many times as they like.

User is also prompted to enter new tasks as opacity lowers again and the underline transitions.

When a task is completed it can be checked off and line goes through task item.

The task counter responds correctly to remaining tasks and the word task changes to plural tasks when a value of more than one is in the count. 

The progress bar responds correctly to remaining tasks.

The title of the task list changes to correspond with category selected.

The tasks can be unchecked by re-clicking the tasks.

The clear complete buttons clear any checked tasks.

The delete category button clears the highlighted category.

When page is refreshed all the information has been stored on local storage and is still available.

The project was also tested on multiple browsers (Chrome, Microsoft edge, Internet Explorer, and Firefox) and device sizes to ensure compatibility and responsiveness.

There is a message displayed directly after to acknowledge that the email has been sent.

#### Bugs
* The progress bar updates when the selected category is highlighted and works when tasks are checked and unchecked but when a new category is selected it doesnt auto update along with the task count. Once a task is checked or unchecked it updates, but not automatically. But managed to fix it as the varibale selectedList needed to be redefined. 
white space issue when putting hike description in edit hike area. solved with minus within jinga template
## Deployment

A repository was created on GitHub and Gitpod was used to write the code. The code was commited and pushed to Github regularly to ensure it was saved. The GitHub repository was then deployed to GitHub pages by:

1. Logging into GitHub
2. Selecting repositories and then MileStoneProject2_TaskTracker.
3. Then select settings from the top menu bar.
4. Under GitHub pages
5. Under source, select master branch.
6. The website is now deployed and a link appears for the deployed site.
7. This link can now be cloned and run locally.

## Credits
copied custom validation for the form from the tutuorial
### Content

### Media
#### Image
The source for the background images were from the following stories
* [Background Image 1](https://www.kevinandamanda.com/cliffs-of-moher/).
* [Background Image 2](https://www.irishcentral.com/uploads/article/46589/walking_hiking_ireland_getty.jpg?t=1605605516).
* [Background Image 3](https://img.theculturetrip.com/450x/smart/wp-content/uploads/2020/08/bjfmt0.jpg).
* [Background Image 4](https://thumbs-prod.si-cdn.com/Um3X9ygjd9CIgys35Klyfs4ECPU=/1072x500/filters:focal(1368x1212:1369x1213)/https://public-media.smithsonianjourneys.org/filer/30/7e/307e4fbf-dd84-42cd-8c8b-b0aeaefa1825/active_ire_hiker_dt_l_119992650.jpg).
* [Home icon Image 1](https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Fgeoffreymorrison%2Ffiles%2F2016%2F04%2F8-Scenic-Spots-Not-To-Miss-in-Ireland-by-Geoffrey-Morrison-1-of-12-1200x800.jpg).
* [Home icon Image 2](https://i.pinimg.com/550x/d2/10/f7/d210f7d908b62ba71589db2e7556b6d4.jpg).
* [Home icon Image 2](https://www.activeme.ie/wp-content/uploads/2016/09/Causaway-Coast-Scenic-Drive-Derry-to-Ballycastle-to-Belfast-Co-Antrim-Northern-Ireland-connects-to-Irelands-Wild-Atlantic-Way.jpg).



### Acknowledgements
I got inspiration for this project as I like to try and keep organised but tend to keep lists everywhere and don’t have them grouped into types and headings. Having one place to go for references and has all my tasks stored and broken down into smaller individually items is extremely handy. Also the progress bar is encouraging to get the list completed. 

Also my mentor, Brian Macharia for helping me along the way!
