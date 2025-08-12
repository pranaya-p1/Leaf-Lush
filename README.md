# Project Definition – Leaf & Lush

## Purpose
**Leaf & Lush** is a gardening-themed social networking web application designed to make gardening easy and accessible for young people. It allows users to share tips, post videos, participate in contests, and track plant growth using personal dashboards. Our goal is to create a supportive online gardening community.

## Functional Requirements (What the app will do)
- Users can create an account and log in
- Users can create dashboards for their plants
- Users can post gardening tips, images, and videos
- Users can read newsletters on gardening topics
- Users can enter gardening contests
- Users can complete “quests” (gamified gardening challenges)
- Users can flag/report misinformation
- Admins can approve expert-verified posts

## Non-Functional Requirements (How the app will look & perform)
- Clean and modern UI with earthy colour tones (greens, browns)
- Mobile-friendly and responsive design
- Fast loading (under 3 seconds per page)
- Safe and secure login with multi-factor authentication
- AES-256 encryption for sensitive data
- Regular data backups and use of firewalls
- IDS/IPS monitoring for suspicious activity

## Project Scope
The core features like posting, dashboards, and contests are achievable within 10 weeks. We will start with basic versions of each feature and develop them further if time allows.

## Scope Issues
**Some advanced features such as:**
- Full encryption and security features
- Complex admin/moderation tools  
...may not be completed in full due to the time constraint, but we will include basic mockups or simplified versions.

# Project Task 2  : Basic Design of UI, Hierachy and Interactive Elements  
## Changes
After reviewing the previous UI Design form last year, i decided to change the colour scheme to make it more engaging and visually appealing. 

## My Inspiration:
I beleived that these **contrasting colours** was more effective while still sticking to the **Gardening Theme.**

![alt text](<colour scheme.png>)


## Before vs After
The **previous colour pallete** and design seemed to be dull and not catchy to the eye. The logo was also simple and didn't **effectively compliment the website.** 

![alt text](<before colour.png>)
![alt text](image.png)

After implementing new colours, the UI design was much better. 

![alt text](<after colour.png>)
![alt text](logo-2.png)

## Current Design
**Homepage:**

![alt text](homepage.png)

**Events Page:**

![alt text](<events page.png>)

**Sign Up Page:**

![alt text](<sign up page.png>)

**Dashboard Page:**

![Dashboard](<dashboard page.png>)


# Project Task 3 - Alternative Design - Playing with Possibilities

## Client Feedback
 - Add an option to change login and profile information
 - Create a more minimalist dsign
 - Create more rounded and smaller buttons
 - Move headings to the centre rather than the side 
 - Add a searchbar icon

## Design Choices
| Design Element   | Choice                                                      |
| ---------------- | ----------------------------------------------------------- |
| Colour Palette   | Garden Green (#86C232), Grey (#474B4F), Jet Black (#000000), White(#FFFFFF) |
| Typography       | Heading: Newsreader, Lexend, Body: Inter                    |
| Image/Icon Style | AI-generated images, Figma Icons & Assets                   |

## Alternative Design Prototype

The Sign-Up Page and Dashboard have a similar layout, however the header is changed to match the other pages.  

**HomePage:**

![Homepage Image](Homepage-1.png)

**Events Page:**

![Eventspage image](Events.png)



# Project Task 4 - Designing Algorithms

## Flowchart
![Flowchart](Flowchart-1.png)

## Pseudocode
1. User clicks "Add Plant" button
2. Prompt user to upload plant photo
   - If no photo → show error and go back
3. Prompt user to enter:
   - Latin Name
   - Short Bio
   - Fruits Produced? (Yes/No)
   - Fun Fact
4. Validate all fields
   - If missing → show error and go back
5. Save details to database
6. Display new plant card on dashboard

## Test Cases
###  Add Plant to Dashboard

| Test Case ID | Feature Being Tested     | Input                                                                                                                                             | Expected Output                                                  |
|--------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| TC001        | Add Plant to Dashboard   | **Photo**: rose.jpg, **Latin Name**: *Rosa chinensis*, **Bio**: "A beautiful rose plant", **Fruits**: No, **Fun Fact**: "Symbol of love"           | Plant card appears on dashboard with uploaded image and details |
| TC002        | Add Plant to Dashboard   | **Photo**: _(none)_, **Latin Name**: *Ocimum basilicum*, **Bio**: "Basil plant for cooking", **Fruits**: Yes, **Fun Fact**: "Great in pasta"       | Error message: "Please upload a plant photo"                    |
