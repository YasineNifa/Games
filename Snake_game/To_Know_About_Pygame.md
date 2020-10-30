# Pygame

```
screen = pygame.display.set_mode((720, 480))  # Notice the tuple! It's not 2 arguments.
clock = pygame.time.Clock()
FPS = 60  # This variable will define how many frames we update per second.
```

- Nous devons également créer un affichage. Pygame a déjà créé un affichage (caché), il suffit donc de définir le mode d'affichage (dans cet exemple, nous ne définissons que la résolution). Il est également judicieux de créer une horloge pour s’assurer que nos programmes sont mis à jour à une vitesse fixe (sinon, la vitesse serait différente selon la vitesse de l’ordinateur).



```
rect = pygame.Rect((0, 0), (32, 32))  # First tuple is position, second is size.
image = pygame.Surface((32, 32))  # The tuple represent size.
image.fill(WHITE)  # We fill our surface with a nice white color (by default black).
```
- Dans pygame, nous utilisons généralement une surface pour représenter l'apparence d'un objet et une rect (rectangle) pour représenter la position d'un objet. Une surface est comme une feuille de papier vierge contenant des couleurs ou des images. Si vous créez une classe, vous devez nommer les attributs image et rect car de nombreuses fonctions recherchent et utilisent ces attributs. De telles classes en tireraient avantage en héritant de la classe pygame.sprite.Sprite pour les raisons que vous pouvez lire ici .


- Ensuite, nous gérerons les événements. Un événement est essentiellement une action de l'utilisateur, telle que déplacer la souris ou appuyer sur une touche. Pygame enregistrera tous ces événements dans une file d'attente pygame.event.get() appelant pygame.event.get() . Nous pouvons itérer cela et vérifier s'il y a un événement que nous aimerions gérer. Les événements ont un attribut type que nous pouvons vérifier avec les constantes du module pygame pour déterminer le type d’événement.