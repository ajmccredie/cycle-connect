# cycle-connect
![Logo](static/README-images/cc-logo-blue-text.png)

A mini-social-networking site for cycling enthusiasts to build and enjoy their community of riders.
A link to the deployed project can be found here https://cycle-connect-70cef323855a.herokuapp.com

<images of the deployed site across different devices>

## Problem statement
To address the need for a website to connect fellow cyclists, allowing them to share experiences and find helpful information to improve their cycling journey. Cyclists need a website that allows the creation of a secure personal profile, a place to discuss bike maintenance and other cycling related topics, discover new cycling routes, plan and join group rides, buy and sell bikes and cycling related items, and book cycling related services easily. 
This website should help all users to feel like they are part of a friendly cycling community, keeping them motivated and informated for their cycling adventures.

## Initial proposed database structure to meet the problem statement
![Database structure plan](static/README-images/database-model-miro.png)

### Explanation of the data relationships:
Each user can create multiple posts, and each post belongs to one user (one-to-many relationship between Users and Posts).
Users can have multiple bikes for sale, and each bike belongs to one user (one-to-many relationship between Users and Bikes).
Users can make multiple bookings for services, and each booking belongs to one user (one-to-many relationship between Users and Bookings).
GroupCycles are organised by users, and users can participate in multiple group cycles (one-to-many relationship between Users and GroupCycles, many-to-many relationship between GroupCycles and Users through the Participants table).


## Design and development of themes and project as a whole
### Initial ideas
The site needed to feel clean and professional, preferably making use of motivational cycling images in the background. 
Information needed to be easy to find and the site easy to navigate. 
Themes of outdoor adventure were used from the outset and the logo design.

### Wireframes and initial mock-ups
| Titles |  |  |
| ------ | ----- | ------ |
| Wireframes of layout for sign in and rides | ![Wireframe for sign in layout](static/README-images/wireframe-signup.png) | ![Wireframe for rides layout](static/README-images/wireframe-rides.png) |
| Concept art login | ![Phone concept art login](static/README-images/concept-phone-login.png) | ![PC concept art login](static/README-images/concept-pc-login.png) |
| Concept art sign-up | ![Phone concept art signup](static/README-images/concept-phone-signup.png) | ![PC concept art signup](static/README-images/concept-pc-signup.png) |
| Concept art Ts and Cs/ forum entry | ![Phone concept art Ts and Cs and forum entry](static/README-images/concept-phone-tcs-forum.png) | ![PC concept art Ts and Cs and forum entry](static/README-images/concept-pc-tcs-forum.png) |

### Colour schemes and background images
The site colour palette:
1. **Primary Colour - RGB(111, 111, 188):** This is a soft muted blue. It provides the backdrop for all pages and is used as the image overlay for all background images.
2. **Accent Colour - RGBE(255, 221, 85, 0.7):** This is a semi-transparent golden-yellow to provide a strong contrast and draw the users attention to buttons and key navigational elements.
3. **White and Black:** These are used for text and borders and some background elements to ensure good readability.
4. **Warnings and Status Indicators:** These are in clear colours such as red, green, orange and yellow to give intuitive indication to the users.

A selection of background images were obtained from Freepik (references below). These were recoloured in PowerPoint to keep with the themes and colours decided. 
The navbar and footer were styled in dark colours with a consistent logo in the top left and the menu (changing to drop down on smaller screens) in the right. Social media links were placed in the footer.
The `background-attachment: fixed` property gives a parallax-like effect, adding depth to the pages.

### Typography
- **Primary Font - 'Dosis', sans-serif:** Used for most textual content of the site. This font has modern, clean lines.
- **Secondary Font - 'Kanit', sans-serif:** Used for headings, navigation, and certain buttons. This provides a subtle contrast to the main body text while maintaining overall harmony.

### Common themes and navigation
Each app has a different background image (although the colours feel the same). Each of these background images behaves the same way. The buttons and links throughout the site are styled in a similar manner (with the same colours and hover functions), and any pop-up modals used match. This is all with the aim to promote a positive UX throughout the site. 

## Division of the Django project into specific 'Apps'
From the database structure, the apps were decided and worked on individually. The initial minimum viable product set up was to ensure that users could sign-up with a mini-profile and then be able to write, update and delete posts on the user forum, and read and like the posts of others. 

