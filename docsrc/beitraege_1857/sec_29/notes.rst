:layout: book
:canonical_id: § 29
:breadcrumb_title: § 29
:order: 3
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _beitraege-sec_29-notes:

Critical Notes: § 29. The Harmonic Scale & Projective Abscissae (arts. 403–404)
===============================================================================

.. rubric:: Scholarly Commentary — Karl Georg Christian von Staudt — *Beiträge, Zweites Heft* (1857), § 29 (arts. 403–404)

* **Exact Projective Abscissa Formula in ``geometor.staudt``**: Relative to finite gauge points $P_0, P_1, P_\infty$ on $\ell$, ``projective_abscissa(P0, P1, Pinf, X)`` evaluates the exact invariant $(X, P_1; P_0, P_\infty)$. For instance, on $P_0 = (0, 0)$, $P_1 = (1, 0)$, $P_\infty = (8, 0)$, a point $P_k$ of projective abscissa $k$ has exact rational Cartesian coordinate:

  .. math::

     x(P_k) = \frac{8k}{k + 7},

  so $P_1 = (1, 0)$, $P_2 = \left(\frac{16}{9}, 0\right)$, $P_3 = \left(\frac{12}{5}, 0\right)$, $P_5 = \left(\frac{10}{3}, 0\right)$, and $P_6 = \left(\frac{48}{13}, 0\right)$—matching ``construct_von_staudt_addition`` ($P_2 + P_3 = P_5$) and ``construct_von_staudt_multiplication`` ($P_2 \cdot P_3 = P_6$) identically!
* **The Golden Throw Identity over $\mathbb{Q}(\phi)$ (``geometor/divine`` Bridge)**: In ``verify_golden_throw_identity``, placing the golden abscissa $\phi = \frac{1 + \sqrt{5}}{2}$ at $P_\phi = \left(\frac{4 + 28\sqrt{5}}{55}, 0\right)$ on the horizon-8 carrier and executing **both** von Staudt's straightedge product $P_\phi \cdot P_\phi$ and straightedge sum $P_\phi + P_1$ produces the exact same symbolic point $\left(\frac{92 + 28\sqrt{5}}{71}, 0\right)$ of abscissa $\phi^2 = \phi + 1 = \frac{3 + \sqrt{5}}{2}$, while its Galois conjugate $\hat{\phi} = 1 - \phi$ satisfies $P_\phi + P_{\hat{\phi}} = P_1$ (trace $1$) and $P_\phi \cdot P_{\hat{\phi}} = P_{-1}$ (norm $-1$).
