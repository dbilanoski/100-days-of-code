# 366 Days Of Code Log - Danilo Bilanoski

## Challenge Goals & Planning

### Primary Commitment
> I will code for at least half hour every day for the next 366 days.

### Broad Goals
- Revisit HTML, CSS & responsive design principles
- Learn JS well
- Learn one JS framework well
- Expand portfolio (min 15 projects)
- Create personal portfolio website
- Job ready by the end of the year (frontend position)
- Advance in Linux environment
- Get better at English language
- Bring back discipline & order

### First Quarter Plan
- Revisit and recall HTML, CSS & responsive design principles
    - Kevin Powell’s The Responsive Web Design Bootcamp
    - freeCodeCamp Responsive Web Design Certification
- Revisit and recall previously learned JS
    - Brad Traversy’s Modern Javascript From The Beginning
    - Parallel to course, read Eloquent JavaScript
- Focus more on object oriented JS, async JS and ES6 (things I know less now)
- Plan further learning of JS and decide on JS framework, write second quarter plan

**Start date: January 1st, 2020.**

## Days - table of content
[Day 1](#day-1-january-1st-2020)
[Day 2](#day-2-january-2nd-2020)
[Day 3](#day-3-january-3rd-2020)
[Day 4](#day-4-january-4th-2020)
[Day 5](#day-5-january-5th-2020)
[Day 6](#day-6-january-6th-2020)
[Day 7](#day-7-january-7th-2020)

---
### Day 1: January 1st, 2020
Made a plan, evaluated my knowledge and sorted literature and courses I will take in first quarter of this challenge. Prepared GitHub journal repo and fooled around in Firefox Console with some basic JavaScript. Still got them, basics :)

While preparing this, learned some Markdown syntax.

[Twitter post](https://twitter.com/DBilanoski/status/1212484655796105217)

### Day 2: January 2nd, 2020
Today I started with [Kevin Powell's Responsive Web Design Bootcamp](https://scrimba.com/g/gresponsive) with a plan to revisit and recall HTML, CSS & Responsive design principles and roughtly at the third of the first module, I can say I made a good choice of course literature.

**Topics I covered:**
- Box model
- Inline VS block elements
- Margin & padding, collapsing margins especially
    - Interesting thing, if we set margin-top to first child element in some HTML box, that margin will become parent's top-margin
- Link states and how to style them properly
    - Interesting thing, five states of anchor tag, never heard of a:link state
    - Seems to me that best practice is to set styles for "a" in general, then style a:hover and a:focus
- Small blog-post card project as practice

**Note:** Scrimba was not working for me, code written in the service's playground was not rendering to mini browser inside so I finished the exercise on CodePen. 

[Twitter post](https://twitter.com/DBilanoski/status/1212866805762580481)

### Day 3: January 3rd, 2020
Further down the first module of Responsive Design Bootcamp which I am now, at the second third, slowly bringing to an end. I had fun learning about CSS Specificity - something I thought I understood earlier, but really did not.

**Topics I covered:**
- Styling buttons
- CSS selectors and compounding of them
- Specificity in CSS
    - Interesting to note, CSS selectors priority is grouped in categories and when using compounding, adding of specificity points is done in those groups separately for each category
    - So, If we say that these are priority groups ranked higher to lower:
        - Inline CSS, ID, Class, Element
    - Calculation is done for each separately
        - (points for inline), (points for ID), (points for Class), (points for Element)
    - In example: 
        - `.main-page #content a {color: red}` is calculated like:
        -  (0, 0, 1, 0) + (0, 1, 0, 0) + (0, 0, 0, 1) = **(0, 1, 1, 1)**

[Twitter post](https://twitter.com/DBilanoski/status/1213229696810393600)

### Day 4: January 4th, 2020

Today I finished first module of Responsive Design Bootcamp called CSS Fundamentals and completed excercise at the and of the module. It was fun and educational but annoyance worth mentioning is frustration due to frequent interuptions during study which is something to consider when learning during weekends when everybody is at home. Looking forward to continue. 

**Topics I covered:**
- Text properties
- Font stacks
    - Interesting to note, when loading Google fonts it is faster if link is included in HTML as an stylesheet
- Inheritance
- Challenge excercise

[Twitter post](https://twitter.com/DBilanoski/status/1213563165763624963)

### Day 5: January 5th, 2020

Today I started with second module of the RWD bootcamp called "Starting to think responsively" and made it almost to the half of the module where I completed given exercise and challenge. Even though it was Sunday and I had family obligations, frequent interuptions and little to no "alone time" to actually sit and work, I am quite happy and proud of how I managed do produce more than two hours for this.

**Topics I covered:**
- CSS units in general
    - Interesting to note that pixel value in CSS is actually an absolute unit that is based in something called "Reference pixel" whose lenght is calculated to 0.23 mm (1/96 inch).
- Working with Em's & Rem's
- Width, min-width & max-width
- Basic Flexbox for simple layouting
- Challenge exercise

[Twitter post](https://twitter.com/DBilanoski/status/1213946518849433601)

### Day 6: January 6th, 2020

Today I was reading further about responsive design and played with Flexbox a lot. Also touched on media quearies and finally understood their syntax. Created simple navigation component, it was fun. Looking forward to the big challenge in course I'm currently attending.

**Topics I covered:**
- Flexbox
    - Flex direction, what it means to change it
    - Positioning commands for horizontal and vertical alignment
        - Interesting to note, those commands (`align-items` or `justify-content`) always orient themselves on main axis)
        - If we change the main axis with `flex-direction`, that change will reflect on behaviour of those commands (for example, up-down for `flex-direction: row` and left-right for `flex-direction: column`)
- Media queries sintax and basic usage
- Challenge exercise

[Twitter post](https://twitter.com/DBilanoski/status/1214314023744876550)
    
### Day 7, January 7th, 2020

Today I wrote a lot of HTML while listening to course material at the end of the second module called "Starting to think responsively where I aimned to make the end project alone before listening how the course owner did it. Lost some time on playing with CSS transitions which was a good practice and a fine refresher on transforms, transform origins and little tricks on how to style navigation links. Looking forward to continue with the challenge.

**Topics I covered**
- How to structure main navigation on the page and what is considered good practice
- Basic HTML accessibility considering structuring site elements and focus states of focusable elements
    - Interesting thing to note, regarding `<main>` tag, you need to givi it "role" to be reckognised by earlier versions of IE. In example, `<main role="main">`.
- Course challenge project progress:
    - Finished styling main navigation which is now responsive
    - Wrote all HTML for the main page

[Twitter post](https://twitter.com/DBilanoski/status/1214668268331577344)