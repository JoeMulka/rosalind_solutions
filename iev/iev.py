
dominant_fraction = {"AA-AA":1,"AA-Aa":1,"AA-aa":1,"Aa-Aa":0.75,"Aa-aa":0.5,"aa-aa":0}
num_offspring = 2
#couple_counts = [1,0,0,1,0,1]
couple_counts = [19570,16348,16382,18823,17756,19999]

expected_num_dominant = 0
for i,couple_type in enumerate(dominant_fraction):
    expected_num_dominant += (dominant_fraction[couple_type] * num_offspring) * couple_counts[i]

print(f"Expected offspring with dominant phenotype: {expected_num_dominant}")