The site was then developed further to incorporate services and bookings, marketplace, and social rides apps. A separate small app was created for adding a terms and conditions page.

### Profile and profile services
#### Purpose
A first time user can easily sign-up to the site and immediately feel involved.

#### UX/UI key features
| Feature | Image | Description |
| ---- | ---- | ---- |
| Login screen | ![Login screen](static/README-images/general-1-signin.png) | Clear layout where existing users can sign-in and new users can click to sign-up. |
| Initial sign-up screen | ![Basic sign-up screen](static/README-images/general-2-createaccount.png) | The site only requires a username and a password (entered twice). |
| Ts and Cs | <image> | A very basic user agreement is generated for the user to sign. The user is unable to access any other features until this is done using Django Middleware. Admin has a list of the users who have agreed to the terms. |
| Detailed profile form | ![Detailed profile sign-up and edit form](static/README-images/profile-2-edit.png) | A first time user can feel involved with the site from the outset as they are invited to share a bit about their cycling background. They can also skip the form and go straight into the site if they wish, accommodating for users who might want to do this later, or simply are not interested in this piece of functionality. The profile pictures are used for the trading conversations part of the site and the top right corner to show the user is logged in. The form has one longer input field, some radio buttons and a thumbnail display of any uploaded images for the user to check their inputs.|
| Profile details view | ![Profile view screen](static/README-images/profile-1-view.png) | The user can see their profile at any time by clicking on the profile link or their profile picture in the top right hand corner of any logged in page. This profile is currently private to the user (aside from the profile picture), but there is room to add future functionality here in sharing profiles, cross-referencing skills to social ride sign-ups and even targeting discussions regarding maintenance. |

#### Tests (full details in separate documentation)

### Main user forum
#### Purpose
The main userforum is where the cyclists can bring up and discuss any topics of their choosing, including bike types, interesting cycle routes and upcoming races/events. 

The page is self-monitoring and users can report posts that go against community standards. The decision was taken not to require admin approval to post on this page in order to allow the site users to be immediately involved in discussions and posts.

#### UX/UI key features
| Feature | Image | Description |
| ---- | ---- | ---- |
| Forum welcome and main page | ![Forum main page](static/README-images/forum-1-welcome.png)  | The forum is designed to be dynamic and interactive. Users can add posts straight from the page and see them instantly appear below. Posts are organised from newest to oldest. The input field allows rich text input, as well as images and links. Additionally there is a built-in spell check for English, so users can check the content of their message before they post it. |
| Forum main page - posts and pagination | ![Forum main page posts](static/README-images/forum-2-posts.png) | Users can interact with other posts on the page using the ‘like’ button. They can also see how many comments there already are for any particular post and can then open a new page for each post to view the comments and add their own if they wish. There is a limit to the number of posts displayed on the pages to prevent information overload. |
| Post editing | ![Forum post edits](static/README-images/forum-3-postedit.png) | Any post made by the user can be edited, this form also checks for valid inputs. Users can navigate away from this page without making changes if they wish. |
| Post deletion | ![Forum post delete check](static/README-images/forum-4-postdelete.png) | Users can choose to delete their own posts at will, and this page confirms this is the intended action. Deleted posts are removed from the database, along with any associated comments. |
| Commenting on posts | ![Forum post comments](static/README-images/forum-5-comments.png) | Users can comment on the posts of others join the discussion of a post in this thread. The posts are displayed with the comments. Users are able to edit their own comments if required. |
| Deleting comments on posts | ![Delete comment confirmation](static/README-images/forum-7-commentdelete.png) | Users can delete their own comments if they wish. A similar confirmation of action is required to the main forum post deletion. Deleted comments are also removed from the database. |
| Post reporting verification | ![Forum reporting of posts](static/README-images/forum-8-reportcheck.png) | Users who report posts using the 'report' button are required to verify this action, because it will remove the post from the forum, alongside all associated comments. It does not cause deletion of the post, so admin can reinstate the post if it was done in error. |
| Reported post notification | ![Forum reported post](static/README-images/forum-9-reportedpost.png) | The author of a reported post receives a warning on their post, which they are still able to see. It provides the option to contact admin if they believe it was reported in error. This prevents user confusion of their post simply vanishing. |


