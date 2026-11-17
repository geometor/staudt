:layout: book
:canonical_id: § 6
:breadcrumb_title: § 6
:order: 7
:folio: § 6
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _geometrie-sec_06-de:
.. _geometrie-unit-2-de:

.. folio:: § 6
   :page: 29

§ 6. Vollständige Vierecke und harmonische Gebilde (Art. 66–74)
===============================================================

.. rubric:: Karl Georg Christian von Staudt — *Geometrie der Lage* (Nürnberg, 1847), § 6 (Art. 66–74)

**Art. 66.** Vier in einer Ebene liegende Punkte $E, F, G, H$, von welchen keine drei in einer Geraden liegen, bestimmen sechs Verbindungsgerade (*Seiten*), die sich zu drei Paaren *Gegenseiten* ordnen:

.. math::

   ([EF], [GH]), \qquad ([FG], [HE]), \qquad ([EG], [FH]).

Ein solches Gebilde heißt ein :term:`vollständiges ebenes Viereck <vollstaendiges-viereck>`, und die drei Schnittpunkte je zweier Gegenseiten heißen seine **Diagonalpunkte**. Dual bestimmen vier Gerade einer Ebene, von welchen keine drei durch einen Punkt gehen, ein *vollständiges ebenes Vierseit* mit sechs Ecken und drei *Diagonalen*.

**Art. 67.** Geht eine Gerade $\ell$ durch zwei Diagonalpunkte $A = [EF] \cap [GH]$ und $B = [FG] \cap [HE]$ eines vollständigen ebenen Vierecks $EFGH$, und schneiden die beiden übrigen Gegenseiten $[EG]$ und $[FH]$ die Gerade $\ell$ in $C$ und $D$, so heißen $A, C, B, D$ **vier harmonische Punkte** (:term:`harmonisches Gebilde <harmonisches-gebilde>`), und zwar heißt $D$ **der vierte harmonische Punkt** zu $A, B, C$, zugeordnet dem Punkte $C$ in bezug auf das Paar $(A, B)$.

.. picture:: /_static/figures/unit2_complete_quadrangle_harmonic.svg
   :alt: Vollständiges ebenes Viereck EFGH schneidet den Träger l in vier harmonischen Punkten A, C, B, D.
   :caption: **Konstruktion des vierten harmonischen Punktes allein mit dem Lineal (1847 § 6, Art. 67):** Zu drei kollinearen Punkten $A, B, C$ liefert das vollständige Viereck $EFGH$ eindeutig den vierten harmonischen Punkt $D$.

**Art. 70 (Räumlicher Eindeutigkeitsbeweis).** *Durch drei in einer Geraden liegende Punkte $A, B, C$ ist der vierte harmonische Punkt $D$ vollkommen bestimmt und von der Wahl der Hilfsebene wie des vollständigen Vierecks unabhängig.*

*Beweis.* Liegt ein zweites vollständiges Viereck $E'F'G'H'$ in einer **anderen** durch $\ell = [AB]$ gehenden Ebene $\alpha'$, dergestalt daß $[E'F'] \cap [G'H'] = A$, $[F'G'] \cap [H'E'] = B$ und $[E'G']$ durch $C$ geht, so schneiden sich $[EG]$ und $[E'G']$ in $C$; mithin liegen $[EE']$ und $[GG']$ in einer Ebene und schneiden sich in einem Zentrum $S$ außerhalb $\alpha$ und $\alpha'$. Aus $S$ projizieren sich $E, G, F, H$ unmittelbar in $E', G', F', H'$; folglich liegen $[FH]$ und $[F'H']$ in einer durch $S$ gehenden Ebene und treffen die Schnittgerade $\ell = \alpha \cap \alpha'$ in **einem und demselben Punkte** $D = D'$. Ein drittes in $\alpha$ selbst gelegenes Viereck stimmt ebenso mit $E'F'G'H'$ und daher auch mit $EFGH$ überein. $\blacksquare$

**Art. 72.** In jedem harmonischen Gebilde $(A, B; C, D)$ lassen sich die beiden Paare zugeordneter Elemente $(A, B)$ und $(C, D)$ miteinander sowie die beiden Elemente jedes Paares untereinander vertauschen; überdies :term:`trennen <getrennte-paare>` die Punkte $A, B$ stets die Punkte $C, D$.
