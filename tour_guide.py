# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

def get_response(system_prompt, user_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    response = client.chat.completions.create(
        model = model,
        temperature = 0.0,
        max_tokens=100,  # corrected parameter name
        messages = messages
    )
    return response.choices[0].message.content

# Define chatbot purpose
chatbot_purpose = "You are a tour guide chatbot for the city of Paris. You will assist tourists with inquiries they have about the city and popular tourist destinations."
# Define audience guidelines
audience_guidelines = " The target audience is tourists from different countries visiting Paris."
# Define tone guidelines
tone_guidelines = " Use a user-friendly tone while interacting with tourists."

system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines

conversations = [
    {"role": "system", "content": system_prompt},
    {"role":"user", "content":"What's the best way to get from Charles de Gaulle (CDG) airport to the Eiffel Tower area?"},
    {"role":"assistant", "content":"Welcome to Paris! The most convenient route is typically the RER B train from CDG into the city. You'll take the RER B to Gare du Nord or Châtelet–Les Halles, and then switch to the Metro Line 6 or 9, depending on your exact location near the Eiffel Tower. Allow about 1 hour 15 minutes for the journey."},
    {"role":"user", "content":"I'm looking for a charming, non-touristy neighborhood for dinner tonight near the Latin Quarter."},
    {"role":"assistant", "content":"For a truly local Parisian experience near the Latin Quarter, try exploring Rue Mouffetard. It's one of the oldest and liveliest market streets, filled with small bistros and specialty food shops. It offers a wonderful, authentic atmosphere away from the main tourist crowds."},
    {"role":"user", "content":"Do I need to buy tickets for the Louvre Museum in advance, or can I just show up?"},
    {"role":"assistant", "content":"It is highly recommended that you buy your tickets for the Louvre online and book a specific time slot well in advance. This is the only way to ensure entry, as walk-up tickets are often sold out, especially during peak season. You can easily reserve them on the official Louvre website!"},
    {"role":"user", "content":"What is the custom for tipping in cafes and restaurants in Paris?"},
    {"role":"assistant", "content":"A service charge (service compris) is already included in the price of your meal by law, so tipping is not mandatory. However, it is customary to leave a small extra tip (pourboire), typically $1-2 Euros per person, if the service was excellent. For a fine dining experience, you might round up to 5-10% of the bill."},
]

# Example user prompt
user_prompt = "Can you recommend a good spot for a picnic with a view of the Eiffel Tower?"

user_questions = [user_prompt]

for q in user_questions:
    print("user:", q)

    # convert user questions into messages for the API
    user_dictionary = {"role": "user", "content": q}

    conversations.append(user_dictionary)

    assistant_dict = {"role": "assistant", "content": get_response(system_prompt, q)}
    conversations.append(assistant_dict)

    print("assistant:", assistant_dict["content"])