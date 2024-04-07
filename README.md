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

![Contact Forms Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/contact_test_forms.jpg?raw=true)

![Hello_news Views Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/hello_news_test_views1.jpg?raw=true)
![Hello_news Views Test 2](https://github.com/AlexSunner/newsflash/blob/main/static/images/hello_news_test_views2.jpg?raw=true)

![Contact Views Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/contact_test_views.jpg?raw=true)

![Hello_news Models Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/hello_news_test_models.jpg?raw=true)

![Contact Models Test](https://github.com/AlexSunner/newsflash/blob/main/static/images/contact_test_models.jpg?raw=true)

![Run Test Command]()

![Views Test 3]

## HTML Validator
- Minor errors encountered in HTML validator for the signup page, potentionally caused by Django.

## CSS Validator
- ALL CSS rules passed validation without any errors.

## JavaScript Validator (JSHint)
- No errors or warnings reported in the JSHint validator, indicating clean JavaScript code.

## Python Validator (CI Python Linter)
- `admin.py`, `forms.py`, `models.py`, `urls.py`, and `views.py` in the `hello_news` app passed the Python linter without any errors or warnings.