#### Tests (full details in separate documentation)

### User Market
#### Purpose
The market (or 'trading') app exists within the site to allow users to buy and sell specific cycling related items. It is not mandatory to add a price, because some users may simply wish to exchange items. Users can filter items by a few categories and their condition.

#### UX/UI key features
| Feature | Image | Description |
| ---- | ---- | ---- |
| Marketplace main page | ![Marketplace main page](static/README-images/trading-1-welcome.png) | For sale items are listed from newest to oldest and there are filters to help find what they may be looking for. There is no 'search' function other than the filters. Items for sale are clearly marked as 'available', which automatically toggles to 'sold' once the seller clicks the button to mark the item as sold. Images and descriptions of the items are presented in a clear and consistent manner. A place-holder image is used if the user does not upload an image. This is to encourage them to use a more meaningful image of their own. |
| Add item form | ![Marketplace add item form](static/README-images/trading-2-form.png) | Users can add items using a simple, quick form. They have the option to mark the item as 'sold' from the outset, because they might be looking to show the sorts of items they have previously sold (although it is unlikely that many will want to do this). The form has defaults for the item type button, but not the condition. It is important that the user gives the condition some thought and the form will not validate until the enter an input. Users can see a thumbnail of the image they are uploading. They have the ability to navigate back to the Marketplace main page without adding and item if they wish. |
| Confirmation of item submission | ![Marketplace confirmation](static/README-images/trading-3-thankyou.png) | In order to align with the user story for admin being able to oversee the activity on the marketplace, and to verify the items being sold are appropriate for the site, items need to be verified. This is briefly explained to the user when they add an item for sale using a pop-up modal. |
| Post pending admin verification | ![Marketplace pending post](static/README-images/trading-4-pendingpost.png) | The added posts are marked as pending for the author, but other users are unable to see the marketplace posts until they are verified by the admin. The pending posts are clearly marked with indicators, which are removed when the post is verified. |
| Edit their own post | ![Marketplace edit post](static/README-images/trading-5-edit.png) | Users can xxx |



#### Tests (full details in separate documentation)

### Bookable company services
#### Purpose
This part of the site links to the company providing the site, allowing for services to be booked for more local riders. This section of the site is not necessarily intended for all of the users.

#### UX/UI key features
| Feature | Image | Description |
| ---- | ---- | ---- |
|  |  |  |

#### Tests (full details in separate documentation)

### Group Cycles
#### Purpose
Users can view rides which have been planned or added by themselves or other users (or admin). They can sign up to upcoming rides and receive a running total of the rides they have attended. Uploaded images need to be sourced from other places and saved to be uploaded here.

#### UX/UI key features
| Feature | Image | Description |
| ---- | ---- | ---- |
|  |  |  |

#### Tests (full details in separate documentation)


## Agile project planning and methodology
Initial collection of user stories were made, categorised for 'must', 'should' and 'could' and then used in conjunction with GitHub Projects.
Meeting the user stories was then planned with a series of goals, and then split down further into sprints. The proposed sprints were then met fully or partially, and any incomplete work was reassessed as to its value and where it should be placed.

