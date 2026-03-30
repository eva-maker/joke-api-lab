# 🤠 Chuck Norris Joke Generator

A simple Python script that fetches a random Chuck Norris joke 
by category using the Chuck Norris API and displays it in the console.

## 🎯 Objective

- Accept a joke category from the user via console input
- Send a GET request to the Chuck Norris API
- Parse the JSON response and extract the required fields
- Display the category, creation date, and joke text in the console

## ⚙️ Implementation

The script consists of two main functions:

1. `get_joke(category)` — sends a GET request to the API, 
   parses the JSON response, and returns a joke object
2. `main()` — displays available categories, receives user input, 
   calls get_joke() and prints the result

External libraries used:
- `requests` — for handling HTTP requests

## ▶️ How to Run

Install the required dependencies:

pip install requests

Then run the script with:

python joke_api.py

## 💡 Example Output

Available categories:
animal, career, celebrity, dev, ...

Enter category: science

Category:      Science
Created at:    2020-01-05 13:42:19.104863
Joke:          Chuck Norris knows the last digit of Pi.

## 🛡️ Error Handling

- If an invalid category is entered, an appropriate warning is shown
- If the script fails to connect to the API, an error message is displayed

## 👤 Author

Created as a learning example for practicing API usage 
and JSON parsing in Python.
