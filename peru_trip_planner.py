

import os

from dotenv import load_dotenv
from groq import Groq


# ============================================================
# 1. CONNECT TO GROQ
# ============================================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY NOT FOUND")

client = Groq(api_key=api_key)

model = "qwen/qwen3.6-27b"


# ============================================================
# 2. AI ROLE
# ============================================================

system_prompt = """
You are a luxury Peru trip planner.

Your job is to create personalized,
detailed and practical travel itineraries for Peru.

Focus on:

- luxury experiences
- beautiful hotels
- great food
- history and culture
- nature
- comfortable transportation
- staying within the user's budget

Create a day-by-day itinerary based on
the user's travel preferences.

Use the budget calculations provided by the
Python program. Do not change or invent the
calculated totals.
"""


# ============================================================
# 3. GET TRIP DETAILS
# ============================================================

days = input("How many days are you travelling? ")

budget = input("What is your budget in rupees? ")

travelers = input("How many people are travelling? ")

interests = input("What are your interests? ")


# ============================================================
# 4. GET ESTIMATED COSTS
# ============================================================

flight_cost = float(input("Estimated flight cost: "))

hotel_cost = float(input("Estimated hotel cost: "))

food_cost = float(input("Estimated food cost: "))

transport_cost = float(input("Estimated transport cost: "))

activity_cost = float(input("Estimated activities cost: "))


# ============================================================
# 5. CALCULATE BUDGET
# ============================================================

total_spent = (
    flight_cost
    + hotel_cost
    + food_cost
    + transport_cost
    + activity_cost
)

remaining_budget = float(budget) - total_spent


# ============================================================
# 6. CREATE THE AI PROMPT
# ============================================================

prompt = f"""
Plan a luxury trip to Peru.

Trip details:

- Number of days: {days}
- Budget: ₹{budget}
- Number of travelers: {travelers}
- Interests: {interests}

Estimated costs:

- Flights: ₹{flight_cost}
- Hotels: ₹{hotel_cost}
- Food: ₹{food_cost}
- Transport: ₹{transport_cost}
- Activities: ₹{activity_cost}

The Python program has calculated:

Total spent: ₹{total_spent}
Remaining budget: ₹{remaining_budget}

Create a detailed day-by-day itinerary.

Include:

- luxury accommodation
- food experiences
- historical and cultural places
- nature experiences
- comfortable transportation

At the end, show:

1. Total estimated spending
2. Original budget
3. Remaining budget

IMPORTANT:

Use the exact budget calculations provided above.
Do not change the total spent or remaining budget.
"""


# ============================================================
# 7. ASK THE AI
# ============================================================

response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7
)


# ============================================================
# 8. GET AI RESPONSE
# ============================================================

answer = response.choices[0].message.content


# ============================================================
# 9. PRINT ITINERARY
# ============================================================

print("\n🇵🇪 YOUR LUXURY PERU ITINERARY 🇵🇪\n")

print(answer)


# ============================================================
# 10. PRINT REAL PYTHON BUDGET CALCULATION
# ============================================================

print("\n💰 BUDGET SUMMARY")
print("----------------------")

print(f"Original budget: ₹{float(budget):,.2f}")

print(f"Total spent: ₹{total_spent:,.2f}")

print(f"Remaining: ₹{remaining_budget:,.2f}")

