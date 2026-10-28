# Exercise 1: Understanding Object-Oriented Programming

Name: Kazi Zahir
Course: ISM 3232

## Question 1: What is a class?

A class is basically a blueprint that tells Python what an object should have and what it can do. For example, our SupportChatbot class defines the chatbot’s name, instructions, and conversation history. It also contains methods that allow the chatbot to respond to customers.

## Question 2: What is an object?

An object is something we create using a class. Each object can have its own information and perform the actions defined by its class. For example, when we created Sunny using the SupportChatbot class, Sunny became an object with its own name and conversation history.

## question 3: what is an atribute 
An object is something we create using a class. Each object can have its own information and perform the actions defined by its class. For example, when we created Sunny using the SupportChatbot class, Sunny became an object with its own name and conversation history.

## question 4: what is a method?
A method is a function inside a class that allows an object to perform an action. For example, our SupportChatbot class has a respond() method that takes a customer’s message, chooses a response, and saves the conversation history.

## what is compostion? 
Composition is when one class uses an object from another class to perform a task. For example, our SupportChatbot uses the OrderLookup object to find order numbers and check their statuses. This allows each class to focus on its own responsibilities.

## what does self mean in python? 
self refers to the specific object that is using a method. It allows the object to access its own attributes and methods. For example, self.name refers to the chatbot’s name, while self.history refers to its conversation history.