import json
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#essa bosta é relacionada com a função de gerar o grafico, essa bosta é pra mexer onde ta alguma merda n entendi n quero mais entender va tudo pra bosta melada de bosta fodaose morram sofram fodase vai tomanocu nunca mais quero ler essa bosta some, por isos nunca estudei matematica vsf um monte de imvecil fingindo q algo é mais dificil q é por isso o mundo é atrasado pra caralho, bando de pavao imvecil ou um completo asno que so sabe peidar arrotar e comer traveco bebado, parabens aos imvolvidos
ORTHO_LEFT = 0
ORTHO_RIGHT = 4
ORTHO_BOTTOM = 4
ORTHO_TOP = -1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Graphs in Python")


def init_ortho():
    glMatrixMode(GL_PROJECTION) #glMatrixMode(GL_PROJECTION) seleciona a matriz de projeção, que é responsável por definir como as coordenadas 3D são projetadas na tela 2D, GL_PROJECTION é a constante que indica que queremos configurar a matriz de projeção.
    glLoadIdentity() #glLoadIdentity() reseta a matriz de projeção para o estado padrão, garantindo que as transformações anteriores não afetem a nova configuração ortográfica.
    gluOrtho2D(ORTHO_LEFT, ORTHO_RIGHT, ORTHO_TOP, ORTHO_BOTTOM) #gluOrtho2D(ORTHO_LEFT, ORTHO_RIGHT, ORTHO_TOP, ORTHO_BOTTOM) define uma projeção ortográfica 2D, onde os parâmetros especificam os limites do espaço de coordenadas que queremos usar para desenhar. ORTHO_LEFT e ORTHO_RIGHT definem os limites horizontalmente, enquanto ORTHO_TOP e ORTHO_BOTTOM definem os limites verticalmente. Isso significa que as coordenadas que enviarmos para desenhar serão mapeadas para esse espaço definido. #q: Esses argumentos ortagonais precisam ou nao ter esses nomes? # r: não #q: O que é ortogonal e o que tem a ver? # r: Ortogonal é um tipo de projeção onde os objetos são projetados sem perspectiva, ou seja, as linhas paralelas permanecem paralelas. Isso é útil para gráficos 2D, onde queremos que as formas mantenham suas proporções independentemente da distância. A função gluOrtho2D define esse tipo de projeção, permitindo que desenhemos em um espaço 2D sem distorção de perspectiva.#q: Qual a etimologia de ortogonal? # r: A palavra "ortogonal" vem do grego "orthos" (reto) e "gonia" (ângulo), significando literalmente "ângulo reto".

def map_value(value, src_min, src_max, dst_min, dst_max):
    if src_max == src_min:
        return dst_min
    return dst_min + (value - src_min) * (dst_max - dst_min) / (src_max - src_min)

# Essa função traduz coordenadas de tela (pixels) para o espaço cartesiano definido acima.
# def plot_graph():
#     glBegin(GL_LINE_STRIP)
#     for px in np.arange(0.0, 4.0, 0.005):
#         py = math.exp(-px) * math.cos(2 * math.pi * px)
#         glVertex2f(px, py)
#     glEnd()

# def save_drawing(point_groups):
#     with open("drawing.txt", "w", encoding="utf-8") as f:
#         f.write(f"{len(point_groups)}\n")
#         for line in point_groups:
#             f.write(f"{len(line)}\n")
#             for x, y in line:
#                 f.write(f"{x} {y}\n")
#     print("Drawing saved to drawing.txt")


def plot_lines(point_groups):
    for line in point_groups:
        if not line:
            continue
        glBegin(GL_LINE_STRIP)
        for x, y in line:
            glVertex2f(x, y)
        glEnd()

# A cada `glBegin`/`glEnd` o OpenGL conecta pontos consecutivos com linhas.
import json
import os

def save_points_json(point_groups):
    # Obtém o diretório onde o script atual está localizado
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Une o diretório ao nome do arquivo
    file_path = os.path.join(script_dir, "1_exe.json")

    payload = [
        [{"x": float(x), "y": float(y)} for x, y in line]
        for line in point_groups
    ]
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    
    print(f"Coordinates saved to {file_path}")

def main():
    init_ortho()
    glPointSize(5)
    # normalmente essas variaveis nao seriam globais e seriam estruturas mais complexas que arrays, mas ta bom pra esse exemplo
    points = []
    current_line = []
    mouse_down = False
    running = True
    while running:
        # O pygame coloca todos os eventos ocorridos em uma fila; iteramos para reagir a cada um.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # quero salvar usando s e/ou esc, como faz isso no pygame
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                # O K significa key. #Tem uma lista enorme de teclas em https://www.pygame.org/docs/ref/key.html#pygame.key.key_code
                save_points_json(points)
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_down = True
                current_line = []
                points.append(current_line)
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                mouse_down = False
            elif event.type == MOUSEMOTION and mouse_down:
                x = map_value(event.pos[0], 0, SCREEN_WIDTH, ORTHO_LEFT, ORTHO_RIGHT)
                y = map_value(event.pos[1], 0, SCREEN_HEIGHT, ORTHO_BOTTOM, ORTHO_TOP)
                current_line.append((x, y))

        # Limpa o buffer e reseta a matriz para desenhar cada frame do zero.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Aqui escolhemos a matriz que vai transformar as coordenadas que enviamos em `glVertex`.
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # plot_graph()
        plot_lines(points)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
