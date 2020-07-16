 # Recipe Pouch

My website is a simple and easy to use recipe storage page where the user can view existing recipes and more importantly create new recipe, edit existing recipes and delete old or unneeded recipes. It holds a very simple design consisting of the site name located at the top and the list of recipes that have been added. The creation and edit pages are also following the simple theme as they contain a spread out and easy to understand form where the user can do whatever they need to do whenever they need it . The page contains no images or animations as I intend for the page to be one where you need to just pop on and have a quick reminder of ingredients or just to follow the baking method with no distractions or clutter filling the screen. 


## UX

When designing my website i had decided to create to target (but not limited to) an elderly audience. With this in mind I tried to create a design that was very simple and unintimidating to use with minimal amounts of clutter and anything that may be potentially confusing or not vital to the websites functionality. The idea was to have as little buttons and accessories as possible to enable easy access to the users recipes they may have stored at any time or place. I also included various retail store shopping links in the footer of every page. The idea of this is to enable the user to click on these links and be redirected to an external shopping site where they can compare prices and get baking ingredients. 

The objective of this website is to enable the user to quickly and easily find,create,edit and delete any recipe they may have added to wanted to add. I have also made the design responsive so the user will have the ability to view thier recipe book on their mobile, tablet or pc at any time. This creates a new level of accessibility as this means no matter what situation/environment youre in you can always access the storge and tweak what you want.

I believe that my project is the ideal way to help the user achieve their goal of the website because i have implemented all of the core aspects of data manipulation in a very simple manner via the use of clear labeled buttons throughout the page to try and make the actions of each button as clear as possible. The user can create a new data entry with the click of a button and by filling in a nice and tidy form clearly laying out what input field does what. The user can also edit any stored data by clicking on the 'Edit recipe' button at any time and once again very easily find and alter their desired piece of data. And finally the user can also simply remove any data collection with the click of a button labeled 'delete' with a handy bin icon to further clarify the buttons outcome. 

## User Stories

As an elderly lady, I want to be able to go on my phone and double check the cooking method of my homemade trifle as I sometimes get forgetful. So i would need to open up the website and have a quick scroll through the list of recipes i have created so i can retrieve my recipe and make my trifle without fear of getting it wrong.

As a person in my 20's, I want to update one of my cheesecake recipes as i have found a newer and better version of it online which sounds much nicer. To do this i would need to hop on to the website and find the cheesecake recipe witha simple scroll down the page and once I have found it I will need to click the edit button and change any data that needs updating leaving the correct recipe on the home page ready for when i need it.

As a busy worker, I have very little time to make loads of different and time consuming recipes so i need to delete any recipes i won't have the time to make after work which will make finding the recipes i actually want to make a lot easier. For this all I would need to do is find the desired recipe and press the delete button.


## Features

### Existing features

My project hosts a rather simple and accessible style therefor there are not a whole load of dynamic features to overload the target user with. 

* My first feature on my page is the logo. When clicked, this allows the user to navigate back to the home page where a list of the recipes can be found. 

* My second feature is the 'Add recipes' button. This allows the users to create new data entries by having the user fill out the required form.

* My third feature is the 'Edit recipes' button. This allows the users to alter existing data entries by having the user fill out the required form.

* My fourth feature is the 'Delete' button. When clicked, this allows the user to completely remove existing data entries.

* My fifth feature is the accordion format of the ingredients and method sections. This allows the user to have a clear overview of all the recipies on the home page however when the dropdown is triggered it will expand and display the desired information.

* My sixth feature is the footer containign shopping site links, This allows the user to check various poplar retail store stocks to see where they can get the cheapest ingredients if they need some. 

### Future feature implementations

* The first feature i want to add is the use of an account system. Having this in my website will drastically improve its usability as at this present time anyone can access the page and change a recipe at will. With the use of the account system, the experience will be a lot more personalised and better suited to the websites intention. The reason i did not include this feature is purely downt o lack of knowledge. I had a go at trying to implement it but after a couple of days i was running out of time to complete the website.

* The second feature i would like to add is a chat section where any user can join with an account and start chatting and interacting with other people on the page. This would also improve the websites user experience as it will enable people to talk and share recipes and cooking tips. 

* Thirdly, I would also be intersted in adding some sort of validation system where it will prevent users from creating meaningless spam entries clogging up the databases used to store the data. 

## Technologies Used

