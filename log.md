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
[Day 8](#day-8-january-8th-2020)
[Day 9](#day-9-january-9th-2020)
[Day 10](#day-10-january-10th-2020)
[Day 11](#day-11-january-11th-2020)
[Day 12](#day-12-january-12th-2020)
[Day 13](#day-13-january-13th-2020)
[Day 14](#day-14-january-14th-2020)
[Day 15](#day-15-january-15th-2020)
[Day 16](#day-16-january-16th-2020)
[Day 17](#day-17-january-17th-2020)
[Day 18](#day-18-january-18th-2020)
[Day 19](#day-19-january-19th-2020)
[Day 20](#day-20-january-20th-2020)
[Day 21](#day-21-january-21st-2020)
[Day 22](#day-22-january-22nd-2020)
[Day 23](#day-23-january-23rd-2020)
[Day 24](#day-24-january-24th-2020)
[Day 25](#day-25-january-25th-2020)
[Day 26](#day-26-january-26th-2020)
[Day 27](#day-27-january-27th-2020)
[Day 28](#day-28-january-28th-2020)
[Day 29](#day-29-january-29th-2020)
[Day 30](#day-30-january-30th-2020)
[Day 31](#day-31-january-30st-2020)
[Day 32](#day-32-february-1st-2020)
[Day 33](#day-33-february-2nd-2020)
[Day 34](#day-34-february-3rd-2020)
[Day 35](#day-35-february-4th-2020)
[Day 36](#day-36-february-5th-2020)
[Day 37](#day-37-february-6th-2020)
[Day 38](#day-38-february-7th-2020)
[Day 39](#day-39-february-8th-2020)
[Day 40](#day-40-february-9th-2020)
[Day 41](#day-41-february-10th-2020)
[Day 42](#day-42-february-11th-2020)
[Day 43](#day-43-february-12th-2020)
[Day 44](#day-44-february-13th-2020)
[Day 45](#day-45-february-14th-2020)
[Day 46](#day-46-february-15th-2020)
[Day 47](#day-47-february-16th-2020)
[Day 48](#day-48-february-17th-2020)
[Day 49](#day-49-february-18th-2020)
[Day 50](#day-50-february-19th-2020)
[Day 51](#day-51-february-20th-2020)
[Day 52](#day-52-february-21th-2020)
[Day 53](#day-53-february-22th-2020)
[Day 54](#day-54-february-23th-2020)
[Day 55](#day-55-february-24th-2020)
[Day 56](#day-56-february-25th-2020)
[Day 57](#day-57-february-26th-2020)


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

### Day 8: January 8th, 2020

Today I started styling the course exercise and went through most of it regarding layout, globals and typography. Looking forward to finishing the project which will probably be tomorrow. Beside the course I'm currently taking as a refresher, today I had a chance to work with Google Sheets query function more deeply which was fun.

**Topics I covered**
- Styling typography
- Collapsing margins
- Flexbox
- Code refractoring
- CSS variables
- Google Sheets `IMPORTRANGE()` and `QUERY()` functions
		- Interesting to note, `IMPORTRANGE()` can be used as a `QUERY()` argument for specifying source data but result is returned as an array
		- This means that when specifying which columns to show or filter column letters (A, B, C, etc.) are no longer valid - syntax is to write them by number as `Col1, Col2, Col3 etc.`

[Twitter post](https://twitter.com/DBilanoski/status/1215034594761809920)

### Day 9: January 9th, 2020

Today I finished main page of the course challenge without looking at solution which was a fine refresher on CSS basics and Flexbox based layouts. Found a struggle though - Mobile First aproach is not intuitive to me and I always end up doing desktop version first. Need to work on this! Later I watched what instructor did for the page and learned few tricks but nothing that my code would benefit if changed. Tomorrow I will do About page and Recents post page and conclude module 2 of the course.

**Topics I covered:**
- Mobile first aproach
		- Interestingly, this aproach is not intuitive to me and I allways end up doing desktop version fist. Need to work on this.
- Styling links with pseudo elements to create animated bottom border
- Flexbox order
- Media queries

[Twitter post](https://twitter.com/DBilanoski/status/1215402707139416071)

### Day 10: January 10th, 2020

Today I decided to redo the whole CSS of the yesterday's exercise to try the "Mobile First" approach again and reinforce it as a principle - success. After rethinking the whole process, I concluded that:
- Mobile first is actually a lot less CSS code to write initially so CSS is lighter and more simple
		- Layout for mobile devices is mostly done without event writing CSS
- When writing HTML, desktop version needs to be considered because of more complex layout

After that, I finished last video of the course second module and successfully completed exercise project using both approaches. 

I decided to include all bigger challenge project to this journal by this parameters:
- Projects will be stored in "exercises" folder
- Whenever I can, I will try to make projects as sigle files for simplicity
- When available, I will link project file to the journal entry

**Topics I covered:**
- Mobile first approach in structuring CSS
- Code refactoring

[Twitter post](https://twitter.com/DBilanoski/status/1215761357565571073)

[Challenge excercise on GitHub](https://github.com/dbilanoski/whole-year-of-code/blob/master/exercises/RWDB_01-M2_Living_the_simple_life.html)

### Day 11: January 11th, 2020

Weekend comes and biggest challenge for me becomes to catch time for learning. Today I started module 3 of the RWD course called "Stepping up your style" and got up to half of the first challenge which was fun. Looking forward to finish it tomorrow.

**Topics I covered:**
- More text properties like:
		- line-height
				- Interesting to note, even though it will take any unit, it is probably best to use "unitless" number since value here is multiplier on font-size
						- In example, if font size is set to 16px and line height to 1.6, it will calculate as 16 * 1.6
		- text-transform
		- letter-spacing
- Background-image
		- I you have text on top of image, use standard `<img>`, if not, `background-image: url("link.jpg")` is good idea

[Twitter post](https://twitter.com/DBilanoski/status/1216106160694140932)

### Day 12: January 12th, 2012

Today I was super productive - especially for one Sunday where I usually manage to sit down at a computer only later at night. Key is to avoid responsibilities :) I've managed to learn for almost 4 hours in two sittings and almost finished third module from the RWD course. For tomorrow I am leaving CSS blend modes after which I will take one day off from the course materials to study HTML forms.

**Topics I covered:**
- Flexbox order refresher
- Viewport units
- Box-sizing options
- HTML Forms - basics
- Styling forms
- CSS gradients
		- **Very** interesting thing - you can set background image to borders and with that make the border have garient background
		- Weird syntax though
				- `border-image: linear-gradient(direction, color 1, color 2) 1;` where the "1" at the and is called "Slice" value and border needs it to render image properly
- CSS transitions
- Challenge project completed, upload to journal scheduled for tommorow then I'll actually finish the module

[Twitter post](https://twitter.com/DBilanoski/status/1216481279874682880)

### Day 13: January 13th, 2020

Today I completed module 2 of Kevin Powell's RWB course where I revisited CSS blend modes. After that, I took a detour from course material to learn more about structuring forms and what is considered to be best practice for that matter. Also, played a bit with `border-image` and clipping background to text with CSS.

Tomorrow I'm continuing with course materials starting module 4 - looking forward to that.

**Topics I covered:**
- HTML forms
		- How to structure them
		- How to grup similar items into fieldsets and larger groups into sections
		- How to properly use labels and inputs to achieve accessibility
				- Interestingly, inputs can be nested into labels and still be considered best pratcice
				- Important is to match input's ID to correspodning label's "for" attribute
		- Basic styling of form elements
		- How screen readers percieve form structure and elements
		- Built an example with tutorial on [Codepen](https://codepen.io/dbilanoski/pen/JjoZapB)
- CSS border images and clip masking 
		- Border gradient with `border-image`
		- Knockout text with `background-clip: text`

[Twitter post](https://twitter.com/DBilanoski/status/1216857573200203776)

### Day 14: January 14th, 2020

Today I started a deep dive into Flexbox and went through horizontal and vertical aligment methonds both by flex parent and on child items and learnt how to control size and growth of flex child items. Super fun. Finished first challenge exercise by myself, need to check how instructor did it.

Before I started Module 4 of the RWD course, I finished CSS border-image & mask-clipping example on [Codepen](https://codepen.io/dbilanoski/pen/BayPBzQ) and saved it both as a quick refererence and as a Twitter upload CSS trick for todays post.

**Topics I covered:**
- Flex flow (`flex-direction` and `flex-wrap`)
- Flex (`flex-grow`, `flex-shrink` and `flex-basis`)
- Horizontal and vertical aligment by flex parent
		- `justify-content` and `align-items`
		- Interestingly, there is also `align-content` function
				- It will align all new rows created automaticly if `flex-wrap: wrap` by cross axis
- Horizontal and vertical aligment by flex child items
		- `align-self`, but since it works only by cross axis, when `flex-direction: column` it becomes aligment for left and right 
				- Here we use "auto" for top and bottom margins since in Flexbox "auto" on margins works for vertical aligment also

[Twitter post](https://twitter.com/DBilanoski/status/1217217370340646912)

[Challenge exercise on Codepen](https://codepen.io/dbilanoski/pen/qBEyXBP) 

### Day 15: January 15th, 2020

Today I've completed Module 4 of RWD course where I watched how instructor solved the challenge I took yesterday by myself. Learned few good tricks, especially one with present bug when trying to use `flex-basis` on images. Refractored my code to reflect that issue with implemented solution to be saved as a quick reference, and to share with Twitter folks. Will be calling it a night and use time left to relax and play some video games before sleep - good first half of the month, tommorow on to the Module 4 and CSS Grid - can't wait.

**Topics I covered:**
- Flexbox in general, practiced it on example and refreshed knowledge
- Code refractoring
- Flex-basis and issues in some edge cases
		- Interestingly, when used on image, it won't work on Chrome and Firefox (known bug)
		- To fix it, `min-width` and/or `min-height` needs to be set to 0
- Object-fit and object-position

[Twitter post](https://twitter.com/DBilanoski/status/1217568401117368322)

[Challenge excercise on GitHub](https://github.com/dbilanoski/whole-year-of-code/blob/master/exercises/RWDB_03-Card_component.html)

### Day 16: January 16th, 2020

Today I started Module 5 of the RWD course and a deep dive into CSS Grid. Now, I have tried Grid before, but never actually learned it. Went over few basic properties for setting parent-children relationship and jumped into positioning items over grid and aligning them vertically and horizontally.

Tested everything by rewriting last exercise to use Grid, managed to pull it off without issues. So far, I'm excited to learn but not sure if Grid is actually a better solution for simple layouts. I'm thinking more in terms of - Grid for big/site layout, Flexbox for simple smaller layouts.

**Topics I covered:**
- Grid, what it is and how it works
- Templating for rows and columns
- Positioning children over grid using line numbers
		- Interestingly, you can count them backward, but with negative numbers (1 to 4 -> -1 to -4)
		- With that in mind, full cover of item over all lines can be shortened by using 1 to -1
- Aligning positioned children both from parent and by self using justify and align functions

[Twitter post](https://twitter.com/DBilanoski/status/1217942649052844032)

[Challenge excercise on GitHub](https://github.com/dbilanoski/whole-year-of-code/blob/master/exercises/RWDB_04-Card_component_with_grid.html)

### Day 17: January 17th, 2020

Today I decided to pratcice what I learned yesterday and test my understaning of CSS Grid basic concepts by building component card. I spent more time than I intended looking for complex enough design which looked good - decided on shoe store product card, turned out really nice. Althought I understood Grid just fine, almost whole hour went on making responsive square box around some boxed numbers to stay in proportion. And that is how you end up after midnight, way pass intended bed time, and with missed push to Github.

**Topics I covered:**
- Challenge exercise to test my Grid understanding
		- CSS Grid basic templating conceptcs
		- Aligning items horizontally and vertically
		- Chaning layout in media queries
- How to make responsive square with borders around element whose content varies
		- Interesting solution described [here](https://spin.atomicobject.com/2015/07/14/css-responsive-square/)

[Twitter post](https://twitter.com/DBilanoski/status/1218318445365944321)

[Challenge excercise on Codepen](https://codepen.io/dbilanoski/pen/GRgYENj?editors=1100)

### Day 18: January 18th, 2020

Today I knew there will be an hour at best of free time so I planned my hour properly - fix issue with product image and refactor some code from yesterday's project, then go through Free Code Camp and finish basic CSS module of Responsive Web Design certification - check, check and check.

**Topics I covered:**
- CSS custom properties (variables)
- Specificity in CSS
- Basic CSS functions, mostly all of them
- Code refactoring

[Twitter post](https://twitter.com/DBilanoski/status/1218621599340994563)

### Day 19: January 19th, 2020

Today I continued with Responsive Web Design Course, Module 5, CSS Grid where I learned about Grid Areas, implementation in media queries and new units. Wanted to start a new project to exercise newly learnt but I was too tired and got sick earlier so with sore throat I am calling this a night.

**Topics I covered:**
- Implicit & Explicit grid and how to set size on implicit grid items
- CSS Grid Areas
		- Super useful, especially in media queries where you only need to redefine parent's code
- Grid units
		- minmax(), fr, min-content, max-content
		- Interestingly, you can't use fr unit as minimum in minmax()

[Twitter post](https://twitter.com/DBilanoski/status/1218990421503815680)

### Day 20: January 20th, 2020

Today was more theoretical then "hands-on" - I completed module 5 of the RWD Course but since I caught a nasty cold, wasn't able to sit for longer periods of time at my computer so I postponed challenge project for tommorow, finished "Applied Visual Design" module on Free Code Camp an tought myself how to animate a [heartbeat](https://codepen.io/dbilanoski/pen/wvBQQyJ) with CSS.

**Topics I covered:**
- CSS Grid
		- repeat() function
		- how to use it with Auto-fit & Auto-fill
		- Auto-fill is interesting, it will continue to add new columns eventhough they are blank and not declared in the markup
- CSS in general
		- animations
		- apsolute positioning
		- gradients and different ways of declaring colors
- Color theory basics

[Twitter post](https://twitter.com/DBilanoski/status/1219379689443282944)

### Day 21: January 21st, 2020

Today I finally started with final challenge project form RWD course, wrote HTML for homepage, started styling it and after I wrote all resets, typography, some styles and started with layout, I realised that I constructed that whole page with Flexbox in mind. Rewroted HTML, wrote Grid layout and called it a night. Also, spent more than hour to find usable assets online since Scimba: 
- is not allowing to download images instructor used
- is still unusable.

**Topics I covered:**
- Writing bigger project from scratch
- How to plan a layout
		- Considering Flexbox
		- Considering Grid
- Flexbox & Grid layout
- Basic CSS styles
- Code refactor

[Twitter post](https://twitter.com/DBilanoski/status/1219761005510713344)

### Day 22: January 22nd, 2020

Refactored project from yesterday with more CSS Grid in mind, wrote styles, finished layout and completed homepage of the project. I wrote few lines of JavaScript to enable mobile navigation toggle and enjoyed that more than the rest of the page. Two things I need to do more:
1. Build more complicated projects with CSS Grid and Mobile First approach
2. Get back to JS as soon as possible

**Topics I covered:**
- Writing bigger project from scratch
- How to plan a layout considering Grid
		- Interstingly, and since you still need containers, with grid you need a "hack" to achieve them
		- What I did was `grid-template-columns: minmax(1rem, 1f) (page content setup) minmax(1rem, 1f)`
				- so, minimum 1em on the sides and grows if viewport is wider, minmax for the content also to desired max width
- Grid layout with mobile first approach
- Code refactor
- JS click event listeners with classlist toggle

[Twitter post](https://twitter.com/DBilanoski/status/1220119418560221186)

### Day 23: January 23rd, 2020

Today I watched how instructor did the landing page from previous challenge. Found out few things about my approach and what I need to practice more:
- Consistent and pactical naming convention
- CSS Grid - my was kind of more complex and maybe unnecessary
		- Yes, I wanted to push it as a practice but padding and margins are just fine for spacing things out
- Typography
		- Need to learn defaults so I can be more efficient
		- Find good reset where most defaults are usable
Refactored parts of my code but did not changed main logic, that's all mine ;)
Need to find better way of uploading code (images are problematic when I use offline, don't want to put folders here).

**Topics I covered:**
- Code reactoring
- Positioning in CSS
- Grid layout functions
		- Interestingly, Grid child elements can also be arranged with `order`, just like Flex child elements

[Twitter post](https://twitter.com/DBilanoski/status/1220469940249137152)

### Day 24: January 24th, 2020

Eventhought I initially wanted to skip this, today I styled About page of the course final challenge project to test my CSS Grid understanding and to test CSS Grid reusability. It was fun, fiddled with styling letters more than I thought I would. Started "Applied Accessibility" module of the FreeCodeCamp RWD course.

Tomorow I might finish Scriba course and focus on FreeCodeCamp curriculum to try to finish it by the end of the month.


**Topics I covered:**
- CSS Grid reusability
- Grid layout functions and aligning items
		- Realised it is good idea to create "gaps" between items with margins, empty grid rows was a good exercise but ultimately more CSS needs to be written and I didn't like empty blocks, even layout wise where there is no HTML and `grid gap` functionality is not a great solution if you simulate container boxes with empty columns
- Box-shadow and text-shadow properties in CSS

[Twitter post](https://twitter.com/DBilanoski/status/1220842123773337600)

### Day 25: January 25th, 2020

Today I barely found time during the day and finally managed to sit down at my computer little past midnight where I finished Contact page of RWD course final challenge project and now whole site is complete. Tomorrow I will wrap up with the course, review it and attack FreeCodeCamp curriculum.

**Topics I covered:**
- Writing and styling contact form
- CSS Grid reusability
- Textarea element
		- Interestingly, `<textarea>` needs a closing tag, while other input elements don't. Without it it will "eat" rest of the HTML and display it as part of the textarea element effectively braking the site.

[Twitter post](https://twitter.com/DBilanoski/status/1221230384094023680)

### Day 26: January 26th, 2020

Today I completed Kevin Powell's Responsive Web Design Bootcamp at Scrimba and while content-wise it was really a blast and a fine dive into responsive design with inspiring and enjoyable instructor, platform itself left much to be desired. Watched instructor solution to final challenge project, refactored mine a little, fixed some spacing issues and pushed project here to journal as a reference.

**Topics I covered:**
- CSS Grid reusability
- CSS Grid layout functions and aligning items
- Code refactoring

[Twitter post](https://twitter.com/DBilanoski/status/1221557275082530816)

[Challenge excercise on GitHub](https://github.com/dbilanoski/whole-year-of-code/blob/master/exercises/RWDB_05-Final-Marketing_agency/)

### Day 27: January 27th, 2020

Today I went through "Applied Accessibility" module of the FreeCodeCamp RWD course and completed it. Also, installed Wakatime VS Code extention and configured it.

**Topics I covered:**
- Semantic value and role of HTML5 elements:
		- header, footer, article, section, main, audio and figure
- Forms and how to properly structure them
		- label & inputs
		- fieldsets & legend
		- date type of input
- Date & time tags
- Some attributes that can play role in accessibility (tabindex, accesskey)
		- Interestingly, `accesskey="letter"` attribute on an html tag defines shortcut key that will activate that tag if it's interactable
		- Seems useful on navigation for keyboard only-users 

[Twitter post](https://twitter.com/DBilanoski/status/1221914595566260232)

### Day 28: January 28th, 2020

Today I completed FreeCodeCamp "Responsive Web Design Principles" module and short free UI Design Course by Gary Simon on Scrimba which was super fun. Plan is to complete all modules from FreeCodeCamp up to certification projects and start with Wesbos's Grid course on Youtube by the end of the month.

**Topics I covered:**
- Vh, Vw, Vmin, Vmax units
- Responsive images and typography
- UI Design fundamental concepts:
		- Whitespace
		- Color
		- Contrast
				- Interestingly, there is a standard for good contrast ratios defined under the Web Content Accessibility Guidelines 2.0.
				- Good read [here](https://webaim.org/articles/contrast/) 
		- Scale
		- Alignment
		- Typography
		- Visual Hierarchy

[Twitter post](https://twitter.com/DBilanoski/status/1222292754786590726)

### Day 29: January 29th, 2020

Today I completed Flexbox module and Grid module on FreeCodeCamp and got to the challenge projects which I will start tomorrow. Started Wes Bos's CSS Grid course on Youtube, went through fundamentals.

**Topics I covered:**
- Flexbox basics
- CSS grid basics
- CSS implicit and explicit grid
		- what they are, how to size and control them
- Firefox DevTools
		- Interestingly, grid lines there are changing in regard to grid type
		- Explicit grid will be bordered with solid lines and crossed with dashed lines with full opacity while implicit will be drawn with semi opaque dotted lines

[Twitter post](https://twitter.com/DBilanoski/status/1222643660094832640)

### Day 30: January 30th, 2020

Today I completed first of five design projects from Free Code Camp Responsive Web Design course where I built Mr. Spock tribute page with five cool fact about the character. Score - 10 of 10 from first try. 

**Topics I covered:**
- Figures, blockquotes and articles
- Basic CSS styling and layouting
- Flexbox
- Pseudoelements

[Codepen project](https://codepen.io/dbilanoski/pen/vYEqyqg)

[Twitter post](https://twitter.com/DBilanoski/status/1223012884025872390)

### Day 31: January 31st, 2020

Today I started second of five design projects from Free Code Camp Responsive Web Design course where I wrote HTML for Survey form, but wanted to learn HTML tables along the way and complicated form's layout a bit. This resulted with struggle to successfully complete project conditions which are too simple in calculation.

Since it's not finished, I'll add project link tommorow.

**Topics I covered:**
- Forms
- Tables

[Twitter post](https://twitter.com/DBilanoski/status/1223380209321246725)

### Day 32: February 1st, 2020

Today I completed second of five design projects from Free Code Camp Responsive Web Design course where I built a survey form, made it complex and practiced with tables a bit. Regardless of headcache and fever I was having today, I've managed to complete this challenge.

**Topics I covered:**
- Forms
- Tables
- Code refactor

[Twitter post](https://twitter.com/DBilanoski/status/1223741866396540928)

[Codepen project](https://codepen.io/dbilanoski/pen/VwYJgjJ)

### Day 33: February 2nd, 2020

Today I decided to take a day off - well earned and really needed. But, for it to not be empty challenge wise, little code refactor on yesterday's form, some sorting on CodePen & a good read on color theory. Also, wrote few lines of JavaScript to clear form input fields and alert user upon submiting form with poput message - felt really good.

**Topics I covered:**
- Code refactor
- Some JavaScript
		- Event listeners
		- Arrow functions
- Color theory
		- Good read about the basics [here](https://99designs.com/blog/tips/the-7-step-guide-to-understanding-color-theory/) 

[Twitter post](https://twitter.com/DBilanoski/status/1224087067820462081)

### Day 34: February 3rd, 2020

Today I started third FCC Responsive Web Design project called "Landing page" where I decided on the theme, found most of the assets, planned out layout and wrote all markup. Played a bit with the colors and went to sleep half hour earlier than usual. Good day.


**Topics I covered:**
- Planning a small project
		- Deciding on theme, finding assets
		- Planning layout, making content up
- HTML of landing page
		- Page structure elements, Iframe, form
		- Interestingly, while planning a layout and page structure, I intuitively wrote desktop version first. **Gotta start thinking responsive**.
- Color sheme planning

[Twitter post](https://twitter.com/DBilanoski/status/1224463239561564160)

### Day 35: February 4th, 2020

Today I continued with landing page project from FCC RWD. Refractored classes to start with mobile first and spent most of the time positioning hero section elements,figuring out why sticky positioning is not working and tweaking colors.


**Topics I covered:**
- Sticky position in CSS (really understood it)
		- Interestingly, you can't specify which element will be "parent" element for sticky element, it's always the parent element so it's best to plan markup accordingly
- Absolute positioning
- Typography styling
- CSS resets
- Background images, positioning and blend modes 

[Twitter post](https://twitter.com/DBilanoski/status/1224831356892520448)

### Day 36: February 5th, 2020

Continued with landing page project form FCC RWD, styled most of the sections and almost completed mobile view. Need to fix iframe size, decide on font family for section titles and sort some minor typography issues - then desktop size styles, all of that tomorrow.

**Topics I covered:**
- Flexbox layout
		- Interestingly, and I knew this but manage to forget it again - there is a bug in modern browsers when image becomes flex item - flex basis will not affect it. To overcome this, min-width or min-height, depending on whichever is causing the issue (best to put them both), needs to be set to zero.
- Typography styling
- Object-fit & Object-position
- Styling form elements
- Mobile first approach

[Twitter post](https://twitter.com/DBilanoski/status/1225182773658505217)

### Day 37: February 6th, 2020

Completed third FCC Responsive Web Design project, created landing page for pizzeria with some Borderlands flavor ;) Code refactor is needed but initial score was 16/16 which was cool. 

**Topics I covered:**
- Flexbox layout
- From mobile view to desktop view styles
- Media queries
- Typography styling
- Styling form elements

[Twitter post](https://twitter.com/DBilanoski/status/1225558011827171329)
[Codepen project](https://codepen.io/dbilanoski/pen/yLNLQpK)

### Day 38: February 7th, 2020

Today I worked on mobile toggle button and dropdown navigation menu on my landing page project. Wrote hamburger menu with CSS, animated it, fixed navigation items and set them up to slide down and wrote some JavaScript to make it work. Gonna take the rest of the night off to watch some movies with my wife.

**Topics I covered:**
- Mobile navigation
- Hamburger menu with CSS
- Apsolute and realtive positioning
- JavaScript
		- Functions and Event listeners
		- If statements

[Twitter post](https://twitter.com/DBilanoski/status/1225877759496540160)

### Day 39: February 8th, 2020

Today I had few runs with CSS Grid whenever I got some spare time and managed to fully complete my landing page project where mobile navigations now works perfectly fine. Going to bed earlier to catch some sleep finally.

**Topics I covered:**
- Animating transitions with CSS
- Some basic problem solving with JavaScript
- Explicit & implicit CSS Grid
- How to size auto rows and auto colums
- Spaning grid items on the grid
- Emmet
		- Super powerfull. Needed 20 divs with class names "item item[div number]" where every one has text content with that div's number. Did it by writing `.item.item${$}` and "tab". Pure magic ;) 

[Twitter post](https://twitter.com/DBilanoski/status/1226269078932934656)

### Day 40: February 9th, 2020

Today I had some time during the day but later at night I was simply too tired. Managed to squize almost two hours and invested them in learning more of CSS Grid by following [Wes Bos's Youtube Course](https://www.youtube.com/watch?v=rBoveH7tdJU&list=PLu8EoSxDXHP5CIFvt9-ze3IngcdAc2xKG&index=18). Got right to exercises which I will do tomorrow.

**Topics I covered:**
- CSS Grid Template Areas
- Naming lines
- Auto-flow options and usefull "dense" option
		- Gotta try to make gallery using this
- Alignment, centering and reordering grid items

[Twitter post](https://twitter.com/DBilanoski/status/1226624405729619968)

### Day 41: February 10th, 2020

Worked on a cool CSS Grid Galery concept that I saw in Wes Bos's Grid Course and completed it mostly - little code refactor tomorrow and some style changes. Wanted to practice CSS Grid, mostly wrote JavaScript :)

**Topics I covered:**
- CSS Grid basic positioning
- CSS Grid overlaping items
- JavaScript
		- Event listeners
		- Functions
		- Creating DOM elements
		- Adding class names to DOM elements
		- Traversing the DOM
		- Event delegation
		- Creating random numbers
		- Working with arrays
		- High order array methods (map())

[Twitter post](https://twitter.com/DBilanoski/status/1227015455627456512)

### Day 42: February 11th, 2020

Completed collage/mosaic photo gallery I was working on from Wes Bos's Youtube grid course, added functionality to close the image modal by clicking outside of the modal box same as by clicking on the close button, refactored a little and prepared Codepen pen with the project.

Went on with the CSS Grid course, watched a fine comparison between Flexbox and Grid and when each might be a better option - didn't know that Flexbox "grow" property can be animated with CSS while grid properties can't.

**Topics I covered:**
- Javascript
	- Event listeners, event delegation
	- Adding class names to DOM elements
- CSS Grid & Flex-box
	- Flex grow usage
	- Horizontal and vertical alignment
	- Basic positiong with both technologies
- Code refactoring

[Twitter post](https://twitter.com/DBilanoski/status/1227359063022940163)

[Codepen project](https://codepen.io/dbilanoski/pen/bGdVdQJ)

### Day 43: February 12th, 2020

Worked on a Codepen clone throughtout the day as a CSS Grid practice, ended up with Flexbox in few places but overall I'm quite happy with the project. Little code refactor for tomorrow to make it all CSS Grid and few sizing issues. Thinking about creating GitHub repo for clone sites and try to do one per month, something like "CSS Cardio".

**Topics I covered:**
- Building clone site from scratch
- CSS Grid positioning
- Flexbox positioning
- CSS custom properties

[Twitter post](https://twitter.com/DBilanoski/status/1227726648625311747)

### Day 44: February 13th, 2020

Completed my little CodePen clone project, decided to leave Flexbox where it seemed to fit better, fixed minor sizing issues and added mobile view styles and layout changes. Spent most time writing JavaScript to enable chosing which editor will be visible, stayed far longer then I intended so GitHub repo will bi topic for tomorrow.

**Topics I covered:**
- Code refactoring
- Making HTML elements resizeable
- Making HTML elements editable
- CSS & Flexbox layout tools
- JS
	- Event listeners
	- Event delegation
	- Query selectors
	- For each and Find array methods

[Twitter post](https://twitter.com/DBilanoski/status/1228101341236662272)


### Day 45: February 14th, 2020

Today I worked on my CSS Cardio idea and created corresponding Git Hub repo, added guides, rules and my first clone project. Idea is to write a clone of existing website from scratch without looking at the source code.

Since I did most of the work during the day and for the evening I had other plans (Valentine's Day), simply didn't managed to write here and to Twitter. So, two entries today, this one for yesterday, and one later for today. 

**Topics I covered:**
- Markdown basics
	- Images, links, headings, blockquotes etc.
- Basic Git syntax
- CSS Grid and Flexbox

[Twitter post](https://twitter.com/DBilanoski/status/1228644277007376384)

[CSS Cardio: Web Clones Repo](https://github.com/dbilanoski/css-cardio-web-clones)

### Day 46: February 15th, 2020

Today I had little time and didn't code that much but I went through rest of Wes Bos's CSS Grid course examples and played a bit with configuring auto positioning with grid. Also, finished CSS Cardio project documentation and uploaded everything to GitHub. Next stop - last two FreeCodeCamp exercises to complete Responsive Web Design certification.  

**Topics I covered:**
- CSS Grid layout tools

[Twitter post](https://twitter.com/DBilanoski/status/1228781698550292482)

### Day 47: February 16th, 2020

Today I started working on the fourth FreeCodeCamp certification project "Build a Technical Documentation Page". Decided on topic (CSS Selectors), prepared all materials, wrote content and started with HTML. Played a bit with `<details>` tag for expandable navigation and sorted all sections.

**Topics I covered:**
- Planning new project and preparing assets and content
- CSS Selectors
- HTML `<details>` tag

[Twitter post](https://twitter.com/DBilanoski/status/1229182742493122564)

### Day 48: February 17th, 2020

Continued working on my technical documentation project and finally completed the markup. It was a whole bunch of data and for the reference page, which is basicly a table of selectors, I've managed to convert my data to JSON, then parse it to JS object and wrote a little function to populate the table which saved me from writing about 250 lines of HTML. Yeah, good job.

**Topics I covered:**
- HTML table
	- thead, tbody, tr, td
- JSON
	- Converting CSV data to JSON
- JavaScript
	- Parsing JSON to JavaScript object
	- forEach array method
	- Template literals (strings)
	- Dynamic population of HTML with data from JSON object

[Twitter post](https://twitter.com/DBilanoski/status/1229540619124723713)

### Day 49: February 18th, 2020

Today was a long day. Managed to style some of the tech documentation project page during the day but evening completely went to tedious client work of manually entering markup data for cosmetics store static web page.

**Topics I covered:**
- Tedious data entry
- Basic HTML, CSS and Flexbox
- CSS Grid layouting

[Twitter post](https://twitter.com/DBilanoski/status/1229907010226921480)

### Day 50: February 19th, 2020

Another long day - managed to follow up and finish with client work during the day and cleared my evening for FCC tech documentation page project. Finished styling the page, need to tweak some colors and program the mobile navigation toggle which I'll do tomorrow.

**Topics I covered:**
- CSS Grid
- CSS Flexbox
- Working with tables
	- Forgot again, to achieve uninterrupted borders on table inner elements, element table needs a `border-collapse: collapse` entry.

[Twitter post](https://twitter.com/DBilanoski/status/1230276263958503424)

### Day 51: February 20th, 2020

Completed the FreeCodeCamp's fourth challenge project for Responsive Web Design Certification - a Technical Documentation Page. Decided to cover the topic of CSS Selectors, used MDN and W3C pages for content source and inspiration and worked on my design which turned out nicely. Next and final project - Personal Portfolio.

**Topics I covered:**
- Basic CSS
- Pseudo Elements
- Code refactoring

[Twitter post](https://twitter.com/DBilanoski/status/1230628383475806214)

[Codepen project](https://codepen.io/dbilanoski/full/vYOXMNp)

### Day 52: February 21th, 2020

Slow and unproductive day - I looked few solutions to mobile navigation animations and fiddled a bit with some examples but ultimately didn't do much. Tomorrow. 

**Topics I covered:**
- Pseudo elements
- Styling and animating mobile navigation

[Twitter post](https://twitter.com/DBilanoski/status/1230989921063751682)

### Day 53: February 22th, 2020

Had a little time today but managed to complete imagined transition for mobile navigation, test out `skew` and `rotate3d` CSS properties and read a little about CSS Stacking Context. 

**Topics I covered:**
- Pseudo elements
- Styling and animating mobile navigation
- CSS Transform options
	- Skew, skew3d, rotate, rotate3d, translate
- JS
	- toggle function
- CSS stacking context (intro)

[Twitter post](https://twitter.com/DBilanoski/status/1231375740312203264)


### Day 54: February 23th, 2020

Tweaked yesterday's navigation project a bit and animated toggle button to go with the flow of the main animation. Studied CSS stacking context more, revieved CSS positioning and started planning the last FCC project.

**Topics I covered:**
- CSS non-static positioning
- CSS Stacking Context
	- Interestingly, all transition properties, opacity and declaring z-index on flexbox and grid child items will create new stacking contexts
- Project planning
	- Colors, fonts, layout, assets

[Twitter post](https://twitter.com/DBilanoski/status/1231702536471617536)


### Day 55: February 24th, 2020

Prepared all assets and wrote markup for the Personal Portfolio project of FreeCodeCamp Responsive Web Design certification.

**Topics I covered:**
- Planning new project and preparing assets and content
- Basic HTML elements, HTML forms 

[Twitter post](https://twitter.com/DBilanoski/status/1232067451447398401)


### Day 56: February 25th, 2020

Started styling the Personal Portfolio project, structured basic grid with container max width, completed landing page and navigation, animated transitions, wrote basic layout rules for about section article. 

**Topics I covered:**
- CSS reset
- Styling typography
- CSS Grid
- `:not()` pseudo-class
	- Super usefull, for example when I want to set top margins on all items except first in container, no need for separate selectors, `p:not(:first-of-type) {margin-top: 1rem;}`

[Twitter post](https://twitter.com/DBilanoski/status/1232438806122356738)

### Day 57: February 26th, 2020

Continued working on the Personal Portfolio project, completed about section and projects section, animated project cards, wrote some JavaScript for navigation. Having second thought about used images so tomorrow, more work with assets.

**Topics I covered:**
- Styling typography
- CSS Grid and Flexbox
- CSS transitions
- Object-fit, manipulating images

[Twitter post](https://twitter.com/DBilanoski/status/1232799241149538305)





