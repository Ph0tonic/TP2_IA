# TP2_IA
IA TP n°2 - A*

# Questions - Heuristiques
Supposons que l’on veuille se rendre à la ville B. Pour tout noeud n, on va s’int´eresser aux heuristiques
suivantes
- h0(n) = 0
- h1(n) = “la distance entre n et B sur l’axe des x”
- h2(n) = “la distance entre n et B sur l’axe des y”
- h3(n) = “la distance à vol d’oiseau entre n et B”
- h4(n) = “la distance de Manhattan entre n et B”

Parmi ces heuristiques, lesquelles sont admissibles ?
Toutes les heuristiques sont admissibles à l'exception de h4(n), c'est à dire la distance de Manhattan.

## Exemple du problème avec h4
Un exemple concret de ce problème peut être constaté sur le trajet Paris-Prague.
Résultats pour trajet Paris-Prague:
- h0 -> Paris/Brussels/Amsterdam/Munich/Prague | Total Length : *1089*
- h1 -> Paris/Brussels/Amsterdam/Munich/Prague | Total Length : *1089*
- h2 -> Paris/Brussels/Amsterdam/Munich/Prague | Total Length : *1089*
- h3 -> Paris/Brussels/Amsterdam/Munich/Prague | Total Length : *1089*
- h4 -> Paris/Brussels/Amsterdam/Hamburg/Berlin/Prague | Total Length : *1128*
