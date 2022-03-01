# granos_contabilizados => 3
granos_contabilizados = 0
peso_por_grano = 0.02
padding_exponente = 2
padding_granos = 20
padding_peso = 25
buffer = ""

for exponente in range(64):
    granos_por_casilla = 2 ** exponente
    peso_por_casilla = peso_por_grano * granos_por_casilla
    
    ui_exponente = str(exponente).ljust(padding_exponente)
    ui_granos_por_casilla = str(granos_por_casilla).center(padding_granos)
    ui_peso_por_casilla = str(peso_por_casilla).center(padding_peso)

    buffer += f"│ {ui_exponente} "
    buffer += f"│ {ui_granos_por_casilla}"
    buffer += f"│ {ui_peso_por_casilla} │"
    
    buffer += "\n"

    granos_contabilizados = granos_contabilizados + granos_por_casilla

pre = """┌────┬─────────────────────┬───────────────────────────┐
│  # │       granos        │        gramos             │
├────┼─────────────────────┼───────────────────────────┤
"""

post = "└────┴─────────────────────┴───────────────────────────┘"

buffer = pre + post

print(buffer)

peso_total = peso_por_grano * granos_contabilizados
print(f"  · Granos totales: {granos_contabilizados}")
print(f"  · Peso total = {peso_total} gramos")
print(f"  · Peso total = {peso_total/1000} kilos")
print(f"  · Peso total = {peso_total/1000000} toneladas")