| User story | Must/should/ could | Database section | Time-box allocation/ Story points |
| ----------- | ----------- | ----------- | ----------- |
| As a **site admin**, I can **manage user accounts and profiles** so that **I can ensure the platform’s security and integrity**.      | Must | Userprofile, Forum, Trading | 8-13 |
| As a **site user**, I can **create, view, and update my profile** so that **I can share my cycling interests and connect with other riders.** | Must | Userprofile | 5 |
| As a **site admin**, I can **check and verify the content of posts** so that **the community standards can be upheld, and no misleading or offensive information is published.** | Should. Was reviewed in development and altered to the ability to report posts and have them removed pending review. This keeps the feel of the forum more dynamic. | Userprofile | 2 |
| As a **site user**, I can **post maintenance tips and tricks** so that **I can help fellow cyclists with their cycle maintenance.** | Must | Forum | 3 |
| As a **site user**, I can **post to ask the advice of others in the community** so that **my cycling can improve.** | Must | Forum | 3 |
| As a **site user**, I can **like the posts of others** so that **I can encourage them in the cycling community and feel involved.** | Should | Forum | 2 |
| As a **site user**, I can **comment on the posts of others** so that **I can feel involved in the conversation.** | Should | Forum | 3 |
| As a **site user**, I can **post some of my favourite route suggestions** so that **I can help inspire my fellow cyclists.** | Should | Forum (these are just suggestions rather than planning group rides) | 5 (to include the ability to search for the routes) |
| As a **site user**, I can **list bikes and components for sale** so that **I can find buyers for my items or purchase what I need.** | Must | Trading | 5 |
| As a **site admin**, I can **monitor and support the marketplace listings** so that **users can buy and sell items without issues.** | Must | Trading | 3 |
| As a **site user**, I can **immediately show if an item I had listed for sale is no longer available** so that **I do not waste the time of other users who would otherwise have liked to purchase the item.** | Should | Trading | 2 |
| (As a **site user**, I can **approach the sellers of bikes and components for sale** so that **I can find items or purchase what I need.**) | Must (but added in the sprint) | Trading | 5 |
| As a **site user**, I can **easily upload images for marketplace items** so that **I can generate more interest in the item.** | Could | Trading | 2 |
| As a **site user**, I can **make, check, and amend bookings for cycling-related services** so that **I can get the support I need for my cycling.** | Must | Bookings and Services | 8 |
| As a **site admin**, I can **handle user inquiries and issues related to service bookings** so that **users have a smooth experience.** | Must | Bookings and Services | 5 |
| As a **site user** I can **see the status of my booking requests** so that **I can be reassured of progress** | Should | Bookings and Services | 3 |
| As a **site admin**, I can **create, read, update, and delete the general services offered** so that **the information is up-to-date and correct, and bookings can be made.** | Should | Bookings and Services | 3 |
| As a **site user**, I can **plan and join group rides** so that **I can enjoy cycling with others.** | Must | Social Rides | 8 |
| As a **site admin**, I can **approve and manage group cycling events** so that **I can facilitate safe and organized rides.** | Must | Social Rides | 5 |
| As a **site user**, I can **view and RSVP to upcoming group cycling events** so that **I can participate in local rides.** | Must | Social Rides | 3 |
| As a **site user**, I can **earn badges or achievements based on my cycling milestones** so that **I can visualize and share my cycling experience.** | Could | Social Rides | 3 |
| As a **site admin**, I can **host virtual cycling challenges or competitions** so that **users can compete and stay engaged.** | Could | Social Rides/ Forum | 3 |
| As a **site user/admin**, I can **send invites to join the platform through text and emails** so that **the community can grow more quickly.** | Could | Userprofile | 8 |

The data relationship model was prepared and verified prior to the sprints.

### Sprint 1: Objectives - 
Getting a minimum viable product (MVP) in place: users can sign-up, set up an account, login, logout and use the forum. Within the forum users have full 'CRUD' (Create, Read, Update and Delete) capabilities of their own posts and add images. Admin can oversee the forum activity. Create test groups and user profiles to use on the site. Deploy to Heroku.
#### Definition of done for Sprint 1: 
A MVP site deployed to Heroku with full CRUD capability in the forum.
#### Break down of work goals to meet objectives and the user stories at the top of the table (not the optional ones at the bottom):
Goal 1: Set-up the project on GitHub and transfer user stories into Kanban Projects board in GitHub. Move the essential user stories relating to profile and forum into the 'Working on' column.
Goal 2: Set-up the Django project for the site (as per the CodeStar Blog walkthough), set-up a superuser, and check admin access. 
Goal 3: Initial deployment and set-up in Heroku
Goal 4: Set-up apps and database for the user account/profile.
Goal 5: Design wire frames and concept art for site
Goal 6: Create tests for minimum functionality (create, view, update and delete accounts, create, view, update and delete posts on the forum, including images)
Goal 7: Create html and css for login and basic account set-up (adaptation of existing forms for sign-up to accept additional profile information). Use of crispy-forms? There will be button use and toggle similar to Hello Django. Consider multiple choice buttons as well as free text input for fields.
Goal 8: Set-up the app and models for the data in main user forum. This will take a similar form and structure initially to CodeStar blog.
Goal 9: Link up html and css to the forum
Goal 10: Check the link up and the admin capabilities
*Goal 11: Set-up user likes for posts on the forum
*Goal 12: Add commenting ability and CRUD capability to comments
Goal 13: Deploy MVP site to Heroku
Goal 14: Full-testing of key-feature behaviour to check capability
Goal 15: Create user groups and profiles.
<br>

