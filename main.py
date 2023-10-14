from mascotas_del_dojo import Ninja, Mascota

Luna = Mascota("Luna", "Perro", "pizza")
lisa = Ninja("Lisa", "Park", Luna, "pollo", "bacon" )

print(f"{lisa.nombre} pasea a su mascota:")
lisa.caminar()

print(f"{lisa.nombre} alimenta a su mascota con {lisa.comida_mascota}:")
lisa.alimentar()

print(f"{lisa.nombre} baña a su mascota:")
lisa.bañar()