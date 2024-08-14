from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon", "Type", "Caught"]
table.add_rows([
        ["Pikatchu", "Electric", 0],
        ["Squirtle", "Water", 0],
        ["Charmander", "Fire", 0],
    ])
print(table)
