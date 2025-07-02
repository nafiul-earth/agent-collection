# crew_tourist_guide_ollama.py

import requests

class TouristGuideAgent:
    def __init__(self, model="llama3.2", base_url="http://localhost:11434/api/generate"):
        self.model = model
        self.api_url = base_url

    def generate_prompt(self, country):
        return (
            f"You are a helpful and knowledgeable tourist guide. "
            f"A traveler is visiting {country}. Suggest 5 must-see tourist attractions in {country}, "
            f"briefly explaining why each place is worth visiting."
        )

    def suggest_spots(self, country):
        prompt = self.generate_prompt(country)
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            result = response.json()
            return result.get("response", "Sorry, I couldn't get any suggestions.")
        except requests.exceptions.RequestException as e:
            return f"Error communicating with Ollama: {str(e)}"

# Example usage
if __name__ == "__main__":
    guide = TouristGuideAgent()
    user_country = input("Enter a country name: ")
    print("\nTourist Suggestions:")
    result = guide.suggest_spots(user_country)
    print(result)


""" Enter a country name: Bangladesh

Tourist Suggestions:
Jamunot! Welcome to Bangladesh, the land of hospitality and rich cultural heritage. As your friendly tour guide, I'm excited to share with you five must-see tourist attractions that will give you a glimpse into our vibrant country's history, culture, and natural beauty.

**1. Lalbagh Fort (Dhaka)**
This 17th-century Mughal fort is one of the most iconic landmarks in Bangladesh. Built by Aurangzeb in 1678, it showcases the architectural style of the Mughal Empire and features stunning gardens, mausoleums, and beautiful mosques.

**2. Sundarbans National Park (Sonargaon)**
The Sundarbans is the largest mangrove forest in the world and a UNESCO World Heritage Site. This vast wilderness is home to Bengal tigers, crocodiles, and numerous bird species. Take a boat ride or trek through the forest to experience the unique ecosystem of this incredible national park.

**3. Ahsan Manzil (Dhaka)**
This stunning Victorian-era palace was built in 1872 for Nawab Abdul Ghalib. The intricate architecture and beautiful stained-glass windows make it a must-visit attraction in Dhaka. Take a guided tour to learn about its rich history and cultural significance.

**4. Mahasthangarh (Jhenaidah)**
Dating back to the 3rd century BCE, Mahasthangarh is one of the oldest archaeological sites in Bangladesh. This ancient fort was once a major center of trade and commerce during the reign of the Pala Empire. Explore the ruins and learn about the history of our country's early civilization.

**5. St. Martin's Island (Cox's Bazar)**
Located off the coast of Cox's Bazar, this picturesque island is a haven for nature lovers and beach enthusiasts. Enjoy stunning sunsets, pristine beaches, and vibrant coral reefs. Take a boat ride to explore the island's hidden coves, go snorkeling or diving, or simply relax in paradise.

These five attractions offer a glimpse into Bangladesh's rich history, cultural heritage, and natural beauty. As your tour guide, I'll be happy to help you plan your itinerary and make the most of your time in this wonderful country!

Shubh yatra! (Have a great trip!) """