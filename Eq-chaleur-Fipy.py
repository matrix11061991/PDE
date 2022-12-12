from fipy import Grid1D, TransientTerm, DiffusionTerm, Viewer

# Créer un maillage 1D avec 100 points
mesh = Grid1D(nx=100)

# Définir la fonction de température initiale
u = CellVariable(name="temperature", mesh=mesh, value=0.0)

# Définir les constantes de l'équation de la chaleur
alpha = 0.01
dt = 0.1

# Définir le terme de dérivée temporelle et le terme de diffusion de l'équation
eq = TransientTerm(coeff=1.0 / dt) == DiffusionTerm(coeff=alpha)

# Créer un visualiseur pour afficher la solution
viewer = Viewer(vars=u, datamin=0.0, datamax=1.0)

# Exécuter la boucle de résolution de l'équation
for t in range(100):
    eq.solve(var=u)
    viewer.plot()
