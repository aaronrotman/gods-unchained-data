##################################################
# Dependencies
##################################################
print("Importing dependencies...")
import pandas as pd
print("Dependencies imported successfully")

# Input and store the desired tournament week number
week_num = f"{input('Enter the tournament week number: ')}"

# Assign the file path to a variable
csv_path = f"data/raw_data/week_{week_num}.csv"

# Read in data from the csv file
data = pd.read_csv(csv_path)

##################################################
# TOP TEN MYTHIC PLAYERS
##################################################

print("Cleaning data...")

# Drop un-needed columns
data.drop(columns = ["Unnamed: 0", "Unnamed: 13", "Unnamed: 14"], inplace=True)

# Fix capitalization in 'Wins in first 25' column name
data.rename(columns={"Wins in first 25": "Wins in First 25"}, inplace=True)

# Add column for week_number
data["Week Number"] = week_num

# Create dataframe of the top ten mythic players
top_ten = data[0:10].copy()

# Convert Place column to integer
data["Place"] = top_ten["Place"].astype(int).copy()

# Reorder columns to match database schema
top_ten = top_ten[[
    "Week Number", 
    "Place", 
    "Username", 
    "Peak Rating", 
    "Wins", 
    "Wins in First 25", 
    "Counted Wins", 
    "Core Rare", 
    "Core Epic", 
    "Core Legendary", 
    "Trial Rare", 
    "Trial Epic", 
    "Trial Legendary",]].copy()

##################################################
# MAIN EVENT
##################################################

# Dataframe of main event data
main_event = data[11:].copy()

# Drop the "Place" column
main_event = main_event.drop(columns=["Place"])

# Remove the first row containing column names
main_event = main_event[1:].copy()

# Rename the "Peak Rating" column to "Rank"
main_event.rename(columns={"Peak Rating": "Rank"}, inplace=True)

# Reset the index
main_event = main_event.reset_index(drop=True)

# Reorder columns to match database schema
main_event = main_event[[
    "Week Number", 
    "Username", 
    "Rank", 
    "Wins", 
    "Wins in First 25", 
    "Counted Wins", 
    "Core Rare", 
    "Core Epic", 
    "Core Legendary", 
    "Trial Rare", 
    "Trial Epic", 
    "Trial Legendary"]].copy()

# Cast the username column as a string
main_event["Username"] = main_event["Username"].astype(str).copy()

print("Data cleaning complete.")

##################################################
# Export data
##################################################

print("Creating export file paths...")

# Assign the top mythic player output paths to variables
# Path to save dataframe as CSV
cleaned_mythic_path = f"data/cleaned_data/top_mythic_{week_num}.csv"
# Path to append datafame to the combined data CSV
combined_mythic_path = "data/combined_data/top_mythic.csv"

# Assign the main event output paths to variables
# Path to save dataframe as CSV
cleaned_main_path = f"data/cleaned_data/main_event_{week_num}.csv"
# Path to append datafame to the combined data CSV
combined_main_path = "data/combined_data/main_event.csv"

print("File paths created.")

print("Writing dataframes to CSV...")

# Save the top mythic player dataframe as CSV 
# Export the dataframe to the cleaned data folder
top_ten.to_csv(cleaned_mythic_path, index=False)

###################################################################################################
# @ DEV 
# Uncomment the code below ONLY THE FIRST TIME the script is run to create the combined data file.

# Save the top mythic player dataframe to a new combined data file
# top_ten.to_csv(combined_mythic_path, index=False)
###################################################################################################


# Append the dataframe to the combined data file
top_ten.to_csv(combined_mythic_path, mode="a", index=False, header=False)

# Save the main event dataframe as CSV 
# Save the dataframe to the cleaned data folder
main_event.to_csv(cleaned_main_path, index=False)


###################################################################################################
# @ DEV 
# Uncomment the code below ONLY THE FIRST TIME the script is run to create the combined data file.

# Save the main event dataframe to a new combined data file
# main_event.to_csv(combined_main_path, index=False)
###################################################################################################

# Append the dataframe to the combined data file
main_event.to_csv(combined_main_path, mode="a", index=False, header=False)

print("Data cleaning complete.")