#### Analysis of the sprint (lessons learned):
The initial time-boxing points were not very accurate, and many of these goals took a disproportionate amount of time to complete. This sprint took far longer than intended to reach the MVP and therefore to meet the Definition of Done. 
Lessons were learned due to the overly ambitious nature and not fully understanding  many of the Django features. The Userforum was mainly based on walk-through code, which I thought would have been easier to have customised for my requirements. Initially many lessons were learned about how to better interpret the Debug error messages and how to solve issues of getting templates, urls, views, models, forms and admin files to all work effectively together. The first sprint took around double the amount of time which had been predicted from previous experience, but the majority of the planned work was necessary to complete in order to make a Minimum Viable Product (and therefore meet the Definition of Done for that sprint).
Testing found some bugs, some of which required immmediate tackling. Some ideas to improve UX/UI were identified and listed to be potentially added to future sprint backlogs (in order of importance):
- Fully consistent application of CSS on pages
- Pagination of posts
- Admin verification of posts
- Categorisation or search function for posts
- Thumbnails of images in profiles
- JavaScript feedback messages confirming user actions
- Feedback to user regarding upload image size

### Sprint 2: Objectives - 
Add ability for users to view the services available for booking, make appropriate bookings and cancel bookings. Admin must be able to set the services up in the admin panel in a straightforward manner, and must confirm bookings for the users. It is important that service slots cannot be double booked, and take into account where the set-up or collection and returns of bikes are intended for on each day.
#### Definition of done for Sprint 2: 
A bookings system for services offered with full CRUD capability for both site admin and user.
#### Break down of goals meet objectives and the user stories regarding bookings and services:
Goal 1: Set up the app for the additional services offered
Goal 2: Design the page and information flow structure
Goal 3: Create a list of tests for the app to pass for this sprint to meet the definition of done
Goal 4: Create models
Goal 5: Create forms
Goal 6: Allow for admin to mark when particular things are available for booking
Goal 7: Link the mobile service details to the admin calendar
Goal 8: Make and link up all the html template pages and view
Goal 9: Write the css and the js
Goal 10: Produce specific enquiries forms and fill in all the details (bikes and pedibus details – lift from cycool site, including images)
*Goal 11: Link enquiry forms up to email service and test X NO EMAIL FORM – add to ‘nice to haves’
Goal 12: full-testing
Goal 13: Fix static files issues and deploy to Heroku
<br>

#### Analysis of sprint 2 and lessons learned:
The Definition of Done was met, and users were able to access a list of services, make, view, amend and delete their bookings. The static files issues were sorted and the site was successfully deployed to Heroku.
Generally, this sprint went far better than the first one, and the story-points were more or less accurate. Some features were decided to be left (and possibly not picked up again), including integration of an email alert system for the admin. Major bugs were found and fixed in testing, but one minor bug being added for investigation on a later sprint. Other things identified for adding to the backlog to be addressed in a later sprint if appropriate are also listed below in order of importance to the project:
- Fixing the bug to make sure the slot count for the region is accurate (or remove the count)
- Adding improved formatting and potentially images to the services lists
- Pop-ups for user to confirm action for delete
- Message to user when status has been changed by admin (ie a ‘new’ sort of indication)
- Set up of a daily summary email for admin of any bookings requiring confirmation?


