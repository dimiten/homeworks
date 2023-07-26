"""broj_u_indeksu = 105
rb_zad_2 = (rb_zad_1 + 4) % 8 + 1 """

"""Zadatak_7
(p -> (q -> r)) <-> ((p and q) -> r) """

# Ovaj zadatak zadatak sam probao da uradim preko funkcije da vidim da li cu moci i koliko vidim uspeo sam.


def tautologije(p, q, r):
    levi_deo = not q or r  # q -> r
    levi_ceo = not p or levi_deo  # p -> (q -> r)
    desni_deo = p and q  # p and q
    desni_ceo = not desni_deo or r  # (p and q) -> r
    ceo = (levi_ceo and desni_ceo) or not (levi_ceo or desni_ceo)  # (p -> (q -> r)) <-> ((p and q) -> r)
    print(p, q, r, ceo)


tautologije(True, True, True)
tautologije(True, True, False)
tautologije(True, False, True)
tautologije(True, False, False)
tautologije(False, True, True)
tautologije(False, True, False)
tautologije(False, False, True)
tautologije(False, False, False)
