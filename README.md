# TP2_IA
- IA TP n°2 - A*
- Autheur : Bastien Wermeille
- Date : 11.11.2018

# Questions - Heuristiques
Supposons que l’on veuille se rendre à la ville B. Pour tout noeud n, on va s’intéresser aux heuristiques
suivantes.
- h0(n) = 0
- h1(n) = “la distance entre n et B sur l’axe des x”
- h2(n) = “la distance entre n et B sur l’axe des y”
- h3(n) = “la distance à vol d’oiseau entre n et B”
- h4(n) = “la distance de Manhattan entre n et B”

## Parmi ces heuristiques, lesquelles sont admissibles ?
Toutes les heuristiques sont admissibles à l'exception de h4(n), c'est-à-dire la distance de Manhattan. h4 n'est pas admissible, car il retourne une distance restante surévaluée, ce qui peut conduire à la découverte d'une solution suboptimale.

# Questions - Expérimentation
## L’utilisation des différentes heuristiques a-t-elle une influence sur l’efficacité de la recherche ?(en termes du nombre de noeuds visités)
Oui, le choix d'une heuristique est primordial, cependant il est important de comprendre qu'il y a plusieurs situations distinctes:
- heuristique minimisant la distance totale (comme h0, h1 ou h2) -> Prendra plus d'itérations que h3, mais conduit quand même à la solution optimale
- heuristique surévaluant la distance totale (comme h4) -> Peut prendre moins d'itérations que h3, mais en contre partie n'assure pas d'avoir le chemin optimal!

Il important de comprendre qu’une heuristique surévaluant la distance totale permet de réduire le nombre de cycles, ce qui peut être très utile lorsque l'on cherche une bonne solution et non pas une solution optimale qui prendrait plus de temps.

Cet effet est utilisé dans des variantes de A* tel que WA*(weighted A*). Dans cet algorithme, l'heuristique h est multipliée par un poids w. L'algorithme est ainsi généralement plus rapide, mais ne garantit plus une solution optimale.

## Pouvez-vous trouver des exemples où l’utilisation de différentes heuristiques donne des résultats différents en termes de chemin trouvé ?
Un exemple concret de ce problème peut être constaté sur le trajet Paris-Prague.
Résultats pour trajet Paris-Prague:
- h0 -> Paris/Brussels/Amsterdam/Munich/Prague | Total Length : *1089*
- h1 -> Paris/Brussels/Amsterdam/Munich/Prague | Total Length : *1089*
- h2 -> Paris/Brussels/Amsterdam/Munich/Prague | Total Length : *1089*
- h3 -> Paris/Brussels/Amsterdam/Munich/Prague | Total Length : *1089*
- h4 -> Paris/Brussels/Amsterdam/Hamburg/Berlin/Prague | Total Length : *1128*

On peut ainsi constater que l'heuristique h4 produit une solution suboptimale.

## Dans un cas réel, quelle heuristique utiliseriez-vous ?
Dans un cas réel, nous utiliserions très certainement h3 c'est-à-dire la distance à vol d'oiseau. Cette heuristique est totalement admissible, car elle ne retourna jamais une distance surestimée.

En ce qui concerne les autres heuristiques, h0 ne sera pas utilisé, car l'algorithme ne tiendra plus compte de la distance restante, mais uniquement de la distance déjà parcourue jusqu'au noeud, ce qui concrètement ne correspond plus à l'algorithme A*.

Pour les heuristiques h1 et h2 celles-ci ne sont pas adaptées, car elles ne tiennent pas compte des deux dimensions et une ville très fortement éloignée en x peu être très proche en y par exemple.

L'heuristique de Manhattan (h4) elle n'est pas admissible comme expliqué précédèrent, mais peut dans certains cas ou nous ne cherchons pas une solution optimale, mais une bonne solution dans un temps respectable être utilisée.

# Références
- https://fr.wikipedia.org/wiki/Algorithme_A*