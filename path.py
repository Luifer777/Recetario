from pathlib import Path


guia = Path ("Europa", "España", "Barcelona", "Sagrada_familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)
