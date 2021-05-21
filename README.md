# Chelsea Wolfe Online Store #
---
![Hero Screenshot]()

## Contents ##
---

* 1. Research
* 2. UX
    * [User Stories](#user-stories)
    * [Strategy Goals](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Wireframes](#wireframes)
    * [Design](#design)
        * [Colors](#colors)
        * [Fonts](#fonts)
        * [Icons](#icons)
    * [Stripe Functionnality](#stripe)
    * [Database Schema](#dbscheme)
    * [Defensive Design](#defensivedesign)
* [Technologies](#technologies)
    * [Languages and Frameworks](#landf)
    * [Tools](#tools)
* [Features](#features)
    * [Existing Features](#existing)
    * [Future Features](#future)
* [Testing](#testing)
* [Issues](#issues)
* [Deployment](#deployment)
    * [Requirements](#required)
    * [Local deployment](#locald)
    * [Deployment to Heroku](#dheroku) 
* [Credits and References](#credits)

## Research ##
---

To build this project I conducted a global search on the music artist Chelsea Wolfe to know if she already had online stores.  She uses two different plateforms for the EU and US market. All product and informations are picked from both websites.

Then I did a benchmark of all the eCommerce website I liked, whether they are music related or not. I used this benchmark to assemble the front-end and the back-end features I found relevant for this project.

I also took went to [**Awwwards.**](https://www.awwwards.com/) for front-end inspiration and followed several Youtube tutorials, all credited in the 'Credits' section of this document, to build an visually entertaining project and extend my CSS and JS knowledge.

## UX (User Experience) ##
---
<a name="user-stories"></a>
### User Stories ###

After viewing the Boutique Ado mini project, I decided to organize the user stories of this project in a spreadsheet rather then listing them here as they are extensive and a spreadsheet was also easier for me to follow through the development of this project.

Please [**click here**](https://docs.google.com/spreadsheets/d/1Jjwrl0Z5zI8jjJYmJ2XXgHS7ZZPKOzklTGwQ07svR-o/edit?usp=sharing) to discover the User Stories.

<a name="strategy"></a>
### Strategy Goals ###

#### Business Goals ####
* To sell merchandise associated with the artist Chelsea Wolfe.
* To match the design and atmosphere of the artist and offer a website that is easy to navigate and free of confusion.
* To become another source of revenue for the music artist.
* To become a plateform where fans can support the artist and subscribe to a newsletter.
* To allow users to leave reviews on products to control product quality and popularity.
* To create a stock of products to be sold online and keep track of the sales as an admin.
* To be able to crete/update/delete products and their infomations as an admin
* To enable users to create an account for future purchases and access to special discounts.

#### User Goals ####

* To navigate the website easily and understand its purpose.
* To find products and their informations (price, size, category, availability) fast and easy through a website search or through the navigation bar.
* To be able to buy products online as a guest or a registered user.
* To receive a confirmation email with all relevant informations.
* To be able to create/update/delete my personal informations.
* To see a history of my previous purchases.

<a name="Scope"></a>
### Scope ### 

The users should be able to conduct the following actions on the website:

* Use the navigation bar effectively on all devices.
* Conduct a product search by category, text and price in the search bar and get relevant results.
* Check product informations when clicked.
* Add/remove items from the shopping bag.
* Add more than one item in the shopping bag.
* Get an update of the bag status each time one of the actions mentionned above happens.
* Purchase products securely through a payment platform.
* Subscribe to the newsletter.
* Create/Update/Save/Delete their profile account with personal informations.
* Read reviews as guest users, post reviews as registered users.

As an Admin:
* Add, edit, delete a product and its informations.
* Delete reviews that do not meet website policies.
* Create/Update sales product and special prices.


<a name="Structure"></a>

### Structure ###

I used the online tool [**Gloomap**]() to create the map below referring to the structure of the website as in deffirent scenarios.
* The cases in **white** refer to a possible structure from a guest user.
* The cases in **green** refer to a possible structure from a registered user.
* The cases in **yellow** refer to a possible structure from an admin.

Click here to open the map in full or check the image below.

<a name="wireframes"></a>

### Wireframes ###

To create the wireframes for this project, I used the tool [**Balsamiq**](https://balsamiq.com/). I initially wanted to use Figma but was a bit lost in the process.

Click here to discover the wireframes.

<a name="design"></a>

### Design ###

The Chelsea Wolfe store is to be at the image of the artist (which I found to be lacking in her actual EU and US stores). I went for a striking Minimal and Gothic design that I think bring her merch to her standards. All product images are taken from her EU and US stores.

<a name="colors"></a>

##### Colors ####

* It was fairly easy to find a color scheme for this project as the artist Chelsea Wolfe already has a very strong visual identity and is known for it. I went to a Modern Pastel Gothic color scheme that fitted the hero picture with a light pick and a pure white as a main colors to capture the user's attention and turquoise and dark grey as secondary colors for contrast.

Here is my palette :

<a name="fonts"></a>

### Fonts ###

* I wanted to fit the minimal but gothic aesthetic of the website by pairing a bold gothic font for the titles with a lighter and elegant font for all other text content. I chose the Google Fonts pairing of the bold [**Pirata One**]() and the sans-serif [**Raleway**]() to match the contrast I wanted to create and found it aethetically pleasing.

<a name="icons"></a>

### Icons ###

* All icons on this project are taken from the library  [**FontAwesome**](https://fontawesome.com/)
* The Favicon was made using [**Favicon**](https://favicon.io/) online tool with one of the old Chelsea Wolfe logo used on her patches and pins in the store.


<a name="dbscheme"></a>

### Database Scheme ###

* Following requirements, I created my database structure within the Django Framework. For this I followed the **Boutique Ado** CodeInstitute  mini-project.

I made the following schema with [**QuickDBD**](https://www.quickdatabasediagrams.com/):

<a name="defensivedesign"></a>

### Defensive Design ###


1. All required form inputs display a warning message as a tooltip if the field is filled incorrectly.
2. If a non-registered user tries to leave a comment or a review, they will be automatically redirected to the sign-in page.
3. Add to bag button disabled if the product is out of stock.
4. If a user tries to put a number of a single product greater than the stock, a warning message will be displayed and the add to bag action is cancelled.
5. Every time a form is submitted (search, product, review, comment), the user is informed of the action success/failure through a toast message.
6. Implementation of webhooks to create order status in the database and avoid any misstep from the user during checkout.
7. Custom error pages redirecting to homepage.
8. Default images for blog posts and products if the image selected is broken or if no image was selected.


<a name="technologies"></a>

## Technologies ##
---

### Languages and Frameworks ###
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Javascript]()
* [Python]()
* [JQuery](https://jquery.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Font-Awesome](https://fontawesome.com/icons?d=gallery)
* [GSAP](https://greensock.com/gsap/)
* [Django](https://github.com/django/django)
* [SQLite](https://www.sqlite.org/index.html)


### Tools  ###

* [Google fonts](https://fonts.google.com/)
* [Git](https://git-scm.com/)
* [Gitpod](https://gitpod.io/)
* [Heroku](https://heroku.com/)
* [AWS](https://aws.amazon.com/)
* [Balsamiq](https://balsamiq.com/)
* [QuickDBD](https://www.quickdatabasediagrams.com/)
* [Favicon.io](https://favicon.io/)
* [Gloomap](https://www.gloomaps.com/)
* [W3C HTML Validator](https://validator.w3.org/)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JSHINT](https://jshint.com/)
* [PEP8](http://pep8online.com/)


<a name="Features"></a>

## Features ##
---

<a name="existing"></a>

### Existiting Features per Apps ###

**Responsiveness**

* This feature allows the user to consult the website from any of their devices.

* All templates of this project have been build with the responsive framework Bootstrap 4. I also used targeted media queries to make this project responsive on all screen sizes.

**Navigation bars**

* This feature allows the user to navigate through the website easily and without conflicts.

* This project has two responsive navigation bars present on all pages:
1. Main navigation bar: 
* The search bar allows the user to search for products by name, word, category.
* My profile dropdown menu: Links to register or sign in forms when the user is logged out. When logged in as a registered user, the menu links to the profile app and the logout page. When logged in as an admin, the dropdown links to the the product and blog management pages as well as the profile app and the log out page.
* Shopping bag: Update shopping bag once an item is added to the bag and displays the total price. 

2. Product/Contact/Blog navigation bar:
* This navigation bar allows the user to check the shop collections by different category.
* The user can also navigate to the blog section and the contact page.

**Home App**

* This features informs in an attractive way the user of the content of the website and it's safety. It gives an introduction about the artist as well as the products .

* This feature focuses on the index page only.
* The landing page includes a hero animation made with the GSAP library, a call to action button to visit the store, a featured product section with animated cards and a security banner.
* The featured product section showcases selected on random from the product collection.

**Shopping bag App**

* This feature allows the user to add/adjust/delete different products to the shopping bag and view the total price and details in the bag.
* When a product is added, a preview of the shopping bag is displayed in a toast and the total price/shipping price is updated.

**Checkout App**

* This feature allows the user to safely buy the selection of item previously put in the bag thanks to **Stripe**.
* The user doesn't need to be logged in to buy products. If logged in the shipping details will be filled from the details given in the user profile. 
* If no details where given or a detail is changed in the checkout form when logged in, the user has the possibility to check the Remember checkbox and all details will be updated in the profile app.
* The credit card details section is linked to the payment platform **Stripe** to ensure a secure payment procedure. 
* Once the buy button is clicked it triggers custom loading animated screen that will remain while Stripe check the credit card details.
* If the payment did not go through, the user is redirected to the checkout form and informed of the failed procedure.
* If the payment succeeded, the user will be send a confirmation email with the order details and the order number and will be redirected to the checkout success page, informing them of the order detail and the order number.


**Product App**

* This feature allows the user to see all products and their details on the website. The user can also read product reviews as well as Add/Edit/Delete their product review if they are logged in. It also allows the admin to Add/Edit/Delete products in the database.

1. Products page:
* The user can browse by product categories that are on the website through the navigation bar. A keyword search can also be conducted in the navigation bar search box to browse items more specifically.
* The products displayed can be sorted out by alphabetical order and price thanks to the selector under the page title.

2. Product detail page:
* This page displays all the product details (name, category, image, description, price, sizes if any) as well as the review section. All users can visit the product details and read the reviews but need the be registered and logged in to leave a review and a rating.

3. Review/rating section:
* When logged in the user can edit and delete their review and rating directly from the review section. The edit link  redirects to an edit form while the delete link triggers a confirmation modal and deletes the review forever if "Delete" is clicked in the modal.
* To add a review and a rating, the user can click on the "Leave a review" button and will be redirected to the add review page and fill a simple form. Once the form is filled and the user clicked the "Submit" button, they will be redirected to the product page.

4. Suggested Product:
* This feature is located at the bottom of the product details page and is implemented to encourage the customer to look into more store products.
* It generates maximum 4 product cards of the same product category than the product details viewed by the user.

5. Product management:
* If the user is logged in as an admin, they will have the possibility to navigate to the Product management page (through the profile dropdown menu in the main navigation bar) and have the possibility to add a product to the database by filling the add product form. Images can be selected directly from the user's computer and not only as url linked images.
* The admin only can edit and/or delete any product by navigating on a product detail page and click on the edit/delete links.The edit link redirects to a edit form while the delete link triggers a confirmation modal and permanently deletes the product from the database if "Delete" is clicked in the modal.


**Profile App**

* This feature allows the user to create a custom profile on the website and be given registered user priviledges (comments, reviews, checkout details)
1. Registration
* The user can register to the website through the Register form page. Every account requests an email address , a username and a password.
* The email and password need to be confirmed twice to avoid typos.
* A verification email is sent to the user's email to avoid errors. That email contains a security link that opens a "confirmed email" page on the website. The user is added to the database and is allowed to complete their profile on their new profile page.

2. Signing in.
* If the user is already registered, they can sign in through the login page. The user needs their email adress or username as well as their password to connect. The user can also retrieve their password if forgotten.
* Once the login form is approved, the user is redirected to their profile page containing their personal information.

3. Log out
* Once the the user is logged in, they can easily log out by accessing the logout page through the main navigation bar and confirm on that page their intention to log out. The user is then redirected to the index page.

4. Profile Page:
* The profile page is personal and contains:
    - A editable personal information form including the shipping details that will be remember at checkout if logged in.
    - An order history with order number, date and order details. The order number links to the order confirmation page.
    - A review history with date, review and rating. the user can delete or edit their reviews from there.

**Blog App**

* This feature allows the user to be informed of the current artist situation and actions on the webshop as well as communicating with the whole website's community.

1. Blog page:
* This page can be accessed through the navigation menu and displays all blog posts by date, the blog cards include an image, a title, a content preview and the date/author.

2. Blog detail page:
* This page display the full blog post (title, image, text, author and date) as well as the comment section. All users can read the blog post and comments but need the be registered and logged in to comment.

3. Comment section
* When logged in the user can edit and delete their comment directly from the comment section.The edit link redirects to a edit form while the delete link triggers a confirmation modal and permanently deletes the comment if "Delete" is clicked in the modal.
* To add a comment, the user can click on the "Leave a comment" button and will be redirected to the add comment page and fill a simple form. Once the form is filled and the user clicked the "Submit" button, they will be redirected to the blog page.

4. Blog management:
* If the user is logged in as an admin, they will have the possibility to navigate to the Blog management page (through the profile dropdown menu in the main navigation bar) and have the possibility to add a blog post to the blog page/database by filling the add blog post form. Images can be selected directly from the user's computer and not only as URL linked images.
* The admin only can edit and/or delete any blog post by navigating by a blog detail page and click on the edit/delete links.The edit link  redirects to a edit form while the delete link throws a confirmation modal and deletes the post forever if "Delete" is clicked in the modal.

**Contact App**

* This feature allows the user to contact the website's admin and send queries.

* The Contact page allows the user to send a written query to the admin. The query is stored in the database and two email alerts are sent: one to the user to confirm that the message was received and one to the admin to signal the reception of a new query. The alert sent to the admin contains all informations given by the user in the contact form.
* The user does not need to be a registered user to send a query.


<a name="future"></a>

### Future Features ###

* The possibility to add different stock per product sizes.
* Answering messages sent through contact form via the website.
* Sale prices.
* Social Media login.

## Deployment ##
---
<a name="requirements"></a>

### Requirements ###

* an IDE , I used GitPod.
* PIP, for Python packages.
* Python3
* Git for version control.
* Stripe (account, test keys and webhooks) as a secure payment platform.
* AWS cloud storage  and an S3 bucket for online backup of static files.
* Email account, I used Gmail.

<a name="locald"></a>

### Local Deployment ###

<a name="herokud"></a>

**1. Clone from Github**

* One can run this project locally on their IDE of choice by saving a copy of the Github repository at https://github.com/AudreyLL88/cw_store.git by clicking the "Download Code" button or by running this command in their IDE command line:

$ git clone https://github.com/AudreyLL88/cw_store.git

To remove any link to github, one can use the command git remote rm origin into their terminal.

**2. Install Python required modules**

* run the command below to install all the module required to run this project:

pip3 install -r requirements.txt

**3. Store environment variables**

* If you decide to use Gitpod for the development of this project and you can store your environement variables directly in Gitpod by clicking on "Settings" on the Worspaces page then inserted the following variables in  the "Environement Variables" section :

```
'DEVELOPMENT', 'True'
'SECRET_KEY', '<your value>'
'STRIPE_PUBLIC_KEY', '<your value>'
'STRIPE_SECRET_KEY', '<your value>'
'STRIPE_WH_SECRET', '<your value>'
```

* If using another IDE or Gitpod, create env.py file in the root directory of the project and include the following:

```
import os

os.environ["STRIPE_PUBLIC_KEY"] = "YOUR_STRIPE_PUBLIC_KEY"
os.environ["STRIPE_SECRET_KEY"] = "YOUR_STRIPE_SECRET_KEY"
os.environ["STRIPE_WH_SECRET"] = "YOUR_STRIPE_WH_SECRET"
os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY_HERE"
os.environ["DEVELOPMENT"] = "True"
```

* Follow these instructions to fill in the values of each keys:
    - the SECRET_KEY : use a Django Secret Key Generator such as [Djecrety](https://djecrety.ir/)
    - the STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY can be found on the Stripe Dashboard in the Developer's API section.
    - the STRIPE_WH_SECRET: Can be found in the Developer'sAPI section after creating a webhook.

**4. Migrate database models**

* Run the commands below to migrate the models and set up an SQLite database:

````
python3 manage.py makemigrations
python3 manage.py migrate
````

**5. Load categories and products**

* Run the command below in that exact order to load category then product fixtures:

````
python3 manage.py loaddata categories
python3 manage.py loaddata products
````

**6. Create SuperUser**

* A superUser is needed to access the admin panel in Django. Run the command below and follow the instructions after (email needed):

````
python3 manage.py createsuperuser
````

**7. Run the app**

* Enter the command below to start running the project locally :

````
python3 manage.py runserver
````


### Heroku Deployment ###

**1. Signup and login to Heroku**

* Start by going to https://heroku.com/ and create an account or sign in your already existing account.
* Create an app with a unique name and choose your location.
* Navigate to the Resource tab and create a free Postgres database. 

**2. Prepare the database**

* The DATABASE_URL variable was automatically created in the Settings< Config Vars section. Copy its value and temporarily add it to your environment variables in your IDE or your env.py.

* In your Heroku App, navigate to Settings and set the following variables in the Config Vars section:

`````
'AWS_ACCESS_KEY_ID', '<your value>'
'AWS_SECRET_ACCESS_KEY', '<your value>'
'DATABASE_URL', '<your value>'
'SECRET_KEY', '<your value>'
'STRIPE_PUBLIC_KEY', '<your value>'
'STRIPE_SECRET_KEY', '<your value>'
'STRIPE_WH_SECRET', '<your value>'
'USE_AWS', 'True'
`````

* You can now make the migrations to start using Postgres:
``````
python3 manage.py makemigrations
python3 manage.py migrate
``````
* And load the category the product fixtures:
``````
python3 manage.py loaddata categories
python3 manage.py loaddata products
``````

**3. Create a Superuser for mew Postgres database**

* Run the following command to create a superuser to navigate to Django's admin panel:

``````
python3 manage.py createsuperuser
``````

**4. Create Procfile**

* Create a Procfile and add " web: python app.py "then save.
* Push all changed files to Github by running the following commands:
```````
git add .
git commit -m "..."
git push
```````

**5. Remove DATABASE_URL variable**

* Delete the temporary DATABASE_URL from your environement variables or env.py.

**6. Install Heroku CLI and login**

* In case your environment doesn't have it already, run this command to install the Heroku CLI  in your terminal:

``````
$ heroku login
``````
* To login from the CLI run the following command in your terminal:
```````
heroku login -i
```````

**7. Settings**

*Add the hostname of your Heroku App to "ALLOWED HOSTS" in settings.py. the Hostname can be found in the heroku settings < App Name . 

**8. Connect repository to Heroku**

* 1. You can connect your Github repository directly in the Heroku app by selecting your repository in the Deploy tab < Deployment method. I also selected the Automatic Deployment option for convenience. Click on Deploy.

* 2. Copy the Heroku gir url in the Heroku app Setting tab and run the command below to connect your repository:

```````
$ git remote add heroku <your heroku git url>
```````

**9. Add static files to AWS S3**
* In your S3 Bucket, create a 'Media' folder and add all your media files. 
* Still in the bucket, create a 'Static' folder. Django will collect all static files and upload them to S3 as soon as the app is deployed to Heroku

**10. Push to Heroku**

* If you have decided to connect your Github repository to heroku and selected the automatic deployment option, commit and push will be pushed to Heroku.

* In other scenarios , use the following command:

```````
$ git push -u heroku master
```````

The app can now be open at https://< your-app-name >.herokuapp.com/

<a name="credits"></a>

## Credits and References ##
---

**Text Credits:**

All product informations were taken from Chelsea Wolfe official stores :
- https://evilgreed.net/collections/chelsea-wolfe
- https://www.hellomerch.com/collections/chelsea-wolfe

All informations about Chelsea wolfe were taken on her official website:
- https://chelseawolfe.net/


**Image Credits:**

All products images were taken from the offical Chelsea Wolfe US and EU stores:
- https://www.hellomerch.com/collections/chelsea-wolfe
- https://evilgreed.net/collections/chelsea-wolfe

**Code Tutorials**

* This website was made following the tutorials of Code institute for the Boutique Ado project by Chris Zielinski.

* The hero animation was inspired by the [**BedimCode Tutorial**](https://www.youtube.com/watch?v=PLp46cA0Ep8) and heavily edited to fit the project.
* The product detail animation was inspired by [**Codevo tutorial**](https://www.youtube.com/watch?v=FntCLDXQZfs) and heavily edited to fit the project.
* The product cards were inspired by [**Oscar's Codepen**](https://codepen.io/olhilton/pen/dXaqxE) and heavily edited to fit the project.
* The footer was inspired from [**This CodePen**](https://codepen.io/olhilton/pen/dXaqxE) and heavily edited to fit the project.
* The product size and contact form code is partially inspired by [**Kevin Bourke's Fullstack project**](https://github.com/Bourkekev/ms4-power-fitness-gym) and modified to fit with the stock availability.


**Many thanks to:**

* 

**Site for educational purposes only!** (for now)
