from ursina import *
from ursina.shaders import lit_with_shadows_shader
app = Ursina()
DirectionalLight(position = Vec3(0, 10, 10), shadows = True, scale = Vec3(10, 10, 10), rotation = Vec3(45, 180, 180))
Entity(position = Vec3(0, 0, 0), scale = Vec3(1, 1, 1), model = 'sphere', color = Color(0.33022618293762207, 0.24488703906536102, 0.45999109745025635, 1.0), shader = lit_with_shadows_shader, rotation = Vec3(0, 0, 0))
Sky()
app.run()