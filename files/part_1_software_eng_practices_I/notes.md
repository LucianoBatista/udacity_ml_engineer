# Clean and Modular Code

## Production code:
Software running on production servers to handle live users and data of the intended audience. Note this is different from *production quality* code, which describes *code that meets expectations in reliability, efficiency, etc.*, for production. Ideally, all code in production meets these expectations, but this is not always the case.

## Clean:
**Readable, simple, concise**. A characteristic of production quality code that is crucial for collaboration and maintainabillity in software development.

## Modular:
Logically broken up into functions and modules. Also an important characteristic of production quality code that makes your code more organized, efficient, and reusable.

## Module:
A file. Modules allow code to be reused by encapsulating them into files that can be imported into other files.


# Refactoring code
Restructuring your code to improve its internal structure, without changing its external functionality. This gives you a chance to clean and modularize your program after you've got it working.

Since it isn't easy to write your best code while you're still trying to just get it working, allocating time to do this is essential to producting high quality code. Despite the initial time and effort required, this really pays off by speeding up your development time in the long run

# Writing Clean Code: Meaningful Names

## Tip: Use meaningful names

Be descriptive and imply type - E.g. for booleans, you can prefix with `is_` or `has_` to make it clear it is a condition. You can also use part of speech to imply types, like *verbs for functions and nouns for variables*.

Be consistent but clearly differentiate - E.g. age_list and age is easier to differentiate than ages and age.

Avoid abbreviations and especially single letters - (Exception: counters and common math variables) Choosing when these exceptions can be made can be determined based on the audience for your code. If you work with other data scientists, certain variables may be common knowledge. While if you work with full stack engineers, it might be necessary to provide more descriptive names in these cases as well.

**Long names != descriptive names** - You should be descriptive, but only with relevant information. E.g. good functions names describe what they do well without including details about implementation or highly specific uses.

Try testing how effective your names are by asking a fellow programmer to guess the purpose of a function or variable based on its name, without looking at your code. Coming up with meaningful names often requires effort to get right.

## Tip: Use whitespace properly

Organize your code with consistent indentation - the standard is to use 4 spaces for each indent. You can make this a default in your text editor.

Separate sections with blank lines to keep your code well organized and readable.

Try to limit your lines to around 79 characters, which is the guideline given in the *PEP 8 style guide*. In many good text editors, there is a setting to display a subtle line that indicates where the 79 character limit is.

For more guidelines, check out the code layout section of PEP 8 in the notes below.

# Writing Modular Code

## DRY: Don't repeat yourself

Don't repeat yourself! Modularization allows to reuse parts of your code. Generalize and consolidate repeated code in functions or loops.

## Abstract out logic to improve readability

Abstracting out code into a function not only makes it less repetitive, but also improves readability with descriptive function names. Although your code can become mode readable when you abstract out logic into functions, it is possible to over-engineer this and have way too many modules.

## Minimize the number of entities (functions, classes, modules, etc)

There are tradeoffs to having function calls instead of inline logic. If you have broken up your code into an unnecessary amount of functions and modules, you'll have to jump around everywhere if you want to view the implementation details for something that may be too small to be worth it. Creating more modules doesn't necessarily result in effective modularization.

## Functions should do one thing

Each function you write should be focused on doing one thing. If a function is doing multiple things, it becomes more difficult to generalize and reuse. Generally, if there's an "and" in your function name, consider refactoring.

## Arbitrary variable names can be more effective in certain functions

Arbitrary variable names in general functions can actually make the code more readable.

## Try to use fewer than three arguments per function

Try to use no more than three arguments when possible. This is not a hard rule and there are times it is more appropriate to use many parameters. But in many cases, it's more effective to use fewer arguments. Remember we are modularizing to simplify our code and make it more efficient to work with. If your function has a lot of parameters, you may want to rethink how you are splitting this up.

# Efficient Code

Knowing how to write code that *runs efficiently* is another essential skill in software development. Optimizing code to be more efficient can mean making it:

- *Execute faster*
- *Take up less space in memory/storage*

The project you're working on would determine which of these is more important to optimize for your company or product. When we are performing lots of different transformations on large amounts of data, this can make orders of magnitudes of difference in performance.

Sets can be very efficient when use with lots of data. One way to look for intersection between lists:

- `list(set(list1).intersection(list2))`
- `set(list1) - set(list2)`

# Documentation

Additional text or illustrated information that comes with or is embedded in the code of software.

## Types of documentation

1. **Line level**: normaly used
1. **Function or module level**: called *docstring*

Normaly assume this patterns:
*description*
"""
My description about the function

*Args*
Args:
every argument to plug in the function

*Returns*
Returns:
what your function will return
"""

1. **Project level (readme)**: 

Project documentation is *essential for getting others to understand why and how your code is relevant to them*, whether they are potentials users of your project or developers who may contribute to your code. A great first step in project documentation is your README file. It will often be the first interaction most users will have with your project.

Whether it's an application or a package, *your project should absolutely come with a README file*. **At a minimum, this should explain what it does, list its dependencies, and provide sufficiently detailed instructions on how to use it.** You want to make it as simple as possible for others to understand the purpose of your project, and quickly get something working.

Translating all your ideas and thoughts formally on paper can be a little difficult, but you'll get better over time and makes a significant difference in helping others realize the value of your project. Writing this documentation can also help you improve the design of your code, as you're forced to think through your design decisions more thoroughly. This also allows future contributors to know how to follow your original intentions.

Udacity have a 1hour course on how to write readmes files: https://classroom.udacity.com/courses/ud777


