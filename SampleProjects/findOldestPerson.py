data = {
    "Saleh": 37,
    "Elham": 35,
    "Ghazal": 3
}

max_age = max(data, key=data.get)
min_age = min(data, key=data.get)

print(f"The oldest person is '{max_age}' with {data[max_age]} years old")
print(f"The youngest person is '{min_age}' with {data[min_age]} years old")