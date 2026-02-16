---
date: '2025-06-23T14:00:19-04:00'
draft: false
title: 'To Overengineer a Portfolio'
---
Picture this: someone tells you "You should have a website where you can post about your projects." Some great advice right there. Two overengineered attempts later and I'm finally hitting the mark. Here's the thing I understand now that I didn't when I started. You can have a custom pretty site that looks and works exactly how you want it, but it will cost you much more time, sanity, and energy than is worthwhile. The core requirements of a site to demonstrate your work are:

- It loads instantly on everyone's device
- The **content** is instantly accessible
- The purpose of the site is clear and concise

A custom solution, and I mean custom on the level of creating a client side rendered single page application (SPA) with React, calls for you to hit all of those requirements yourself from scratch. It sounds like a simple proposition, but let me tell you, it wasn't for me.

# First Attempt - A 3D portfolio
At some point, I stumbled across [Bruno Simon's portfolio](https://bruno-simon.com/). If you've never experienced this site I highly recommend you check it out. It's basically a 3D video game, in the browser, but the level is a demonstration of Bruno's skill as a designer and front-end developer. Now this really spoke to me. I was enthralled by the experience. It felt so magical and inspiring. That's what I wanted to build. Something that was my own little corner of the internet. Something that welcomed users to my little world. I was not prepared for the amount of perfectionist traps that lay in wait in a project like that. 

Recently, I wanted to start branching out into some freelance work, so I decided to finally create my dream portfolio to showcase my skills. My experience, skills, and my desired work are not in front-end engineering. Yet I started working on a project that demonstrated a proficiency in front-end engineering. Smart.

I started by taking [Bruno Simon's course](https://threejs-journey.com/) in building sites with ThreeJS. If you're at all interested in this type of stuff I highly recommend this course. It's a one-time fee that gives you lifetime access. He's always updating the content and he's accessible in his discord community. Really it's just an insane value. It took me a few months to complete the course. I made a cursory design for my site, I modeled the assets, then I got to work developing the site itself. Dear readers, you might see a trap coming that I didn't. I had effectively no experience creating a website when I began attempting this. I couldn't even tell you what CSS was for or how to use it. It was the first website, the first react app, and the first 3D modeling project I'd ever tried. What could go wrong?

Surprisingly, the things I thought would go wrong didn't. It was the things I didn't even know could go wrong that did. I coded on this project every day for weeks. The scope creep was unreal, the architecture I had decided on was more brittle than I anticipated, and the models I had created were so heavy they caused the site to take up to 30 seconds to load. At 6 weeks, I decided to cap the features to only what was necessary to produce a beta release. This way I could get it into the hands of trusted users who could provide me real feedback. 

When I had my beta complete, I released it to a select few family and friends. If there was going to be anyone who gave my project some time, patience, and provide valuable feedback, it would be them. I wondered what they were going to say. Would they comment on the models, the physics, or any of the other exceptionally minute details that I was aware of? Nope! You know what the overwhelming piece of feedback was: "What's the point?"

_"What do you mean what's the point?!"_

Literally, my friends would load into my site (if they didn't think it was broken from the long load times), be confused as to what the point of the website was, then close it. All the other engineering that was so cool to me, didn't matter at all to end users. Remember, these are my friends. They're giving me much more leeway than a real user would. 

After I showed them what it was and how to use it I received feedback like:

- The controls are unintuitive
- The player moves too slow
- The camera doesn't move right

It's almost like an engineer who works in aerospace test infrastructure attempted to make a design heavy user experience. 

Ok but I have some feedback, I can change the site to hit what's valuable to users. Well, I suppose I could if the architecture of the site lended itself to being changed. This really surprised me. I began developing this site with 5 years of experience under my belt. I gave an honest attempt at separating concerns and building modular software. When you start anything new though, you just don't know what you don't know. In creating a React application, there were a plethora of things I didn't know I didn't know. 

The application almost demanded an entire re-write. When I finally realized that's what it would take. I decided to set it down. I was proud of some of my 3D scenes though, and I wanted to show them off on a site that was more accessible to users, more readily apparent what the point was, and easier for me to add what actually matters: the content.

# Second attempt - React, Tailwind, and MDX
After spending just an ungodly amount of time working on a project that didn't hit any mark, I decided to be much more intentional with this. I decided on a minimal layout that I could make custom with Tailwind CSS (it was inspired heavily by [paco.me](https://www.paco.me)), and I figured out how to load React Three Fiber scenes in MDX documents. The idea here was that I could have the live 3D scenes I wanted in a format that was approachable for most users. 

This worked out pretty well, except for some glaring items that would almost certainly be issues in the future.

This was the first time I used CSS (ah I see a pattern here). I think I did a pretty good job, but fiddling around with CSS to get your images or embedded scenes positioned just right misses the mark of getting content to the user.

Being a react app, the number of dependencies was gargantuan. I would always have to keep the dependencies up to date. It's not a matter of _if_ but a matter of _when_ an update breaks the application. When that occurs, I then have to spend time fixing this app instead of focusing on tasks that actually deliver value. 

Even though it looks better to me, I'm not a designer. I can't trust my instincts of what looks good to a user.

# Final implementation - Hugo and PaperMod theme
So here we are. I've finally come to a solution that is easy to maintain and proven to be accessible to users. Content is put first, the site loads fast for everyone, and the purpose of this site is clear and concise. And if I really really need a little custom flair, I can fork the PaperMod theme and enhance it. 

I learned quite a bit from this journey. Lots of neat technologies, and a whole load of lessons on what not to do. Now for any problem, I'm focusing on what will deliver the most value, not what I think the neatest solution would be.