* [Materialize] (https://materializecss.com/)
  * I utilised the materialize css library in order to create my layot using the grid system and and majority of the other components such as the buttons with icon and the accordion i used as a dropdown inside my recipe cards. 

* [MongoDB] (https://www.mongodb.com/)
  * I Utilised MongoDB as my storage database as i felt it was well suited for my website and i had the most knowledge with at the time.

* [Python] 
  * I used the python language to construct my app with the use of Flask and Py-Mongo together. 
 
* [JavaScript] 
  * I used JavaScript to create a document ready function which enabled my accordions and forms on my website. 

## Testing

Throughout the development process I was testing how my website was being effected by any alterations I made in my code such as positioning and sizes. I did this by running the website in a separate browser tab and using the inspect function. Through this function I was consistently playing around with different sizes, colors and layouts as I could make any changes I wanted without effecting the actually code. This enabled me to pick up on silly mistakes I made like some elements not being responsive on the smallest resolutions. I was also able to pre plan what colors and sizes I wanted to implement without wasting any time on a gamble whether it would work or not. Using the inspect function also reduced the chance for errors because I was already able to see the end result before I added it to the real code. Also when i was testing the website myself I was constantly checking to make sure that all of my app.py functions were function correctly such as edit add and delete buttons.

* I tested my Add and Edit recipe page by doing the following:
  * Clicking on the 'Add/Edit recipe' button
  * Trying to submit an empty form and making sure the required fields text works
  * Trying to submit a form with letters in the servings input field and making sure it asks specifically for a number input
  * Trying to submit a valid form entry and insuring it appears on the recipe page


* I tested my Delete button by doing the following:
  * Clicking on 'Delete recipe' 
  * Making sure that the data entry was successfully deleted from the website and the database on MongoDB
  
  
I also used a code validator website (https://validator.w3.org/) for both my CSS and HTML files throughout the development process. By using this website I was able to keep track of the code I was writing and any mistakes would be flagged up there and then which made rectifying them much easier as oppose to waiting until the end of my project then fixes every error I had made.

Another method of testing I used was sending my website out to other people. I sent the server port link out to a few of my family and friends and ask them to have a play around with the site including but not limited to the navigation features or forms I had. After they had a go with the site I then asked them to give me some feedback on what was good, what's was bad and what could be improved. Because of the target user i had chosen I also decided it would have been a good idea to let my grandparents have a go with my website at various stages of my production and see what they thought about the styles, readability and simplicity of the general website. This allowed me to hone in on specififc features that I would maybe not know was an issue for older people. 

My website also adapts to different screen sizes and resolutions in a way that as the screen gets smaller the layout will change by shifting around the elements to hold a similar style while also being professional and functional. I have developed my website to be responsive as a whole in which I mean that as you switch resolutions to medium or small resolutions the whole page will stay very similar until you cross certain resolution checkpoints. For example, I have each of my recipe card data entries presented as a col 6 following the grid layout system featured on materialize. From what I have experience with other websites over the years and through the feedback I have been given this layout would work well with modern day internet styles. It makes each item easy to view and makes them all stand out due to them covering the entire width of the screen.

When i was testing my MonogDB connection and and app.py connection i had several issues and problems throughout. Most of these were consisting of typos or spelling errors which caused the connections to be faulty. I also had a couple of problems trying to store my MongoDB URI and password as a environmental variable and adding it to a gitignore file. I eventually overcame this with the guidance of a few tutorials and eventually found out that i had a typo in the env.py file I made causing an internal server error 500. 


## Deployment

* Deploying to github

  * My first step when deploying to github was creating my app.py file and getting the basic functionality in place so I could insure that my page connections were working smoothly. 
  
  * Then, in the terminal window I typed 'git add .' to add all of my intial files to the stagin area.
  
  * Then, also in the terminal window I typed 'git commit -m "Initial commit"' outlining the what i was i had done between commits. 
  
  * Finally, I typed 'git push' which pushed my commits to github where it was stored ready for future commits.
  
* Deploying to heroku

  * My first step in deploying my website to Heroku was creating an account to host my project on the Heroku website.
  
  * Then, I needed to navigate to the 'new' button which then gave me the option to create a new app. When choosing the name for my app I attempted to make the name as close to the project theme as possible so I chose to name it 'Recipe-storages'
  
  * After creating a new app i was ready to deploy my initial commits to Heroku. I did this by navigating to the deploy page and clicking on the Github account linking button. I chose to use this method as oppose to using the Herkou CLI and pushing to the master branch every time. It just made everything simpler and more organised.
  
  * Once my Github and Heroku accounts were linked i needed to input the correct PORT and IP figures i used in my app.py file which were PORT:0,0,0,0 and IP:5000. To do this I went on the settings page on Heroku and revealed the config vars for my app. This is where i input my figures for the port and ip as well as my Mongodb URI and Name which was used to make sure my database would connect to the Heroku app. 


This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Credits
Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X