### Sprint 3: Objectives - 
Reuse a similar code to the userforum and layout for the UI for the ‘Market’. Users need to be able to list items for sale easily, browse and approach other users to buy items they are interested in. Find a way for users to connect directly when a sale is to be agreed.
#### Definition of Done for Sprint 3:
A marketplace where users have full CRUD capability for listings, and can approach other users to inquire about and purchase items of interest. 
#### Break down of goals meet objectives and the user stories regarding marketplace/trading app:
Goal 1: Set up the model for a ‘for sale’ item (include the CycleConnect logo as a default image which should be there for the users to be encouraged to change). Posts should have item, location, price, picture, categories (new/used, clothing/bike gear, etc), status (sold/available)
Goal 2: Set up the views for the user market post (including admin verification from the outset)
Goal 3: Set up urls and get the basic categorised posts working with images and suitable layout. Toggle of sold/available should work, as should the ability to CRUD items
Goal 4: Set up the messaging for the posts (which are hidden to all the users except for the ones holding the conversation and admin). General users should be able to see the number of different users who are in conversation about the item, but not see the conversation (this needs to be added to user stories, because was not considered at project inception, but is absolutely essential)
Goal 5: Set up the filter according to category (show only those items/those items first)
Goal 6: Items which are sold should drop to the bottom of the list, but not disappear immediately
Goal 7: Sort pagination for the views
Goal 8: Full testing of app and interactions. 
Goal 9: Use the success with the pagination, categorisation and the admin verification to look at the forum app and solve some of the issues
Goal 10: Add a Ts&Cs to verify on first sign up.
Goal 11: Add thumbnail of user image to the header on the pages.
Goal 12: Full testing of additional work

#### Analysis of sprint 3 and lessons learned:

(Goals 8 through to 12 were added later due to the speed at which the first goals were achieved)

### Sprint 4: Objectives - 

#### Definintion of Done for Sprint 4:

#### Break down of goals meet objectives and the user stories regarding social rides app:

#### Analysis of sprint 4 and lessons learned:


### Sprint 5: Objectives - 


## Main Technologies used
- **Python Django 3.2.23** is the main Python web framework used to build the site. The apps are built within the central workspace.
- **Gunicorn 21.2.0** is a Python WSGI HTTP server for UNIX, providing a powerful interface for deploying Python web applications.
- **HTML5** is used to create the templates for the UI.
- **CSS3** is used for the site styling.
- **JavaScript** is used to make the site more dynamic in places where the Python logic would require a separate page, for example this was mainly used to create modals for the users to confirm actions.
- **Bootstrap 4** is an open-source front-end framework for designing websites and web applications. It contains HTML, CSS, and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components, as well as optional JavaScript extensions. It 
- **Cloudinary 1.37.0** provides cloud storage for the image uploads on the site.
- **PostgreSQL Database** is more powerful than the inbuilt SQLite Django database. This handles all the storage of the information added on the site.
- **pyscopg2 2.9.9** is a PostgreSQL database adapter for Python, necessary for interfacing with PostgreSQL databases, commonly used in Django projects.
- **Whitenoise 6.6.0** allows the web app to serve its own static files, making it simpler to deploy Django apps without the need for configuring a separate static file server.
- **Django-allauth 0.58.2** is an integrated set of Django applications addressing authentication, registration, account management as well as third-party (social) account authentication. This is used to handle the sign up logic and could later be extended to include emails and password reset functionality.
- **Django-crispy-forms 1.14.0** is a Django utility that improves the UI and UX of the forms used. Whilst not used in every form field, it is used extensively throughout this project.
- **Django-summernote 0.8.20.0** is a Django application for integrating Summernote (a Bootstrap-based WYSIWYG text editor) into Django projects. Summernote provides the ability to add rich text to entries and was selected for use in the main forum due to the ability to add images directly through the editor. The fields the user can use were adapted from the documentation, and some redundant ones were removed.
- **Pillow 10.1.0** is A Python Imaging Library that adds image processing capabilities to the Python interpreter, essential for handling image fields in Django.


## Key issues and bugs
### Resolved

### Unresolved

## Potential future work beyond the scope of this project


