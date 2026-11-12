:layout: book

.. _geometrie-unit-4-de:

Einheit 4: Rechnung mit Würfen — Summen, Produkte & projektivische Abscissen
============================================================================

.. rubric:: Karl Georg Christian von Staudt — *Beiträge zur Geometrie der Lage, Zweites Heft* (Nürnberg, 1857), §§ 19, 20, 29 (Art. 256–269, 403–404)

.. contents:: Inhalt dieser Einheit
   :local:
   :depth: 2
   :backlinks: none

.. folio:: § 19
   :page: 166

§ 19. Rechnung mit Würfen — Begriff und Addition (Art. 256–267)
---------------------------------------------------------------

**Art. 256.** Vier Elemente $A, B, C, D$ eines :term:`einförmigen Grundgebildes <grundgebilde>` bestimmen in einer festgesetzten Reihenfolge einen :term:`Wurf <wurf>` $(ABCD)$. Zwei Würfe $(ABCD)$ und $(A'B'C'D')$ heißen **einander gleich**, wenn die beiden Grundgebilde projektivisch so aufeinander bezogen werden können, daß den Elementen $A, B, C, D$ der Reihe nach die Elemente $A', B', C', D'$ entsprechen.

Wählt man auf einem geraden Träger $\ell$ drei feste verschiedene Grundpunkte $P_0$ (*Nullpunkt*), $P_1$ (*Einheitspunkt*) und $P_\infty$ (*Grenzpunkt*), so vertritt jeder von $P_\infty$ verschiedene Punkt $X$ der Geraden eindeutig den Wurf $(P_\infty P_0 P_1 X)$; $P_0$ vertritt den **Nullwurf**, $P_1$ den **Einheitswurf**.

**Art. 259 (Summen von Würfen allein mit dem Lineal).** Um zu zwei von $P_\infty$ verschiedenen Punkten $X, Y$ des Trägers $\ell$ in bezug auf $(P_0, P_1, P_\infty)$ den Summenpunkt $S = X + Y$ allein mittels des Lineals zu konstruieren:

1. Man ziehe durch $P_\infty$ eine beliebige Hilfsgerade $m \neq \ell$ und nehme auf ihr zwei verschiedene Punkte $U, V$ außerhalb $\ell$ an.
2. Man verbinde $[U P_0]$ und $[V X]$ bis zu ihrem Schnittpunkte $R = [U P_0] \cap [V X]$.
3. Man ziehe die Perspektivitätsachse $a = [P_\infty R]$ durch $P_\infty$ und $R$.
4. Man schneide $[U Y]$ mit $a$ in $T = [U Y] \cap a$; alsdann schneidet $[V T]$ den Träger $\ell$ in dem gesuchten Summenpunkte $S = X + Y$.

.. picture:: /_static/figures/unit4_addition_of_throws.svg
   :alt: Rein lineare Konstruktion der Summe zweier Würfe S = X + Y mittels zweier mit P_inf kollinearer Zentren U, V.
   :caption: **Summen von Würfen (1857 § 19, Art. 259):** Die durch $P_\infty$ gehende Zentrengerade $[P_\infty U V]$ und die Achse $a = [P_\infty R]$ liefern $S = X + Y$ allein durch sechs Linealschnitte.

**Art. 262.** Vermöge des Vierecksatzes ist $S$ von der Wahl der Hilfsgeraden $m$ und der Zentren $U, V$ völlig unabhängig, und es gelten allgemein die Gesetze:

.. math::

   X + P_0 = X, \qquad X + Y = Y + X, \qquad (X + Y) + Z = X + (Y + Z),

sowie für jedes $X \neq P_\infty$ die Existenz des entgegengesetzten Punktes $-X$ mit $X + (-X) = P_0$ als vierten harmonischen Punktes zu $(P_0, P_\infty; X)$.

.. folio:: § 20
   :page: 174

§ 20. Produkte aus Würfen (Art. 268–269)
----------------------------------------

**Art. 268.** Um in bezug auf dieselben Grundpunkte $(P_0, P_1, P_\infty)$ zu zwei Punkten $X, Y \in \ell \setminus \{P_0, P_\infty\}$ den Produktpunkt $P = X \cdot Y$ allein mit dem Lineal zu konstruieren:

1. Man lege durch den **Nullpunkt** $P_0$ eine beliebige Hilfsgerade $c \neq \ell$ und wähle auf ihr zwei verschiedene Punkte $U, V$ außerhalb $\ell$.
2. Man bestimme den Schnittpunkt $W = [U P_1] \cap [V X]$.
3. Man ziehe durch den **Grenzpunkt** $P_\infty$ und $W$ die Perspektivitätsachse $a = [P_\infty W]$.
4. Man schneide $[U Y]$ mit $a$ in $Z = [U Y] \cap a$; alsdann trifft $[V Z]$ den Träger $\ell$ in dem gesuchten Produktpunkte $P = X \cdot Y$.

.. picture:: /_static/figures/unit4_multiplication_of_throws.svg
   :alt: Rein lineare Konstruktion des Produktes zweier Würfe P = X * Y mittels zweier mit P_0 kollinearer Zentren U, V.
   :caption: **Produkte aus Würfen (1857 § 20, Art. 268):** Die durch $P_0$ gehende Zentrengerade $[P_0 U V]$ und die durch $P_\infty$ gehende Achse $a = [P_\infty W]$ lassen $P_0$ und $P_\infty$ fest und überführen $P_1 \mapsto X$, $Y \mapsto P = X \cdot Y$.

**Art. 269.** Für diese :term:`Rechnung mit Würfen <rechnung-mit-wuerfen>` gelten ohne jede Berufung auf Streckenlängen sämtliche Grundgesetze der Arithmetik: Kommutativität, Assoziativität und das Distributionsgesetz $X \cdot (Y + Z) = X \cdot Y + X \cdot Z$.

.. folio:: § 29
   :page: 255

§ 29. Harmonische Reihen und projektivische Koordinaten (Art. 403–404)
----------------------------------------------------------------------

**Art. 403.** Durch fortgesetzte Addition des Einheitspunktes $P_1$ entsteht auf $\ell$ die :term:`harmonische Reihe <harmonische-reihe>` $P_1, P_2, P_3, \dots, P_n, \dots$, worin durchgängig $(P_{n-1}, P_{n+1}; P_n, P_\infty)$ ein harmonisches Gebilde ist, und durch Umkehrung der Addition und Multiplikation entspricht jeder rationalen Zahl $p/q$ ein einziger konstruierbarer Punkt $P_{p/q}$ auf $\ell$.

.. picture:: /_static/figures/unit4_harmonic_scale_abscissae.svg
   :alt: Projektivische harmonische Reihe P_{-1}, P_0, P_1, ..., P_5 gegen den Grenzpunkt P_inf.
   :caption: **Harmonische Reihe und projektivische Abscissen (1857 § 29, Art. 403–404):** Fortgesetzte Viereckskonstruktionen erzeugen die ganzzahligen Punkte $P_n$ auf dem Träger $\ell$ ohne jeden Zirkel oder Maßstab.

**Art. 404.** Vermöge der Stetigkeit der Anordnung kommt hierdurch jedem reellen Punkte $X \neq P_\infty$ des Trägers $\ell$ in bezug auf $(P_0, P_1, P_\infty)$ eine vollkommen bestimmte Zahl als :term:`projektivische Abscisse <abscisse>` zu — gewonnen **allein aus Verknüpfung und Anordnung**, ehe irgendein Maßbegriff eingeführt wird.
