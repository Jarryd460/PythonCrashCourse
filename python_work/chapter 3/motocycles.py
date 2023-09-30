motocyles = ["honda", "yamaha", "suzuki"]
print(motocyles)

motocyles[0] = "ducati"
print(motocyles)

motocyles.append("honda")
print(motocyles)

motocyles.insert(0, "ktm")
print(motocyles)

del motocyles[-1]
print(motocyles)

popped_motocyle = motocyles.pop()
print(popped_motocyle)

first_motocycle = motocyles.pop(0)
print(first_motocycle)

# Removes all items after and including "yamaha"
motocyles.remove("yamaha")
print(motocyles)