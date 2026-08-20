# 🇵🇪 Luxury Peru Trip Planner

I really love travelling, so I wanted to build a small project around something I genuinely enjoy.

That's how this Peru Trip Planner came to life.

I wanted to combine my interest in travel with what I've been learning about LLMs and Python,so I built a mini AI travel planner using a Groq-powered LLM that creates personalized luxury itineraries based on the user's trip duration, budget, number of travelers, and interests.

But there's one thing I didn't want the planner to ignore: **money.**

Because, obviously, budget is something we all think about when planning a trip ,so instead of letting the LLM handle the calculations, I used Python to calculate the estimated spending and remaining budget.

The idea is simple:

**You tell the planner what kind of trip you want → Python handles the numbers → the LLM turns it into a personalized itinerary.**

---

## ✨ What It Does

The planner takes:

- Number of travel days
- Budget
- Number of travelers
- Travel interests
- Estimated flight cost
- Estimated hotel cost
- Estimated food cost
- Estimated transport cost
- Estimated activity cost

It then:

- Calculates total estimated spending
- Calculates the remaining budget
- Sends the trip details to the LLM
- Generates a personalized day-by-day luxury Peru itinerary

---

## 🧠 The Idea Behind It

While learning about LLM applications, I wanted to understand where an LLM is useful and where regular Python makes more sense.

So I kept the responsibilities simple:

**Python →** handles the budget calculations

**LLM →** understands the travel preferences and creates the itinerary

This keeps the arithmetic deterministic instead of relying on the LLM to calculate the numbers.

---

## 🛠️ Tech Stack

- Python
- Groq API
- Qwen 3.6 27B
- python-dotenv

---

## 💰 Budget Calculation

The program calculates:

Total Spent = Flights + Hotels + Food + Transport + Activities

Remaining Budget = Original Budget - Total Spent

For example:

Budget: ₹6,00,000

Flights: ₹1,20,000  
Hotels: ₹1,80,000  
Food: ₹60,000  
Transport: ₹40,000  
Activities: ₹50,000  

Total Spent: ₹4,50,000  
Remaining Budget: ₹1,50,000

> **Note:** The costs in this version are estimates entered by the user. The project does not currently fetch live flight or hotel prices.

---

## 🚀 How to Run

### 1. Install the dependencies

Make sure Python is installed.

Run:

pip install -r requirements.txt

### 2. Add your Groq API key

Create a `.env` file in the project folder.

Add:

GROQ_API_KEY=your_api_key_here

Your `.env` file is included in `.gitignore`, so your API key will not be uploaded to GitHub.

**Never share or commit your actual API key.**

### 3. Run the planner

Run:

python peru_trip_planner.py

The program will ask for your trip details and estimated costs.

Example:

How many days are you travelling? 7  
What is your budget in rupees? 600000  
How many people are travelling? 2  
What are your interests? luxury hotels, food, history, nature  

Estimated flight cost: 120000  
Estimated hotel cost: 180000  
Estimated food cost: 60000  
Estimated transport cost: 40000  
Estimated activities cost: 50000

Python calculates the budget, and the LLM then uses those details to generate the itinerary.

---

## 📌 Example Output

Original Budget: ₹6,00,000  
Total Spent: ₹4,50,000  
Remaining Budget: ₹1,50,000

The calculated budget is provided to the LLM along with the travel preferences.

The result is a personalized day-by-day luxury Peru itinerary.

---

## 🔄 How It Works

User Input  
↓  
Trip Preferences + Budget  
↓  
Estimated Travel Costs  
↓  
Python Budget Calculation  
↓  
Total Spent + Remaining Budget  
↓  
Groq / Qwen LLM  
↓  
Personalized Peru Itinerary

The main idea is to let each part do what it is good at:

**Python →** calculations and program logic

**LLM →** travel planning and personalized itinerary generation

---

## 🔮 What's Next?

This is a mini project for now, but I'd love to take it further.

Some ideas for future versions:

- Real-time flight and hotel prices
- Currency conversion
- Weather information
- Travel APIs
- Tool calling
- Structured itinerary output
- A simple web interface
- Expanding the planner to more destinations

For now, it's a small project that combines **something I genuinely enjoy — travelling — with something I'm learning — building applications with LLMs.**

And honestly, that's what made it fun to build as well.



