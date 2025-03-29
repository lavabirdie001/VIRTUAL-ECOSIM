import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from transformers import pipeline
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Initialize the AI chatbot model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium", framework="pt")

st.markdown("""
    <style>
    /* General Styles */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f7f6;
    }

    /* Footer Styling */
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background: linear-gradient(to right, #2E8B57, #4682B4);
        color: white;
        text-align: center;
        padding: 12px 0;
        font-size: 16px;
        font-weight: bold;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.2);
    }

    /* Highlight Box for Important Information */
    .highlight-box {
        background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
        padding: 15px;
        border-left: 5px solid #4682B4;
        border-radius: 8px;
        font-size: 16px;
        color: #333;
        margin-bottom: 20px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
    }

    /* Sidebar Enhancements */
    .sidebar .block-container {
        background: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }

    /* Button Styling */
    .stButton > button {
        background: linear-gradient(to right, #2E8B57, #4682B4);
        color: white;
        font-size: 16px;
        padding: 10px 15px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background: linear-gradient(to right, #4682B4, #2E8B57);
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)


# Page title and introduction
st.title("🌍 Advanced Ecosystem Analyzer ")

# Introduction Section
st.markdown("""
    🌿 **Welcome to the Ecosystem Simulation Portal!**  
    Gain deep insights into biodiversity, species interactions, and ecosystem dynamics through **interactive simulations and AI-powered analytics.**  
    🦁 Predict changes in wildlife populations, explore conservation strategies, and uncover the impact of climate on ecosystems! 🌎  
""")

# Call-to-Action
st.success("🔍 **Start exploring by adjusting parameters in the sidebar!**")


# AI Chatbot Interface
st.sidebar.title("🤖 AI Ecosystem Chatbot")

# User Input Area
st.sidebar.markdown("💬 **Ask me anything about the ecosystem, biodiversity, or species!**")
user_query = st.sidebar.text_area("🔍 Type your question below:", placeholder="e.g., How does deforestation affect biodiversity?")

# Chatbot Response Area
if st.sidebar.button("💡 Get Expert Insights"):
    with st.spinner("Thinking... 🤔"):
        try:
            # Generate AI Response
            response = chatbot(user_query, max_length=150, num_return_sequences=1)
            chatbot_response = response[0]['generated_text']

            # Display Response
            st.sidebar.markdown("### 🌍 AI Ecosystem Insight:")
            st.sidebar.success(chatbot_response)

            # Additional Suggestions
            st.sidebar.info("💡 **Tip:** You can also ask about specific species, ecosystems, or conservation methods!")
        
        except Exception as e:
            st.sidebar.error(f"❌ Error: {str(e)}")

# Additional Features for a Better Experience
st.sidebar.markdown("---")  # Separator for UI clarity
st.sidebar.markdown("🔹 **Try asking:**")
st.sidebar.markdown("- What are the main threats to coral reefs? 🪸")
st.sidebar.markdown("- How do predators maintain ecological balance? 🦁")
st.sidebar.markdown("- What are the best conservation practices for tigers? 🐅")
st.sidebar.markdown("- How does climate change impact marine ecosystems? 🌊")


# Sidebar Parameters for Simulation
st.sidebar.title("🔧 Simulation Settings")

# 🌱 Ecosystem Parameters
st.sidebar.subheader("🌍 Ecosystem Settings")
plant_growth_rate = st.sidebar.slider("🌱 Plant Growth Rate", 0.01, 0.5, 0.2, help="Controls how quickly plants regenerate.")
herbivore_birth_rate = st.sidebar.slider("🐇 Herbivore Birth Rate", 0.01, 0.3, 0.1, help="Rate at which herbivores reproduce.")
predator_birth_rate = st.sidebar.slider("🦁 Predator Birth Rate", 0.01, 0.2, 0.05, help="Rate at which predators reproduce.")

# 📊 Initial Population Settings
st.sidebar.subheader("👥 Initial Population")
initial_plants = st.sidebar.slider("🌼 Initial Plant Population", 50, 500, 100, help="Starting number of plants in the ecosystem.")
initial_herbivores = st.sidebar.slider("🐐 Initial Herbivore Population", 10, 100, 30, help="Starting number of herbivores.")
initial_predators = st.sidebar.slider("🦅 Initial Predator Population", 5, 50, 10, help="Starting number of predators.")

# ⏳ Simulation Control
st.sidebar.subheader("⏳ Simulation Control")
time_steps = st.sidebar.slider("⏱ Simulation Duration (Steps)", 10, 200, 50, help="Number of time steps the simulation will run.")

# 🌿 Abiotic Environmental Factors
st.sidebar.subheader("🌿 Abiotic Factors")
water_availability = st.sidebar.slider("💧 Water Availability", 0.0, 1.0, 0.5, help="Amount of water available in the ecosystem.")
temperature_variation = st.sidebar.slider("🌡 Temperature Variation (°C)", -10, 40, 25, help="Range of temperature fluctuations.")
soil_quality = st.sidebar.slider("🌾 Soil Quality Index", 0.1, 1.0, 0.7, help="Quality of soil affecting plant growth.")

# 🚧 Human Impact & External Factors
st.sidebar.subheader("🚧 Human & External Impact")
human_impact = st.sidebar.slider("🏗 Human Impact Factor", 0.0, 1.0, 0.2, help="Influence of human activities on the ecosystem.")
pollution_level = st.sidebar.slider("☣ Pollution Level", 0.0, 1.0, 0.3, help="Amount of pollution affecting the environment.")
natural_disasters = st.sidebar.slider("🌪 Frequency of Natural Disasters", 0, 10, 2, help="Number of natural disasters occurring in the simulation.")

# 🔄 Additional Dynamic Factors
st.sidebar.subheader("🔄 Dynamic Changes")
seasonal_variation = st.sidebar.slider("🍂 Seasonal Variation Impact", 0.0, 1.0, 0.5, help="Effect of seasonal changes on population dynamics.")
disease_outbreak = st.sidebar.slider("🦠 Disease Outbreak Probability", 0.0, 1.0, 0.2, help="Chance of a disease affecting the population.")

st.sidebar.markdown("---")  # Adds a separator for cleaner UI
st.sidebar.info("🔍 Adjust these parameters to explore different ecosystem scenarios and analyze how various factors impact species populations.")



# Function to run the simulation
def run_simulation(initial_plants, initial_herbivores, initial_predators, time_steps):
    plants, herbivores, predators = initial_plants, initial_herbivores, initial_predators
    plant_pop, herbivore_pop, predator_pop = [], [], []

    for t in range(time_steps):
        plants = max(plants + plants * plant_growth_rate * (1 + water_availability - 0.1 * human_impact) - herbivores * 0.01, 0)
        herbivores = max(herbivores + herbivores * herbivore_birth_rate * (1 + soil_quality - 0.05 * temperature_variation) - predators * 0.01, 0)
        predators = max(predators + predators * predator_birth_rate * (herbivores / (herbivores + 1)), 0)
        plant_pop.append(plants)
        herbivore_pop.append(herbivores)
        predator_pop.append(predators)
    
    return plant_pop, herbivore_pop, predator_pop

# Initialize empty lists for population data
plant_pop, herbivore_pop, predator_pop = [], [], []

# Run the simulation and visualize the results
if st.sidebar.button("Run Simulation"):
    plant_pop, herbivore_pop, predator_pop = run_simulation(initial_plants, initial_herbivores, initial_predators, time_steps)
    
    # Create a more detailed visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # Creating a grid of plots
    
    # Main population dynamics over time
    axes[0, 0].plot(range(time_steps), plant_pop, label='Plants', color='green', linewidth=2)
    axes[0, 0].plot(range(time_steps), herbivore_pop, label='Herbivores', color='blue', linewidth=2)
    axes[0, 0].plot(range(time_steps), predator_pop, label='Predators', color='red', linewidth=2)
    axes[0, 0].set_xlabel("Time Steps")
    axes[0, 0].set_ylabel("Population")
    axes[0, 0].set_title("📈 Population Trends Over Time")
    axes[0, 0].legend()
    axes[0, 0].grid(True)

    # Stack plot for proportion visualization
    axes[0, 1].stackplot(range(time_steps), plant_pop, herbivore_pop, predator_pop, 
                         labels=['Plants', 'Herbivores', 'Predators'], colors=['green', 'blue', 'red'], alpha=0.6)
    axes[0, 1].set_xlabel("Time Steps")
    axes[0, 1].set_ylabel("Population")
    axes[0, 1].set_title("📊 Proportional Representation of Species Over Time")
    axes[0, 1].legend(loc="upper left")
    
    # Distribution of population fluctuations
    sns.histplot(plant_pop, ax=axes[1, 0], kde=True, color='green', bins=20, label="Plants")
    sns.histplot(herbivore_pop, ax=axes[1, 0], kde=True, color='blue', bins=20, label="Herbivores")
    sns.histplot(predator_pop, ax=axes[1, 0], kde=True, color='red', bins=20, label="Predators")
    axes[1, 0].set_title("📊 Population Distribution (Fluctuations Over Time)")
    axes[1, 0].set_xlabel("Population Count")
    axes[1, 0].set_ylabel("Frequency")
    axes[1, 0].legend()
    
    # Correlation heatmap
    data = pd.DataFrame({"Plants": plant_pop, "Herbivores": herbivore_pop, "Predators": predator_pop})
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=axes[1, 1])
    axes[1, 1].set_title("🔗 Correlation Between Species Populations")
    
    # Adjust layout for better visibility
    plt.tight_layout()
    st.pyplot(fig)

    # Summary Statistics & Observations
    st.write("## 🌍 Simulation Observations & Insights")
    st.write("This visualization presents key ecosystem interactions over time:")
    st.markdown("""
    - **Population Growth Trends**: See how plants, herbivores, and predators interact dynamically.
    - **Proportional Representation**: The stack plot shows the relative population share over time.
    - **Population Distribution**: Understand fluctuations in population through histograms.
    - **Correlation Insights**: The heatmap reveals relationships between species (e.g., predators increase when herbivores increase).
    """)



# Generate summary insights if the simulation was run
if plant_pop:
    st.write("## 🌍 Ecosystem Insights & Key Observations")
    st.markdown("""
    The simulation has provided valuable insights into how different species interact and how environmental factors impact their survival. Here’s what we observed:
    """)

    # Understanding plant growth
    if np.mean(plant_pop) > initial_plants:
        st.write("🌱 **Plant Population Thrived!**")
        st.write("The ecosystem provided favorable conditions for plant growth, leading to a steady or increasing plant population. Factors such as high water availability, fertile soil, and minimal human impact played a key role.")
    else:
        st.write("🌱 **Plant Population Declined!**")
        st.write("The plant population faced challenges such as overgrazing, harsh climate conditions, or human interference, leading to a decline over time.")

    # Understanding herbivore population
    if np.mean(herbivore_pop) > initial_herbivores:
        st.write("🐇 **Herbivores Thrived!**")
        st.write("An abundance of plant life ensured herbivores had plenty of food. The stable environment led to population growth, supporting a healthy ecosystem.")
    else:
        st.write("🐇 **Herbivore Population Declined!**")
        st.write("Scarcity of food, increased predation, or unsuitable environmental conditions led to a reduction in herbivore numbers, affecting the balance of the ecosystem.")

    # Understanding predator population
    if np.mean(predator_pop) > initial_predators:
        st.write("🦁 **Predators Maintained a Healthy Population!**")
        st.write("The presence of sufficient prey allowed predators to sustain or grow their population without major disruptions.")
    else:
        st.write("🦁 **Predators Faced Challenges!**")
        st.write("A decline in prey numbers, harsh conditions, or human activities may have impacted the predator population, leading to difficulties in survival.")

    # Overall ecosystem balance
    if (np.mean(plant_pop) > initial_plants and 
        np.mean(herbivore_pop) > initial_herbivores and 
        np.mean(predator_pop) > initial_predators):
        st.success("🌎 **Ecosystem in Balance!**")
        st.write("The ecosystem maintained stability, with all species coexisting in a sustainable manner. This indicates a healthy balance between food availability, reproduction, and natural cycles.")
    else:
        st.error("⚠️ **Ecosystem Instability Detected!**")
        st.write("Certain populations struggled to sustain themselves, possibly due to over-predation, food shortages, climate shifts, or human impact. Addressing these factors could improve biodiversity resilience.")

    # Display duration of the simulation
    st.write(f"🕒 **Total Simulation Duration**: {time_steps} time steps")

else:
    st.warning("⚠️ Run the simulation first to view key highlights.")


# Conservation Tips Section
st.sidebar.header("💡 Conservation Tips & Care Guide")

# List of species (can be expanded)
species_list = [
    "Tiger", "Elephant", "Panda", "Coral Reefs", "Blue Whale", "Mangroves", 
    "Amazon Rainforest", "Snow Leopard", "Sea Turtles", "Monarch Butterfly"
]

# User input (selection or manual entry)
selected_species = st.sidebar.selectbox("Select a species:", species_list)
custom_species = st.sidebar.text_input("Or enter a species name:")

# Function to generate conservation tips
def get_conservation_tips(species):
    conservation_guides = {
        "Tiger": """
        **Conservation Strategies for Tigers:**
        - Protect natural habitats from deforestation and illegal logging.
        - Strengthen anti-poaching laws and wildlife crime monitoring.
        - Support breeding programs in conservation reserves.
        - Reduce human-wildlife conflict by promoting safe buffer zones.
        - Raise awareness about illegal wildlife trade and tiger farming.
        """,
        
        "Elephant": """
        **Conservation Strategies for Elephants:**
        - Preserve migratory corridors to ensure safe movement.
        - Prevent poaching by enforcing strict anti-ivory trade laws.
        - Reduce habitat destruction by promoting sustainable agriculture.
        - Support eco-tourism that funds conservation efforts.
        - Raise awareness on human-elephant conflict resolution.
        """,

        "Panda": """
        **Conservation Strategies for Pandas:**
        - Expand and protect bamboo forests, their primary food source.
        - Prevent habitat fragmentation by creating wildlife corridors.
        - Strengthen captive breeding and reintroduction programs.
        - Promote sustainable farming near panda habitats.
        - Educate communities about the ecological importance of pandas.
        """,

        "Coral Reefs": """
        **Conservation Strategies for Coral Reefs:**
        - Reduce ocean pollution, especially plastic and chemical runoff.
        - Implement sustainable fishing practices to prevent overfishing.
        - Combat climate change by reducing carbon footprints.
        - Promote coral reef restoration projects like coral farming.
        - Encourage marine protected areas (MPAs) and responsible tourism.
        """,

        "Blue Whale": """
        **Conservation Strategies for Blue Whales:**
        - Reduce ship strikes by implementing safe marine traffic routes.
        - Minimize ocean noise pollution to avoid disrupting whale communication.
        - Combat illegal whaling through international agreements.
        - Monitor populations through satellite tracking and conservation programs.
        - Protect krill populations by managing sustainable fisheries.
        """,

        "Mangroves": """
        **Conservation Strategies for Mangroves:**
        - Prevent coastal deforestation and illegal land reclamation.
        - Promote mangrove afforestation and restoration projects.
        - Reduce pollution from agricultural and industrial waste.
        - Educate communities about the role of mangroves in flood control.
        - Establish protected mangrove reserves with strict regulations.
        """,

        "Amazon Rainforest": """
        **Conservation Strategies for the Amazon Rainforest:**
        - Combat illegal logging and land encroachment.
        - Support indigenous communities and their conservation efforts.
        - Promote sustainable agriculture to reduce deforestation.
        - Reduce greenhouse gas emissions to combat climate change.
        - Strengthen law enforcement against wildlife trafficking.
        """,

        "Snow Leopard": """
        **Conservation Strategies for Snow Leopards:**
        - Protect mountain ecosystems and prevent habitat fragmentation.
        - Work with local herders to reduce human-wildlife conflict.
        - Strengthen anti-poaching and illegal fur trade enforcement.
        - Support snow leopard monitoring programs using GPS tracking.
        - Raise awareness through global conservation campaigns.
        """,

        "Sea Turtles": """
        **Conservation Strategies for Sea Turtles:**
        - Reduce plastic pollution to prevent ingestion and entanglement.
        - Protect nesting beaches from human encroachment.
        - Implement fishing gear modifications to prevent accidental capture.
        - Enforce laws against turtle egg poaching and illegal trade.
        - Educate coastal communities about turtle conservation.
        """,

        "Monarch Butterfly": """
        **Conservation Strategies for Monarch Butterflies:**
        - Plant milkweed, their primary food source, in gardens and wild areas.
        - Reduce pesticide and herbicide use to prevent poisoning.
        - Protect migratory routes by preserving wildflower habitats.
        - Raise awareness about butterfly conservation through education.
        - Support research on population declines and climate adaptation.
        """
    }
    
    return conservation_guides.get(species, "No conservation data available for this species. Try selecting another one.")

# Determine the species input and display tips
if custom_species:
    st.sidebar.warning("Custom species feature is in development. Selecting from the list is recommended.")
    species = custom_species.title()
else:
    species = selected_species

conservation_info = get_conservation_tips(species)
st.sidebar.markdown(f"### 🛡 Conservation Guide for **{species}**")
st.sidebar.markdown(conservation_info)


# Educational Resources
st.write("### 📚 Educational Resources")
st.write("Expand your knowledge about biodiversity, conservation, and ecological balance through these trusted resources:")

st.markdown("""
#### 🌿 **Global Biodiversity & Conservation**
- **[IUCN Red List](https://www.iucnredlist.org/)** – A comprehensive source that tracks the conservation status of species worldwide, including endangered and extinct species.
- **[World Wildlife Fund (WWF)](https://www.worldwildlife.org/)** – Provides insights into global conservation efforts, endangered species protection, and climate action.
- **[Convention on Biological Diversity (CBD)](https://www.cbd.int/)** – The official platform for international biodiversity agreements and action plans.

#### 🌏 **Climate Change & Environmental Science**
- **[NASA Climate Change](https://climate.nasa.gov/)** – Real-time data on global climate change, temperature variations, and CO₂ levels.
- **[United Nations Environment Programme (UNEP)](https://www.unep.org/)** – Reports on climate policies, biodiversity loss, and sustainable development goals (SDGs).
- **[IPCC (Intergovernmental Panel on Climate Change)](https://www.ipcc.ch/)** – Scientific assessments on climate change, its impacts, and potential adaptation strategies.

#### 📖 **Educational Platforms & Learning**
- **[National Geographic](https://www.nationalgeographic.com/)** – Engaging articles, documentaries, and interactive maps on biodiversity, wildlife, and ecosystems.
- **[Khan Academy - Ecology](https://www.khanacademy.org/science/biology/ecology)** – Free courses on ecosystems, food webs, and environmental science.
- **[Smithsonian National Museum of Natural History](https://naturalhistory.si.edu/education)** – A collection of interactive exhibits and educational materials on biodiversity and evolution.

#### 🏞 **Citizen Science & Wildlife Monitoring**
- **[eBird](https://ebird.org/)** – A platform where birdwatchers contribute data on bird populations and migration patterns.
- **[iNaturalist](https://www.inaturalist.org/)** – Allows users to document and share observations of plant and animal species with a global community.
- **[Global Biodiversity Information Facility (GBIF)](https://www.gbif.org/)** – Provides open access to biodiversity data, including species distribution maps and occurrence records.

🔍 *Explore these resources to stay informed, participate in conservation efforts, and contribute to scientific research!* 🌱🌎
""")


# Interactive Quiz Section
st.write("### ❓ Interactive Quiz")

quiz_questions = {
    "What is the biggest threat to biodiversity?": {
        "options": ["Habitat Loss", "Climate Change", "Pollution", "Overexploitation"],
        "answer": "Habitat Loss"
    },
    "Which gas is primarily responsible for global warming?": {
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"],
        "answer": "Carbon Dioxide"
    },
    "What percentage of the Earth's surface is covered by forests?": {
        "options": ["10%", "31%", "50%", "75%"],
        "answer": "31%"
    },
    "Which organization maintains the Red List of Threatened Species?": {
        "options": ["UNESCO", "WWF", "IUCN", "Greenpeace"],
        "answer": "IUCN"
    },
    "Which biome is home to the most biodiversity?": {
        "options": ["Desert", "Tundra", "Tropical Rainforest", "Savanna"],
        "answer": "Tropical Rainforest"
    }
}

# Display quiz questions
selected_question = st.selectbox("Choose a question to answer:", list(quiz_questions.keys()))
options = quiz_questions[selected_question]["options"]
correct_answer = quiz_questions[selected_question]["answer"]

user_answer = st.radio("Select your answer:", options)

if st.button("Submit Answer"):
    if user_answer == correct_answer:
        st.success("Correct! 🎉")
    else:
        st.error(f"Incorrect! The correct answer is: {correct_answer}")


# User Feedback Section
st.subheader("💬 User Feedback")
feedback = st.text_area("Please provide your feedback on the simulation and chatbot responses:")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")

# Footer
st.markdown("""
---

Made with Love ❤️ by **Prateek** and **Aditya**
""")
