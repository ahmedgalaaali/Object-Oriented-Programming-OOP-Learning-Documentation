import pandas as pd
import os
import matplotlib.pyplot as plt

class Pokedex:
    def __init__(self, path):
        self.path = path
        self.files_list = []
        for file in os.listdir(path):
            if file.endswith(".csv"):
                df = pd.read_csv(path + "\\" + file)
                self.files_list.append(df)
                self.data = pd.concat(self.files_list, ignore_index=True)

patch_path = "D:\Mine\OOP Python\Pokemon\Patches"
class GameEngine:
    def __init__(self, pokemon):
        self.pokemon = pokemon.data

    # Get the strongest pokemon per type.
    def strongest_per_type(self, type):
        self.type = type
        pokemon_type = self.pokemon[self.pokemon["Type 1"] == self.type]
        pokemon_data = pokemon_type.loc[pokemon_type["Attack"].idxmax()]
        strongest = pokemon_data["Name"]
        attack_power = pokemon_data["Attack"]
        print(f"The strongest {self.type} pokemon is: {strongest} with an attack power: {attack_power}")
    
    # Compare between pokemon types' features.
    def compare_types(self, type_1, type_2, feature):
        self.type_1 = self.pokemon[self.pokemon["Type 1"] == type_1]
        self.type_2 = self.pokemon[self.pokemon["Type 1"] == type_2]
        average_feature_1 = self.type_1[feature].mean()
        average_feature_2 = self.type_2[feature].mean()
        if average_feature_1 > average_feature_2:
            print(f"{type_1} has higher average {feature} than {type_2} ({round(average_feature_1, 0)} vs. {round(average_feature_2, 0)})")
        else: 
            print(f"{type_2} has higher average {feature} than {type_1} ({round(average_feature_2, 0)} vs. {round(average_feature_1, 0)})")
    
    # Check the difference between average legendary and common pokemon speed.
    def legendary_speed_check(self):
        legendary = self.pokemon[self.pokemon["Legendary"] == True]
        non_legendary = self.pokemon[~(self.pokemon["Legendary"] == True)]
        print(f"""
The list contains {len(legendary)} legendary pokemon and {len(non_legendary)} non-legendary pokemon.
Average legendary pokemons speed: {round(legendary["Speed"].mean(), 0)}
Average non-legendary pokemons speed: {round(non_legendary["Speed"].mean(), 0)}
""")
    
    # Nerf any pokemon's feature
    def nerf(self, feature, nerf_value, all_creatures=False, is_legend=False):
        multiplier = 1-nerf_value
        if all_creatures == True:
            self.pokemon[feature] *= multiplier
        elif is_legend ==True:
            self.pokemon.loc[self.pokemon["Legendary"] == True, feature] *= multiplier
        else:
            self.pokemon.loc[self.pokemon["Legendary"] == False, feature] *= multiplier
        print(f"Feature {feature} has been nerfed to {multiplier * 100}%")
    
    # Categorize speed of each pokemon: "Hyper", "Slugish" and "Standard".
    def speed_tire(self):
        self.pokemon["speed_tier"] = ["Hyper" if s > 100 else "Slugish" if s < 50 else "Standard" for s in self.pokemon["Speed"]]
        print("Speed tiering has been applied!")

    # Apply and save all the needed updates!
    def apply_updates(self, version):
        new_patch = patch_path + "\\" + f"balanced_roster_v{version}.csv"
        self.pokemon.to_csv(new_patch, index=False)
        print(f"""
Updates have been applied successfuly!
version: v_{version}
Update path:
{new_patch}
""")

class Dashboard:
    def __init__(self, dataset):
        self.dataset = dataset.data
    def generate_report(self):
        legendary = self.dataset[self.dataset["Legendary"] == True]
        non_legendary = self.dataset[~(self.dataset["Legendary"] == True)]
        avg_leg_atk = legendary["Attack"].mean()
        avg_non_leg_atk = non_legendary["Attack"].mean()
        atk_compare = pd.DataFrame({
            "keys": ["avg_leg_atk", "avg_non_leg_atk"],
            "values": [avg_leg_atk, avg_non_leg_atk]
        })
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        ax1.bar(atk_compare["keys"], atk_compare["values"])
        ax2.hist(self.dataset["Speed"])
        plt.tight_layout()
        plt.show()

x = GameEngine(Pokedex("D:\Mine\OOP Python\Pokemon\Files"))
x.nerf("Speed", 0.1, is_legend=True)
x.speed_tire()
x.apply_updates(1)

y = Dashboard(Pokedex("D:\Mine\OOP Python\Pokemon\Patches"))
y.generate_report()