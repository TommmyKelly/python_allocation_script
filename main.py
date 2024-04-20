def allocate_clients(clients, team_members):
    allocations = {member[0]: [] for member in team_members}
    client_index = 0

    for client in clients:
        while True:
            current_member = team_members[client_index % len(team_members)]
            if client not in current_member[1]:
                allocations[current_member[0]].append(client)
                client_index += 1
                break
            client_index += 1

    return allocations

def main():
    clients = [
        "Client1", "Client2", "Client3", "Client4", "Client5",
        "Client6", "Client7", "Client8", "Client9", "Client10",
        "Client11", "Client12", "Client13", "Client14", "Client15",
        "Client16", "Client17", "Client18", "Client19", "Client20",
        "Client21", "Client22", "Client23", "Client24", "Client25",
        "Client26", "Client27", "Client28", "Client29", "Client30",
        "Client31", "Client32", "Client33", "Client34"
    ]

    team_members = [
        ("Team Member 1", []),
        ("Team Member 2", ["Client6", "Client12", "Client24"]),
        ("Team Member 3", ["Client3", "Client15", "Client21"]),
        ("Team Member 4", ["Client9", "Client18", "Client30"]),
        ("Team Member 5", [])
    ]

    allocations = allocate_clients(clients, team_members)
    print(allocations)
    for member, assigned_clients in allocations.items():
        print(f"{member} has been assigned the following clients:")
        print(", ".join(assigned_clients))

if __name__ == "__main__":
    main()
