![firekeep-logo](firekeep-logo.png)

Firekeep is a Flask app that follows Domain-Driven Design, Repository, Service Layer, and CQRS patterns. For educational purposes only. 


## Motivation

I first learned of the CQRS pattern while learning to code in Go. As I went on exploring, I learned of Domain-driven Design, more of the SOLID principles and design patterns. **Btw, I'm not an expert in Golang, DDD, SOLID, or software design patterns. My code and writing will obviously show that. Please forgive my ignorance.** I want learn how to do this with Python. So here it is.

Currently using this book for studying: *Architecture Patterns with Python: Enabling Test-Driven Development, Domain-Driven Design, and Event-Driven Microservices* by HJW Percival & B Gregory.

## Expected FAQs

1. *Hah! You're applying a pattern for enterprise softwares to a puppy project. Whats the point, man???*

Ans. Hah! There's actually no point! I'm just wasting my time learning design patterns which I probably will never use!

2. *What does the application do anyway?*

Ans. Pleae read the [About the Application](#about-the-application) section below.

3. *I dont think thats the CQRS pattern...(with his/her `Optional[explanation]`)*

Ans. Thank you for taking the time to share your knowledge to me. Glad you are here.

4. *Why named this Firekeep?*

Ans. I initially intended for Firekeep as a name for a validation library I was supposed to build. Well, plans changed, and I am now developing it as a component of this Flask app.

## About the Application

This is a dormitory room management. A REST API built with Flask is the primary goal for its entry point but I will try to keep it *decoupled in a good way* to allow other means: CLI, GUI.

The domain may not be that complex but I believe this will be a good start and exercise.

