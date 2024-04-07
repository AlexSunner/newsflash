# Newsflash

Newsflash is a Django-powered web application designed to provide users with access to a variety of posts on different topics. Users can browse through the homepage to view posts, and if they have registered accounts, they can log in to leave comments on the posts. Additionally, users have the option to sign up for a new account to gain access to additional features and personalize their experience on the platform.

The live link can be found here - <https://newsflash-42b6ce7a76e1.herokuapp.com/>

## Planning

### Before creating this project I visualized how I wanted the final product to be

- I wanted the project to be fully responsive for different devices, ensuring an optimal user experience whether viewed on a desktop, tablet, or mobile device.
- Additionally, I aimed to incorporate user registration functionality, allowing viewers to register accounts so they can comment on posts and engage with the content.
- Furthermore, I envisioned a contact page with a form through which viewers can send collaboration requests, adding an interactive element to the platform.
- Moreover, I envisioned the project as a dynamic news article website featuring posts covering a diverse range of categories, including Space news, Historical events, and Software development updates, to cater to a wide audience with varied interests.

![Responsive Mockup](https://github.com/AlexSunner/newsflash/blob/main/static/images/mockup.jpg?raw=true)

## Features

Here is a presentation of the different features added into Newsflash.

- __Collaboration Request Form__

    - A contact page with a form is available, allowing viewers to send collaboration requests, fostering interaction and engagement with the platform.

![Collaboration Form](https://github.com/AlexSunner/newsflash/blob/main/static/images/collaborate.jpg?raw=true)

- __Homepage__

    - The homepage showcases featured posts from various categories, including Space news, Historical events, and Software development updates. This allows users to easily discover and explore the latest and most relevant content right from the homepage.

![Homepage](https://github.com/AlexSunner/newsflash/blob/main/static/images/homepage-big.jpg?raw=true)

    - Also, this is how it looks on a mobile device.

![Homepage on iPhone](https://github.com/AlexSunner/newsflash/blob/main/static/images/homepage-small.jpg?raw=true)

- __Post Viewing and Comments with Full CRUD Functionality__

    - When users click on a post title from the homepage page, they are directed to a dedicated page displaying the full content of the selected post. This page includes details such as the post title, author, publication date, and the complete article content. Users can also view and contribute comments to engage in discussions about the post's topic.

![Post View](https://github.com/AlexSunner/newsflash/blob/main/static/images/post-big.jpg?raw=true)

    - Users who have commented on posts have the ability to edit or delete their comments. When viewing their own comments, users will see options to edit or delete each comment. Clicking on the "Edit" option allows users to modify the content of their comments, while selecting the "Delete" option prompts a confirmation message asking if they are sure they want to delete the comment. This confirmation step helps prevent accidental deletion of comments. After confirming the deletion, the comment is permanently removed from the post, and a success message confirms the action. Similarly, after editing a comment, the updated content is saved, and a success message is displayed to indicate that the modification was successful.

![Comments Displayed](https://github.com/AlexSunner/newsflash/blob/main/static/images/editdelete.jpg?raw=true)
![Comment confirmation](https://github.com/AlexSunner/newsflash/blob/main/static/images/deletemodal.jpg?raw=true)
![Comment edited or deleted successfully](https://github.com/AlexSunner/newsflash/blob/main/static/images/deletesuccess.jpg?raw=true)

- __User Registration__

    - Viewers have the ability to register accounts, enabling them to interact with the platform by commenting on posts and engaging with the content.

![Signup Page](https://github.com/AlexSunner/newsflash/blob/main/static/images/signup.jpg?raw=true)

- __Login Page__

    - The login page allows registered users to securely access their accounts by entering their username and password. Users can navigate to the login page from any part of the website by clicking on the "Login" link in the navigation bar. Once logged in, users gain access to additional features such as the ability to comment on posts.

![Login Page](https://github.com/AlexSunner/newsflash/blob/main/static/images/login.jpg?raw=true)

- __Logout Page__

    - The logout page allows authenticated users to securely log out of their accounts. When users navigate to the logout page or click the "Logout" link in the navigation bar, they are prompted with a confirmation message asking if they are sure they want to sign out. This additional step ensures that users don't accidentally log out of their accounts. Upon confirming the logout action, users are redirected to the homepage, and their active session is terminated.

![Logout Page](https://github.com/AlexSunner/newsflash/blob/main/static/images/logout.jpg?raw=true)

- __Category Custom Model__

    - The Category model organizes posts into different thematic categories, such as Space News, Historical Events, and Software Development. Each category consists of a name and a unique slug, allowing for easy navigation and filtering of posts based on specific topics. The Category model ensures efficient organization and accessibility of content, enhancing the user experience by providing a structured and intuitive browsing experience.
    - 

![Category](https://github.com/AlexSunner/newsflash/blob/main/static/images/category.jpg?raw=true)

- __Category Management in Django Admin__

    - The Django admin panel provides an intuitive interface for managing categories within the Newsflash project. Administrators can easily add, edit, and delete categories directly through the admin interface, streamlining the process of organizing and updating post categories. Upon accessing the admin panel, administrators can navigate to the Category section, where they have full control over the category data. They can add new categories by providing a name and a unique slug, edit existing categories to update their details, and delete categories that are no longer needed. This functionality empowers administrators to maintain a well-organized and up-to-date category structure, ensuring that posts are appropriately categorized and easily accessible to users.

![Category section for Admins](https://github.com/AlexSunner/newsflash/blob/main/static/images/admincategory.jpg?raw=true)

- __Administrative Control via Django Admin Panel__

    - The Newsflash project offers administrators extensive control and management capabilities through the Django admin panel. Administrators have the authority to add, edit, and delete categories, posts, users, and contact page details effortlessly using the intuitive admin interface. Additionally, they are able to read collaboration requests. Within the admin panel, administrators can navigate to specific sections dedicated to each entity, such as Categories, Posts, Users, Collaboration Requests, and Contact Page. From there, they can perform various actions such as adding new categories or posts, editing existing entries to update their details, and deleting outdated or redundant content. This comprehensive administrative functionality empowers administrators to maintain the project's integrity, manage user interactions, and oversee content creation and collaboration effectively from a centralized and user-friendly interface.

![Admin Panel](https://github.com/AlexSunner/newsflash/blob/main/static/images/adminpanel.jpg?raw=true)

- __Responsive Navigation Bar__

    - The Newsflash project incorporates a responsive navigation bar that seamlessly adapts to different screen sizes, ensuring optimal user experience across devices. On desktop and tablet devices, the navigation bar appears as a traditional horizontal menu, providing easy access to various sections of the website. However, on mobile devices, the navigation bar transforms into a convenient slide-down feature, conserving screen space while offering intuitive navigation options. This responsive design approach enhances usability and accessibility, allowing users to effortlessly explore the website's content regardless of the device they're using.

![Navigation Bar](https://github.com/AlexSunner/newsflash/blob/main/static/images/navbar-big.jpg?raw=true)
![Navigation Bar Mobile Device](https://github.com/AlexSunner/newsflash/blob/main/static/images/navbar-small.jpg?raw=true)

- __Social Media Integration in Footer__

    - The Newsflash project incorporates social media integration within the footer section, providing convenient access to various social media platforms such as Twitter, Youtube, Instagram, and Facebook. The footer includes clickable icons that direct users to the respective social media  pages when clicked. Additionally, to enhance user experience and ensure seamless navigation, each link opens in a new window, allowing users to explore social media content without leaving the website. This integration fosters engagement and connectivity, enabling users to stay updated with the latest news, announcements, and content across different social media platforms.

![Footer](https://github.com/AlexSunner/newsflash/blob/main/static/images/footer.jpg?raw=true)

## Testing

### Automated Testing
- Forms, models, and views passed all automated tests with `python3 manage.py test` command.

![Hello_news Forms Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/hello_news_test_forms.jpg?raw=true)

These are the tests I ran in the `forms.py` file in the `hello_news` app.

![Contact Forms Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/contact_test_forms.jpg?raw=true)

These are the tests I ran in the `forms.py` file in the `contact` app.

![Hello_news Views Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/hello_news_test_views1.jpg?raw=true)
![Hello_news Views Test 2](https://github.com/AlexSunner/newsflash/blob/main/static/images/hello_news_test_views2.jpg?raw=true)

These are the tests I ran in the `views.py` file in the `hello_news` app.

![Contact Views Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/contact_test_views.jpg?raw=true)

These are the tests I ran in the `views.py` file in the `contact` app.

![Hello_news Models Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/hello_news_test_models.jpg?raw=true)

These are the tests I ran in the `models.py` file in the `hello_news` app.

![Contact Models Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/contact_test_models.jpg?raw=true)

These are the tests I ran in the `models.py` file in the `contact` app.

![Run Test Command](https://github.com/AlexSunner/newsflash/blob/main/static/images/testOK.jpg?raw=true)

This is the outcome of every test with the `python3 manage.py test` command.


### HTML Validator
- Minor errors encountered in HTML validator for the signup page, potentionally caused by Django.
    - End tag p implied, but there were open elements.
        - This error indicates that the HTML parser encountered a closing `</p>` tag, but it expected to find an open `<p>` tag to close. This typically occurs when there are unclosed elements within the `<p>` tag.

    - Unclosed Span element
        - This error suggests that the `<span>` element was not properly closed. It indicates that there is an open `<span>` tag without a corresponding closing `</span>` tag.

    - Stray end Span tag
        - This error occurs when there is an unexpected closing `</span>` tag without a corresponding opening `<span>` tag. It indicates that the closing tag doesn't match any open elements.

    - No p element in scope but a p end tag seen
        - This error suggest that the HTML parser encounted a closing `</p>` tag, but there were no open `<p>` tags within its scope. This can happen when the closing `</p>` tag is misplaced or unnecessary.

### CSS Validator
- ALL CSS rules passed validation without any errors.

### JavaScript Validator (JSHint)
- No errors or warnings reported in the JSHint validator, indicating clean JavaScript code.

### Python Validator (CI Python Linter)
- `admin.py`, `forms.py`, `models.py`, `urls.py`, and `views.py` in the `hello_news` app passed the Python linter without any errors or warnings.

### Manual Testing
- Homepage
    - Manually verified that the homepage loads correctly without any errors.
    - Ensured that the posts are displayed on the homepage as expected.
    - Clicked on different posts to ensure they open correctly and displays the content accurately.

- User Authentication
    - Manually tested the user authentication functionality by attempting to log in with valid credentials.
    - Verified that the login form validates user input and displays appropriate error messages for incorrect credentials.
    - After successful login, verified that the user is redirected to the homepage.
    - Manually tested the logout functionality by clicking on the logout button and verifying that the user is logged out of the website.

- User Registration
    - Manually tested the user registration functionality by attempting to register a new account.
    - Filled out the registration form with valid user details and verified that the form submits successfully.
    - Checked for validation errors when providing invalid or incomplete information.
    - After successful registration, attempted to log in using the newly created account to ensure it works as expected.

- Commenting on Posts
    - Manually navigated to individual posts and verified that users can leave comments.
    - Tested the comment submission form by entering valid comment text and ensuring it is posted successfully.
    - Checked for validation errors when attempting to submit empty comments.
    - Verified that comments are displayed correctly under the respective posts.
    - Verified that the `comment count` was increased by 1 when submitting a comment.

- Contact Page
    - Manually tested the contact form by filling it out with valid information and submitting it.
    - Verified that the form submission triggers the intended action, such as sending a collaboration request.
    - Checked for validation errors when providing incomplete or invalid information in the contact form.
    - Ensured that users receive feedback messages confirming the success or failure of their form submissions.

- Responsive Design
    - Manually tested the responsiveness of the application by accessing it from different devices and screen sizes.
    - Verified that the layout and content adapt properly to different screen resolutions, including desktop, tablets and mobile devices.

- Navigation Bar and Footer
    - Manually tested the navigation links to ensure they lead to the correct pages.
    - Checked that the navigation menu is accessible and user-friendly on both desktop and mobile devices.
    - Verify that internal and external links open in the same or new tabs as intended.

- Admin Panel
    - Manually accessed the Django Admin Panel and verified that administrators can add, edit and delete categories, posts, users, collaboration requests, and contact page content.
    - Manually tested the functionality of different admin panel features.

## User Stories
I created a Kanban board on [GitHub](https://github.com/) in order to keep track of my User Stories and its progression.
It provides a visual representation of my tasks, making it easier to manage and prioritize them effectively.
The Kanban board can be found here - [USER STORIES](https://github.com/users/AlexSunner/projects/2)

### Here are some examples of these User Stories
- As a user, I can click on posts, so that I can read the full content.
    - 1 Acceptance Criteria: When a post is clicked on, a detailed view of the post is seen.

- As a registered user, I want to be able to edit and delete my comments, so that I can manage my contributions effectively.
    - 1 Acceptance Criteria: Registered Users should be able to select options to edit and delete their comments when viewing the comment section.
    - 2 Acceptance Criteria: When editing a comment, users should be able to modify the content.
    - 3 Acceptance Criteria: Deleted comments should be removed from the comment thread and not visible to other users.
    - 4 Acceptance Criteria: Users should receive a confirmation prompt before permanently deleting a comment.

- As a admin, I want to be able to select what category the post belongs to, so that I can have all the posts divided into groups with the same subjects.
    - 1 Acceptance Criteria: The admin should be able to select which category he wants to put the post into.

## Deployment
The Newsflash project is deployed on Heroku, providing a convenient way for users to access and enjoy the application.
Despite the deployment being on Heroku, the project's source code is managed and stored on GitHub.
[Newsflash](https://newsflash-42b6ce7a76e1.herokuapp.com/)
[Source Code](https://github.com/AlexSunner/newsflash)

### Deploying to Heroku
1. Log into Heroku website.
2. From the Dashboard page, select "New" and then "Create new app."
3. Assign a name for the application, select the region and then select "Create app."
4. Once the application is created, from the submenu at the top, select "Settings" and then "Reveal Config Vars" to set up config vars.
5. In the KEY input field, enter "PORT" all in capitals and enter "8000" for the VALUE input field and select "Add." If there are other config vars required to run the application, add those here. For this application, there is no other config var required.
6. Scroll down to the "Buildpacks" section and select "Add buildpack."
7. Add buildpacks required to run the application. For this application, "Python" and "Nodejs" are required.
The order of the buildpacks is important. "Python" should be the first and then "Nodejs." If they are not in the correct order, click and drag to change.
8. Select "Deploy" from the submenu at the top.
Under the "Deployment method" section, select "GitHub" to connect to GitHub.
Under the "Connect to GitHub" section, enter the name of the repository and select "Search."
Once the repository is located, select "Connect" to connect the repository to the application within Heroku.
9. Select either "Enable Automatic Deploys" which will deploy a new version of the application every time changes are pushed to GitHub or opt for "Manual Deploy." For this application, "Automatic Deploys" was selected.
10. Once the application is deployed, scroll back to the top of the screen and select "Open app."
If "Enable Automatic Deploys" has been selected, the application will be built and available after the next changes are pushed to GitHub.

### Forking the GitHub Repository
If you want to make changes to your repository without affecting it, you can make a copy of it by 'Forking' it. This ensures your original repository remains unchanged.

1. Find the relevant GitHub repository
2. In the top right corner of the page, click the Fork button (under your account)
3. Your repository has now been 'Forked' and you have a copy to work on

### Cloning the GitHub Repository

Cloning your repository will allow you to download a local version of the repository to be worked on. Cloning can also be a great way to backup your work.

1. Find the relevant GitHub repository
2. Press the arrow on the Code button
3. Copy the link that is shown in the drop-down
4. Now open Codeanywhere or whatever editor you use & select the directory location where you would like the clone created
5. In the terminal type 'git clone' & then paste the link you copied in GitHub
6. Press enter and your local clone will be created.

## Technologies used

### Frontend Technologies
- HTML, CSS, JavaScript
    - Power the frontend of the project, providing a rich and interactive user interface.

### Backend Technologies
- Python
    - Used for server-side logic and backend development.
- Django Framework
    - Facilitates efficient data management, routing, and web development.

### Django Packages
- django-allauth
    - Enables user authentication and account management.
- django-crispy-forms
    - Renders forms with elegant styling and layout control.
- django-summernote
    - Provides rich text editing capabilities within the Django admin interface.

### Server and Deployment
- Gunicorn
    - Acts as the WSGI HTTP server for running Django applications in production environments.

### Database Management
- [ElephantSQL](https://www.elephantsql.com/)
    - Utilized as a PostgreSQL database service for efficient and scalable data storage.

### Additional Python Packages
- asgiref
    - Provides ASGI specification reference implementation.
- psycopg2
    - PostgreSQL adapter for Python, facilitating database connectivity.
- sqlparse
    - Helps parse SQL statements into tokens.
- whitenoise
    - Simplifies serving of static files in Django applications.

### Other Technologies used
- [GitHub](https://github.com/) - Storing Source Code
- [HTML Validator](https://validator.w3.org/) - Validating HTML code
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - Validating CSS code
- [JavaScript Validator](https://jshint.com/) - Validating JavaScript code
- [Python Validator](https://pep8ci.herokuapp.com/) - Validating Python code
- [Google Translate](https://translate.google.se/?hl=sv) - Used as a translator
- [Google Search Engine](https://www.google.com/) - Searching for answers
- [Lucidchart](https://lucidchart.com/) - Creating a basic flowchart
- [GitPod](https://gitpod.io/) - The IDE used to create the project
- [PlaceIt](https://placeit.com/) - Used to create the mockup

## Credits

### Code|Star Walkthrough Project
- Much of the HTML, CSS and Django code in this project is inspired by and adapted from the Code|Star walkthrough project, which provided valuable guidance and insights into web development best practices. Features such as the Navigation bar, the homepage, the footer, the contact page, the post details,the comment section, signup and registation page was very much from the Code|Star project.

### Media
- The background image was taken from [MrWallPaper](https://mrwallpaper.com/)

### Readme
- The content of my README drew inspiration from my previous README for the [Memoree](https://github.com/AlexSunner/memoree/blob/main/README.md) project.