# poke_ball_agent.py

from crewai import Agent, Task, Crew,LLM


# 1. Use Ollama Local LLM
llm = LLM(
        model="ollama/llama3.2",
        base_url="http://localhost:11434",
        stream=True  
    ) # You can change this to mistral or gemma

# 2. Define Agent
poke_ball_agent = Agent(
    role="Poké Ball Specialist",
    goal="Advise trainers on the most effective Poké Ball to use for any situation",
    backstory=(
        'You are an expert Pokémon researcher who understands every type of Poké Ball,'
        'from the classic Poké Ball to advanced options like the Dusk Ball, Timer Ball, and Master Ball.'
        "You consider the Pokémon species, battle situation, time of day, and trainer's inventory when advising."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 3. Define Task
def get_poke_ball_task(pokemon_name, context=""):
    description = (
        f"A trainer is trying to catch a Pokémon named {pokemon_name}. "
        f"{context} "
        "Recommend the best Poké Ball(s) to use and explain why each is effective."
    )
    expected_output= (f"Recommendaton for best poke balls with explanation why each is effective to use for {context} ")
    return Task(
        description=description,
         expected_output= expected_output,
        agent=poke_ball_agent
    )

# 4. Crew runner
def run_poke_ball_advisor(pokemon_name, context=""):
    task = get_poke_ball_task(pokemon_name, context)
    crew = Crew(
        agents=[poke_ball_agent],
        tasks=[task],
        verbose=True
    )
    return crew.kickoff()

# 5. CLI
if __name__ == "__main__":
    pokemon = input("Enter Pokémon name: ")
    context = input("Enter any situation details (optional): ")
    print("\nAdvising on the best Poké Ball...\n")
    result = run_poke_ball_advisor(pokemon, context)
    print("\nResult:\n")
    print(result)
