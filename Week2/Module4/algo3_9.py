lifetime_parent1 = float(input("lp1 ="))
lifetime_parent2 = float(input("lp2 ="))
lifetime_grandfather1 = float(input("gf1 ="))
lifetime_grandfather2 = float(input("gf2 ="))
lifetime_grandmother1 = float(input("gm1 ="))
lifetime_grandmother2 = float(input("gm2 ="))

lifetime = (lifetime_parent1 + lifetime_parent2 + lifetime_grandfather1 + lifetime_grandfather2 +
lifetime_grandmother1 + lifetime_grandmother2) / 6

print(lifetime)