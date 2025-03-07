from PIL import Image, ImageDraw, ImageSequence

# Configuración
width, height = 500, 100  # Tamaño de la imagen
frames = 20  # Número de cuadros de la animación
pacman_radius = 20  # Tamaño de Pac-Man
dot_radius = 5  # Tamaño de los puntos
dot_spacing = 40  # Espacio entre los puntos
background_color = (0, 0, 0)  # Fondo negro
pacman_color = (255, 255, 0)  # Amarillo
dot_color = (255, 255, 255)  # Blanco

# Posiciones de los puntos
dots_x_positions = list(range(50, width - 50, dot_spacing))
dots_y = height // 2

# Crear frames de la animación
frames_list = []
for i in range(frames):
    img = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(img)

    # Dibujar los puntos (solo los que Pac-Man aún no ha comido)
    for x in dots_x_positions:
        if x > 50 + i * (width // frames):
            draw.ellipse((x - dot_radius, dots_y - dot_radius, x + dot_radius, dots_y + dot_radius), fill=dot_color)

    # Dibujar a Pac-Man con una apertura animada
    mouth_angle = 30 if i % 2 == 0 else 10
    pacman_x = 50 + i * (width // frames)
    pacman_y = dots_y

    draw.pieslice((pacman_x - pacman_radius, pacman_y - pacman_radius, pacman_x + pacman_radius, pacman_y + pacman_radius), 
                  mouth_angle, 360 - mouth_angle, fill=pacman_color)

    frames_list.append(img)

# Guardar la animación
frames_list[0].save("pacman.gif", save_all=True, append_images=frames_list[1:], duration=100, loop=0)
print("✅ Pac-Man GIF generado como 'pacman.gif'")