## Deploying to Heroku
1. Ensure that debug mode is set to 'False' in the Django main apps 'settings.py'.
2. Install WhiteNoise `pip3 install whitenoise` and add 'WhiteNoiseMiddleware' to 'MIDDLEWARE' in 'settings.py'.
3. Configure static files in 'settings.py':
- `STATIC_URL = /static/`
- `STATIC_ROOT = BASE_DIR/'staticfiles`
- `STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'`
4. Check in the CSS file if any static images are called from your directory. For each of these, upload the file to Cloudinary and extract the direct link to the image. Replace your image url with this link.
5. Log in to your Heroku account and create a new app with a unique name and appropriate region.
6. Copy the link for the deployed site from Heroku Domains (in 'settings' link in Heroku) and ensure it is added to 'ALLOWED_HOSTS' in 'settings.py'.
7. In the app's 'Settings' tab, go to 'Config Vars':
- Add `PORT` with the value `8000`
- Add database credentials (eg `DATABASE_URL` for PostgreSQL)
- Add `CLOUDINARY_URL` with your Cloudinary credentials
- Add your `SECRET_KEY` 
8. Back in your code editor, run `pip3 freeze > requirements.txt` to save project dependencies.
9. Ensure all code is pushed to GitHub.
10. Back in Heroku, in 'Buildpacks' add 'Python' and 'Node.js', ensuring Python is listed first.
11. In the 'Deploy' tab, choose 'GitHub' as the deployment method and connect your GitHub account.
12. Select your repository and choose between automatic or manual deployment.
13. After deployment, test the project behaves as expected.


## Forking project


## References 
### Images

