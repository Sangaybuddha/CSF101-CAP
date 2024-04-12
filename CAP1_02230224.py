####################
# Sangay Buddha
# 1 ICE
# 02230224
####################
# References
# https://youtu.be/fn68QNcatfo?si=ITs26cdRr3Kho09K
# https://youtu.be/Qcefu1jVPds?si=oBxxjNEnqexIKDQL
# https://youtube.com/shorts/WrYPFpbhmgE?si=bBuFNjd-0XBPmgxm
####################
#
####################
# Solution
# Solution Score:
# 49524
####################
# Read the input_4_cap1.txt file

# Function to read input from the file
def read_input():
    # Open the input file
    with open('input_4_cap1.txt', 'r') as f:
        line = f.readline() 
        rounds = []  # Initialize a list to store round information
        while line:  # Loop until there are no more lines to read

            # Extract opponent's choice and desired outcome from the line and append to the list
            rounds.append((line.split()[0], line.split()[1]))
            line = f.readline()  
        return rounds  # Return the list of rounds


# Function to calculate the total score
def calculate_score(rounds):
    # Define dictionaries to map shape choices to their corresponding scores
    shape_scores = {'A': 1, 'B': 2, 'C': 3}
    # Define a dictionary to map round results to their corresponding scores
    round_scores = {'X': 0, 'Y': 3, 'Z': 6}
    total_score = 0  # Initialize total score to 0
    # Iterate through each round
    for round_info in rounds:
        opponent_choice, result = round_info  
        # Determine player's shape based on opponent's choice and result
        if opponent_choice == 'A' and result == 'X':
            player_shape = 'C'
        elif opponent_choice == 'A' and result == 'Y':
            player_shape = 'A'
        elif opponent_choice == 'A' and result == 'Z':
            player_shape = 'B'
        elif opponent_choice == 'B' and result == 'X':
            player_shape = 'A'
        elif opponent_choice == 'B' and result == 'Y':
            player_shape = 'B'
        elif opponent_choice == 'B' and result == 'Z':
            player_shape = 'C'
        elif opponent_choice == 'C' and result == 'X':
            player_shape = 'B'
        elif opponent_choice == 'C' and result == 'Y':
            player_shape = 'C'
        elif opponent_choice == 'C' and result == 'Z':
            player_shape = 'A'
        else:
            print('Invalid input!')  
        # Add player's shape score and round result score to the total score
        total_score += shape_scores[player_shape] + round_scores[result]
    return total_score  


# Read input from file
round_info_list = read_input()
# Calculate and print the total score
print(f"The total score is: {calculate_score(round_info_list)}")
