import outfits_cost
outfits = outfits_cost.outfits

for key, value in outfits.items():
    print(f"{key}, {value}")
print(sum(outfits.values()))
print(len(outfits))