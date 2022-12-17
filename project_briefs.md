# Project - Web Programming with Python

:star: Remember to gather PDA evidence :star:

Over the next week you will build an app to consolidate and expand on everything you have learned:

* Object oriented programming with Python
* Web Programming (REST, MVC)
* Interacting with a PostgreSQL database (CRUD)

## Rules

* It's Thursday - take a break, have a beer, all you need to do today is be ready to tell us what project you're doing in standup tomorrow

The project must be built using only:

* HTML / CSS
* Python
* Flask
* PostgreSQL

It **MUST NOT** use:

* Any Object Relational Mapper (e.g. ActiveRecord)
* JavaScript. At all. Don't even think about it. We'll get there.
* Authentication. Assume ONE user that already has secure access to the app. Do not create fake login forms! Please (🙏)
* Any pre-built CSS libraries, such as Bootstrap.

Do not make any attempt to use them this week, even if you've used them before.

Make lots of little (but sensible!) git commits. We'd ideally expect around 50 commits across the week.

## Briefs

These briefs detail what is expected of you, including an MVP. Note that the MVP is the **Minimum** Viable Product. You are strongly encouraged to go beyond these specifications if you have time, and some possible extensions are provided.

Talk through your ideas with an instructor during the planning process, and before you begin coding.

<hr>

### Gym

A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

#### MVP

- The app should allow the gym to create and edit Members
- The app should allow the gym to create and edit Classes
- The app should allow the gym to book members on specific classes
- The app should show a list of all upcoming classes
- The app should show all members that are booked in for a particular class

#### Inspired By

[Glofox](https://www.glofox.com/club-solution/), [Pike13](https://www.pike13.com/pike13-scheduling-software-demo)

#### Possible Extensions

- Classes could have a maximum capacity, and users can only be added while there is space remaining.
- The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
- The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.

<hr>

### Shop Inventory

Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

#### MVP

* The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
* The inventory should track manufacturers, including a name and any other appropriate details.
* The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
  * This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
* Show an inventory page, listing all the details for all the products in stock in a single view.
* As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

#### Inspired by

eBay, Amazon (back end only), Magento

#### Possible Extensions

* Calculate the markup on items in the store, and display it in the inventory
* Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.
* Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these categories.
* Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.

<hr>

### Spending Tracker

Build an app that allows a user to track their spending.

#### MVP

* The app should allow the user to create and edit merchants, e.g. Tesco, Amazon, ScotRail
* The app should allow the user to create and edit tags for their spending, e.g. groceries, entertainment, transport
* The user should be able to assign tags and merchants to a transaction, as well as an amount spent on each transaction.
* The app should display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.

#### Inspired by:

Monzo, MoneyDashboard, lots of mobile/online banking apps

#### Possible Extensions

* The user should be able to mark Merchants and Tags as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction. 
* Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
* The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.
* The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.

<hr>

### Vet Management App

A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after MANY animals at a time. An animal is registered with only ONE vet.

#### MVP

- The practice wants to be able to register / track animals. Important information for the vets to know is -
  - Name
  - Date Of Birth (use a VARCHAR initially)
  - Type of animal
  - Contact details for the owner
  - Treatment notes
- Be able to assign animals to vets
- CRUD actions for vets / animals - remember the user - what would they want to see on each View? What Views should there be?

### Possible Extensions

- If an owner has multiple animals we don't want to keep updating contact details separately for each pet. Extend your application to reflect that an owner can have MANY pets and to more sensibly keep track of owners' details (avoiding repetition / inconsistencies)
- Handle check-in / check-out dates
- Let the practice see all animals currently in the practice (today's date is between the check-in and check-out?)
- Sometimes an owner does not know the DOB. Allow them to enter an age instead. Try and make sure this always up to date - ie if they visit again a year from now a 3 yr old dog is now 4.
- Add extra functionality of your choosing - assigning treatments, a more comprehensive way of maintaining treatment notes over time. Appointments. Pricing / billing.

<hr>

### Twist your own

We're open to the idea of you spinning one of these briefs. E.g. a doctor's surgery instead of a vet practice.

<hr>


## Presentation

Presentations will be held on Thursday. You will have 10 minutes to present your work, with 5 minutes for questions.

We expect you to:

* Show your sketches, notes, diagrams, wireframes and user planning
* Demonstrate your app's functionality
* Talk about some code that you are particularly proud of
* Highlight your main learning points
* **Send us a YouTube link for walk-on music**. This gives you time to set up your laptop without any awkwardness. If you want your song to start at a particular second, here's how - https://www.lifewire.com/link-to-specific-part-of-youtube-video-1616414

Do not:

* Talk through every single line of code
* Go over the time limit

## Asking for help

The instructional team will be on hand for technical assistance, but you are strongly encouraged to take this opportunity to practise self-sufficiency, as will be expected of you as a professional software developer.

Before asking an instructor for help this week, you should be ready to answer the following questions:

* What are you trying to achieve?
* What do you think the problem is?
* What have you tried so far?
* What did Google say about your error message?

## Attendance

The cohort will do standup at the usual time every morning. Your attendance is recorded every day as normal.

## PDA Reminder:

As part of this project you are required to take screenshots of the following:

```
- A Use Case Diagram  
- A Class diagram  
- An Object diagram  
- An Activity Diagram
- A user sitemap
- Two wireframe designs
- An example of pseudocode for a function
- One of your projects where you have worked alone and attach the Github link
```

Show user input being processed according to design requirements. Take a screenshot of:

```
- The user inputting something into your program
- The user input being saved or used in some way
```

Show an interaction with data persistence. Take a screenshot of:

```
- Data being inputted into your program
- Confirmation of the data being saved
```

Show the correct output of results and feedback to user. Take a screenshot of:

```
- The user requesting information or an action to be performed
- The user request being processed correctly and demonstrated in the program
```

Produce an Implementations Constraints plan detailing the following factors:

```
 - Hardware and software platforms
 - Performance requirements
 - Persistent storage and transactions
 - Usability
 - Budgets
 - Time   
```

- Submit your PDA evidence (screenshots, etc.) to Canvas

PDA Reference:
A.D 1, A.D 2, A.D 3, A.D 4, A.D 6, P5, P6, P10, P11, P13, P14, P15
