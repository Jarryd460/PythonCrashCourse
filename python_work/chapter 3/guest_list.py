peopleToInvite = ["Albert Einstein", "Sir Isaac Newton", "Tupac"]
print(f"Hi {peopleToInvite[0]}, I would formally like to invite you to my dinner this evening.")
print(f"Hi {peopleToInvite[1]}, I would formally like to invite you to my dinner this evening.")
print(f"Hi {peopleToInvite[2]}, I would formally like to invite you to my dinner this evening.")

print("")
personWhoCantAttend = peopleToInvite.pop(1)
print(f"{personWhoCantAttend} will not be able to attend this evenings dinner.")

print("")
peopleToInvite.insert(1, "Sir Alex Ferguson")
print(f"Hi {peopleToInvite[0]}, I would formally like to invite you to my dinner this evening.")
print(f"Hi {peopleToInvite[1]}, I would formally like to invite you to my dinner this evening.")
print(f"Hi {peopleToInvite[2]}, I would formally like to invite you to my dinner this evening.")

print("")
print("We have found a bigger table so you can expect more guests")

peopleToInvite.insert(0, "Miss Niel")
peopleToInvite.insert(2, "Nelson Mandela")
peopleToInvite.append("Kevin Heart")

print("")
print(f"Hi {peopleToInvite[0]}, I would formally like to invite you to my dinner this evening.")
print(f"Hi {peopleToInvite[1]}, I would formally like to invite you to my dinner this evening.")
print(f"Hi {peopleToInvite[2]}, I would formally like to invite you to my dinner this evening.")
print(f"Hi {peopleToInvite[3]}, I would formally like to invite you to my dinner this evening.")
print(f"Hi {peopleToInvite[4]}, I would formally like to invite you to my dinner this evening.")
print(f"Hi {peopleToInvite[5]}, I would formally like to invite you to my dinner this evening.")

print("")
print("Unfortunately, we can only invite two guests")

unviteGuest = peopleToInvite.pop()
print("")
print(f"Hi {unviteGuest}, we are sorry but due to events out of our control, you have been unvited.")

unviteGuest = peopleToInvite.pop()
print(f"Hi {unviteGuest}, we are sorry but due to events out of our control, you have been unvited.")

unviteGuest = peopleToInvite.pop()
print(f"Hi {unviteGuest}, we are sorry but due to events out of our control, you have been unvited.")

unviteGuest = peopleToInvite.pop()
print(f"Hi {unviteGuest}, we are sorry but due to events out of our control, you have been unvited.")

print("")
print("Number of people invited: " + str(len(peopleToInvite)))
print(f"Hi {peopleToInvite[0]}, you are still invited.")
print(f"Hi {peopleToInvite[1]}, you are still invited.")

del peopleToInvite[1]
del peopleToInvite[0]

print("")
print(peopleToInvite)