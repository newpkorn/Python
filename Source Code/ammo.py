import tank

first_tank = tank.Tank('Gun', 9)
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.fire_ammo()
first_tank.fire_ammo()
print(first_tank.ammo)

first_tank.add_ammo(3)
print(first_tank.ammo)