# Topics that will be cover here

1. Testing
1. Logging
1. Code reviews

## Testing
----------
Testing your code is essential before deployment. It helps you catch erros and faulty conclusions before they make any major impact. Today, employers are looking for data scientist with the skills to properly prepare their code for an industry setting, which includes testing their code.

- problems that could occur in DS aren't always easily detectable
- to catch these errors, you have t ocheck for the quality and accuracy of your analysis in addition to the quality of your code. 
- **Test Driven Development** is a development process where you write tests for tasks before you even write the code to implement those tasks
- **unit test** type of test that covers a "unit" of code, usually a single function, independently from the rest of the program.

## Unit Tests
---
We want to test our functions in a way that is repeatable and automated. Ideally, we'd run a test program that runs all our unit tests and cleanly lets us know which ones failed and which ones succeeded. **We have python pkgs for that.**

### Unit tests advantages and disadvantages

- Unit tests are isolated from the rest of your program, no dependencies are involved.
- They don't require access to databases, APIs, or other external sources of information.
- integration tests are the way to test large programs.


## Pytest
---
Python pkg used to do unit testing (see examples).


## Test Driven Development and Data Science
---
- Writing tests before you write the code that’s being tested. Your test would fail at first, and you’ll know you’ve finished implementing a task when this test passes.
- Tests can check for all the different scenarios and edge cases you can think of, before even starting to write your function. This way, when you do start implementing your function, you can run this test to get immediate feedback on whether it works or not in all the ways you can think of, as you tweak your function.
- When refactoring or adding to your code, **tests help you rest assured that the rest of your code didn't break while you were making those changes**. Tests also helps **ensure that your function behavior is repeatable**, regardless of external parameters, such as hardware and time.
- **Test driven development for data science is relatively new and has a lot of experimentation and breakthroughs appearing, which you can learn more about in the resources below.**

https://www.linkedin.com/pulse/data-science-test-driven-development-sam-savage/

http://engineering.pivotal.io/post/test-driven-development-for-data-science/

https://medium.com/@karijdempsey/test-driven-development-is-essential-for-good-data-science-heres-why-db7975a03a44

http://docs.python-guide.org/en/latest/writing/tests/

TDD for data science (DS) can be a bit tricky than software engineering. Data science has a fair share of exploration involved, where we are trying to find features and algorithms that will contribute best to solve the problem in hand. Do we strictly test drive all our features right from the exploratory phase, when we know a lot of them might not make into production? In the initial days of exploring how TDD fits the DS space, we tried a bunch of stuff. We highlight why we started test driving our DS use case and what worked the best for us.

Now imagine you are a logistics company and this shiny little ‘smart’ app has figured out the best routes your drivers need to pursue the following day via some sorcery. Next day is your moment of truth! The magic better work, else you can only imagine the chaos and loss it will result in. Now what if we say we can ensure that the app will always generate the most optimised route? We suddenly have more confidence in our application. There is no secret ingredient here! We can wrap up our predictions in a test case which allows us to trust the model only when its error rate is below a certain threshold.

You might ask, why would we put a model in production which doesn’t have the desired error rate at the first place? But we are dealing with real life data and predictions here, things can go haywire pretty fast. We might end up with a broken or (if you are even more lucky) no model depending on how robust the code base is. TDD can not only help us ensure that nothing went wrong while developing our model but also prompts us to think what we want to achieve and forces us to think about edge cases where things can potentially go wrong. TDD allow us to be more confident.