### Code
Bootstrap navbar - https://getbootstrap.com/docs/4.0/components/navbar/ - Bootstrap Documentation (6th November).
<br>
<br>
Crispy forms general use, Helper, and data cleaning - https://django-crispy-forms.readthedocs.io/en/latest/form_helper.html - Crispy Forms Documentation (6th November).
<br>
<br>
Crispy forms layout helpers and widgets - https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html#crispy-forms-layout-helpers - Vitor Freitas (Nov 28th 2018) (6th November). 
<br>
<br>
Allauth sign-up and sign-out - https://docs.allauth.org/en/latest/account/views.html - Allauth Documentation (8th November).
<br><br>
'Semi-opaque box' CSS from my own code in the Code Institute's Halloween Hackathon 'BeetleJuice Curse Generator'
<br><br>
Initial set-up of the forum largely based on Code Institute's 'I Think, Therefore I Blog' Walkthrough code.
<br><br>
Help with use of logic in views for userprofile (after getting really stuck) from Chat-GPT AI. Code used to fix bug and then adapted (14th November).
<br><br>
Use of Django's authentication. This was referred to frequently in User creation, authentication and use. Includes use of LoginRequiredMixin and the ModelBackend used to attempt a bug fix (later discarded) - https://docs.djangoproject.com/en/5.0/topics/auth/default/ - Django Documentation (16th November). 
<br><br>
Pagination based on walkthrough ('I Think, Therefore I Blog') and classes added to be able to style later (20th November)
<br><br>
Configurations for Django Summernote. Use shown in settings.py - https://github.com/summernote/django-summernote - Django-summernote on GitHub (20th November).
<br><br>
Django Project Docs used to help with trying to get the ‘likes’ working when the walk-though code did not seem to work as expected. Includes use of Django.http imports -  https://docs.djangoproject.com/en/5.0/intro/tutorial04/ - Django Documentation (21st November).
<br><br>
Use of Whitenoise to sort static files - 
https://devcenter.heroku.com/articles/django-assets - Heroku Help. https://devmaesters.com/blog/34 - DevMaesters. 
https://www.w3schools.com/django/django_static_whitenoise.php - W3Schools (22nd November).
<br><br>
Use of JsonResponse in bug fix attempt for likes after asking chat GPT for suggestions. Fix was unsuccessful (22nd November). Then reverted to HttpResponseRedirect after reading more on the issue from the Django Project Documentation (referenced earlier) and fixed bug (23rd November).
<br><br>
MDN Web Docs Guides > Django Tutorial Part 9: Working with forms. For general advice, guidance and things to try when the error messages were flowing. Try/except statement fix in particular for the ProfileDetailsForm: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms (24th November).
<br><br>
Liked posts display partially from “I think therefore I blog”, with some other parts tried from Stack overflow: https://stackoverflow.com/questions/64997951/getting-all-the-users-name-who-liked-a-post-in-django - Stack Overflow (27th November).
<br><br>
Queryset and general Admin actions - https://docs.djangoproject.com/en/4.2/topics/db/queries/ and  https://docs.djangoproject.com/en/4.2/ref/contrib/admin/actions/ - Django Documentation (30th November).
<br><br>
More information used on querysets and Q - https://www.fullstackpython.com/django-db-models-query-q-examples.html - Fullstack Python, https://www.w3schools.com/django/django_queryset_filter.php - W3Schools (30th November).
<br><br>
Information and tutorial for sending information between the JS and the templates, and how the JSONResponse links into the views.py. Failed attempts at dynamic drop downs for services and bookings tried from: Sorting dynamic requests in Django for the bookings: AJAX - https://www.youtube.com/watch?v=QDdLvImfq_g - Django AJAX Tutorial: Basic AJAX in Django app | Django casts # (23rd November)
<br><br>
Chat GPT to try to solve the issues with the bookings forms: It generated the following lines of code which I used and appeared to be successful in fixing the problem (1st December): 
`If self.service:
		self.fields['service'].initial = self.service
		self.fields['service'].disabled = True
		# Assuming your Slot model has date and time fields
		self.fields['date'].queryset = self.service.slot_set.values_list('start_time__date', flat=True).distinct()
`
<br><br>
Chat GPT for how to create bicycle bullet points for my list in services and bookings. The start and finish of that code is clearly marked in the CSS file. (4th December)
<br><br>
I imported Pillow after reading some comments in various Python forums (and from the PP4 channel of the Code Institute’s Slack feed) to handle the images - https://realpython.com/image-processing-with-the-python-pillow-library/ - RealPython (4th December).
<br><br>
I asked Chat GPT how to best display the information in my template gathered from my form input radio buttons regarding status, condition and category. It suggested the use of ‘post.get_status_display’, which worked really well, so I also used this approach for category and condition. (5th December)
<br><br>
Toggling the status (sold or available) views code was run through Chat GPT again (after all the issues I had getting the ‘likes’ sorted for the forum posts. The use of ‘@require_POST’ and how to apply the subsequent logic was explained through the AI engine. I added my own variables and it worked really well.  (6th December).
<br><br>
Filters for the items developed from the Django docs https://docs.djangoproject.com/en/5.0/topics/db/queries/ and https://learndjango.com/tutorials/django-search-tutorial - Django Documentation (6th December and again on 9th December).
<br><br>
Use of Subquery and OuterRef. This helped to fix the bugs encountered with the ‘trading conversations’ buttons - https://docs.djangoproject.com/en/5.0/ref/models/expressions/#:~:text=Use%20OuterRef%20when%20a%20queryset,outer%20query%20or%20its%20transform - Django Project. And https://djangocentral.com/how-to-use-subquery-in-django/ - Django Central (8th December).
<br><br>
Use of Case/When - https://stackoverflow.com/questions/51165089/using-case-in-django - Stack Overflow (8th December).
<br><br>
Ts and Cs text generated by Chat GPT after being given a rough outline of requirement from me. (9th December)
<br><br>
Middleware requirements for ts and cs - https://django-termsandconditions.readthedocs.io/ - Django Read The Docs (9th December).
<br><br>
General set up of Ts and Cs - Users are asked to agree to terms and conditions for the site: https://www.youtube.com/watch?v=tR_z6mG1oe8 Django Web App Beginner Tutorial: User Registration, Login, Logout, Terms Conditions.  Skolo Online 9th December.
Ride registration with the toggle button and display referred from https://docs.djangoproject.com/en/5.0/ref/request-response/ (13th December) 
Using and developing logic for dates for rides and sign-ups: https://docs.djangoproject.com/en/5.0/ref/models/conditional-expressions/ (14th December)
Using key.startswith to interpret the users on the ride, verify and save them with the logic from https://www.geeksforgeeks.org/python-prefix-key-match-in-dictionary/ Adding the prefixes inspired by https://www.geeksforgeeks.org/python-add-prefix-to-each-key-name-in-dictionary/, but heavily modified and simplified in the application. (14th December)
Timezone.make_aware and timezone.get_default_timezone() https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/ and https://www.fullstackpython.com/django-utils-timezone-make-aware-examples.html (15th December)
Creating image thumbnails using JS: https://dev.to/pqina/generating-image-thumbnails-in-the-browser-using-javascript-and-filepond-10b8 and https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL (17th December)
Using JavaScript to retrieve and compare date fields: https://phoenixnap.com/kb/how-to-get-the-current-date-and-time-javascript (18th December)
Custom template tags for counting and comparing slots in bookings: https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/ (21st December)
<br><br>
Check and verification of initial data-model from Mentor
<br><br>
Project inspiration and general support


