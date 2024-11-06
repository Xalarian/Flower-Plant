#make a selection of plants that a client can take and care for it.
import time
import random
from plyer import notification

#list of plants that can take home
plants = ["cactus", "vriesea","money tree","bamboo"]

#action for the client:
print(plants)

#store the selection of the client's plant:
chosen_plant = input("What plant are you going to take? ")


# Check if the chosen plant is "cactus"
if chosen_plant.lower() == "cactus":  # Convert to lowercase to avoid case sensitivity issues
    print("Great! Let us help you learn about the plant!")

    #INFORMATION ABOUT HOW TO TAKE CARE OF THE PLANT
    print("""1. Lighting
Bright, Direct Light: Cacti love sunlight, so place them near a sunny window where they get plenty of light.
Rotate Occasionally: Turn your cactus every few weeks so all sides receive equal light. This helps avoid uneven growth.
          

2. Watering
Water Sparingly: Cacti are drought-tolerant and should be watered only when the soil is completely dry. Overwatering is the most common way to harm a cactus.
Frequency: In warmer months (spring and summer), water every 2–4 weeks. In winter, water even less—every 4–6 weeks.
Drainage: Make sure the pot has drainage holes, and avoid letting the cactus sit in standing water.""")


elif chosen_plant.lower() == "vriesea":  # Convert to lowercase to avoid case sensitivity issues
    print("Great! Let us help you learn about the plant!")
        #INFORMATION ABOUT HOW TO TAKE CARE OF THE PLANT
    print("""1. Lighting
Bright, Direct Light: Cacti love sunlight, so place them near a sunny window where they get plenty of light.
Rotate Occasionally: Turn your cactus every few weeks so all sides receive equal light. This helps avoid uneven growth.
          

2. Watering
Water Sparingly: Cacti are drought-tolerant and should be watered only when the soil is completely dry. Overwatering is the most common way to harm a cactus.
Frequency: In warmer months (spring and summer), water every 2–4 weeks. In winter, water even less—every 4–6 weeks.
Drainage: Make sure the pot has drainage holes, and avoid letting the cactus sit in standing water.""")

elif chosen_plant.lower() == "money tree":  # Convert to lowercase to avoid case sensitivity issues
    print("Great! Let us help you learn about the plant!")
        #INFORMATION ABOUT HOW TO TAKE CARE OF THE PLANT
    print("""1. Lighting
Bright, Indirect Light: Money trees thrive in bright, indirect sunlight. They can tolerate low light but will grow best with a good balance of light and shade.
Avoid Direct Sunlight: Direct sunlight can burn their leaves. If kept outdoors, place them in partial shade.
          

2. Watering
Moderate Watering: Water when the top 1–2 inches of soil feels dry to the touch, which is usually every 1–2 weeks depending on your environment.
Drain Excess Water: Make sure the pot has drainage holes, as these plants don’t like standing water. Allow water to drain out of the pot to avoid root rot.
Reduce in Winter: Money trees need less water in winter when they are dormant.""")
else:
    print("You selected:", chosen_plant)

verification = input("Are you sure about your future plant?  ")

#Verification about the selection of the plant

if verification == True:
    print("Alright, let's get you the first step!")
elif False:
    print("Alright, let's get you another options!")

print("Every hour will be in need of water! Will let you know!")

def watering_plant():
    while True:
        notification.notify(
            title="Water to the plant!! :D",
            message="It's time for the plant to drink some water!!!",
            timeout=10  # Notification timeout in seconds
        )
        time.sleep(60 * 60)  # Remind every hour (adjust as needed)

if __name__ == "__main__":
    watering_plant()





































