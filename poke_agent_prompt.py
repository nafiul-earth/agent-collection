from crewai import Agent, Task, Crew, LLM
# declare different type of class we will use from crew.ai library
from langchain.tools import tool
import json

# create an object of LLM class



llm = LLM(
        model="ollama/llama3.2", # name of the model
        base_url="http://localhost:11434", # my local ollama
        stream=True  
    )
# === Agents ===

biologist = Agent(
    role='Pokémon Biologist',
    goal='Design realistic and fascinating Pokémon species with detailed habitat and typing',
    backstory='An expert in Pokémon evolution and ecology. Studied under Professor Birch.',
    verbose=True,
    llm=llm
)

historian = Agent(
    role='Pokémon Historian',
    goal='Place the new Pokémon in a mythological or historical context',
    backstory='A renowned Pokémon lore researcher with deep knowledge of ancient texts and regional myths.',
    verbose=True,
    llm=llm
)

trainer = Agent(
    role='Elite Pokémon Trainer',
    goal='Describe the strengths, weaknesses, and battle advice for the new Pokémon',
    backstory='A seasoned trainer who has won multiple regional championships and helps test new Pokémon.',
    verbose=True,
    llm=llm
)

image_prompt_agent = Agent(
    role='Pokémon Concept Artist',
    goal='Generate highly visual prompts for AI art tools like Midjourney or DALL·E',
    backstory='An imaginative designer who creates art prompts from character descriptions for concept art studios.',
    verbose=True,
    llm=llm
)

# === Tasks ===

biologist_task = Task(
    description=(
        "Generate a new Pokémon species including name, type(s), physical description, habitat, and a unique move. "
        "Include any evolutionary forms if applicable."
    ),
    expected_output="A description of a new Pokémon species with habitat, typing, and biology.",
    agent=biologist
)

historian_task = Task(
    description=(
        "Create a story or legend about the new Pokémon that ties it into the history or mythology of a fictional Pokémon region. "
        "Name the region and briefly describe its geography and culture."
    ),
    expected_output="A short story or historical account featuring the new Pokémon and the region it comes from.",
    agent=historian
)

trainer_task = Task(
    description=(
        "Offer competitive battle advice for the new Pokémon. Describe its strengths, weaknesses, best moveset, and team synergy."
    ),
    expected_output="A competitive analysis and trainer advice for using the Pokémon in battles.",
    agent=trainer
)

image_prompt_task = Task(
    description=(
        "Convert the biologist's Pokémon description into a highly detailed, vivid image prompt for Midjourney or DALL·E. "
        "Focus on visual features (size, color, shape), environment (e.g., volcano, forest), and style (anime, watercolor, pixel art). "
        "Keep it under 50 words."
    ),
    expected_output="A visual prompt for AI image generation tools like DALL·E or Midjourney.",
    agent=image_prompt_agent
)


# === Crew Assembly ===
crew = Crew(
    agents=[biologist, historian, trainer, image_prompt_agent],
    tasks=[biologist_task, historian_task, trainer_task, image_prompt_task],
    verbose=True
)


try:
    results = crew.kickoff()
    with open("result2.json", "w") as f:
        json.dump(results, f, indent=2)
except Exception as e:
    print("🔥 CrewAI LLM error:", e)

# === Output to JSON Pokédex ===

pokedex_entry = {
    "pokemon": {
        "biologist_entry": biologist_task.output.raw,
        "historian_entry": historian_task.output.raw,
        "trainer_entry": trainer_task.output.raw,
        "prompt_entry": image_prompt_task.output.raw
    }
}

# Save as JSON
with open("pokedex_entry2.json", "w") as f:
    json.dump(pokedex_entry, f, indent=2)

print("\n✅ Pokédex entry saved as 'pokedex_entry.json'")
print("\n🎨 Image Prompt for DALL·E/Midjourney:\n", image_prompt_task.output.raw)
