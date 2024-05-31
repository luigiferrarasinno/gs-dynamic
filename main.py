import matplotlib.pyplot as plt
import numpy as np

def criar_grafico():
    """
    Cria uma figura e um eixo tridimensional para desenhar o cubo.

    Returns:
        fig (matplotlib.figure.Figure): A figura criada.
        ax (mpl_toolkits.mplot3d.axes3d.Axes3D): O eixo tridimensional.
    """
    fig = plt.figure()  # Cria uma nova figura
    ax = fig.add_subplot(111, projection='3d')  # Adiciona um eixo 3D à figura
    return fig, ax

def desenhar_cubo(ax, limite):
    """
    Desenha um cubo no eixo tridimensional dado.

    Args:
        ax (mpl_toolkits.mplot3d.axes3d.Axes3D): O eixo tridimensional onde o cubo será desenhado.
        limite (float): O tamanho do lado do cubo.

    """
    # Criando os pontos do cubo
    x = [0, limite, limite, 0, 0, limite, limite, 0]
    y = [0, 0, limite, limite, 0, 0, limite, limite]
    z = [0, 0, 0, 0, limite, limite, limite, limite]

    # Definindo as arestas do cubo
    vertices = [
        [0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4],
        [2, 3, 7, 6], [0, 3, 7, 4], [1, 2, 6, 5]
    ]

    # Desenhando o cubo
    for v in vertices:
        ax.plot([x[v[0]], x[v[1]]], [y[v[0]], y[v[1]]], [z[v[0]], z[v[1]]], 'b')
        ax.plot([x[v[1]], x[v[2]]], [y[v[1]], y[v[2]]], [z[v[1]], z[v[2]]], 'b')
        ax.plot([x[v[2]], x[v[3]]], [y[v[2]], y[v[3]]], [z[v[2]], z[v[3]]], 'b')
        ax.plot([x[v[3]], x[v[0]]], [y[v[3]], y[v[0]]], [z[v[3]], z[v[0]]], 'b')


def criar_sensores(raio, num_sensores, limite):
    """
    Cria coordenadas para um número específico de sensores dentro de um cubo com um limite de tamanho.

    Args:
        raio (float): O raio do sensor.
        num_sensores (int): O número de sensores a serem criados.
        limite (float): O tamanho do lado do cubo dentro do qual os sensores devem ser criados.

    Returns:
        coord_sensores (numpy.ndarray): As coordenadas dos sensores criados.
    """
    # Coordenadas dos sensores (distribuídas aleatoriamente, mas sem colisões para este exemplo)
    coord_sensores = np.zeros((num_sensores, 3))

    for i in range(num_sensores):
        while True:
            # Gerar uma posição aleatória para o sensor
            posicao_potencial = np.random.rand(3) * limite

            # Verificar se a posição colide com qualquer sensor existente
            if i > 0:
                distancias = np.sqrt(np.sum((coord_sensores[:i] - posicao_potencial)**2, axis=1))
                if np.any(distancias < 2 * raio):
                    continue  # Se houver uma colisão, gerar uma nova posição

            # Se não houver colisões, adicionar o sensor à lista
            coord_sensores[i] = posicao_potencial
            break

    return coord_sensores


def desenhar_sensores(num_sensores, ax, coord_sensores, raio):
    """
    Desenha os sensores e seus raios de alcance no gráfico.

    Args:
        num_sensores (int): O número de sensores.
        ax (mpl_toolkits.mplot3d.axes3d.Axes3D): O eixo tridimensional onde os sensores serão desenhados.
        coord_sensores (numpy.ndarray): As coordenadas dos sensores.
        raio (float): O raio de alcance dos sensores.

    """
    # Desenhando os sensores e seus raios de alcance
    for i in range(num_sensores):
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = coord_sensores[i, 0] + raio * np.outer(np.cos(u), np.sin(v))
        y = coord_sensores[i, 1] + raio * np.outer(np.sin(u), np.sin(v))
        z = coord_sensores[i, 2] + raio * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(x, y, z, color='r', alpha=0.3)

def gerar_lixo(num_lixos, limite):
    """
    Gera coordenadas para um número específico de "lixos" dentro de um cubo com um limite de tamanho.

    Args:
        num_lixos (int): O número de "lixos" a serem gerados.
        limite (float): O tamanho do lado do cubo dentro do qual os "lixos" devem ser gerados.

    Returns:
        coord_lixos (numpy.ndarray): As coordenadas dos "lixos" gerados.

    """
    # Adicionando "lixos"
    coord_lixos = np.random.rand(num_lixos, 3) * limite
    return coord_lixos

def desenhar_lixo(ax, coord_lixos):
    """
    Desenha os "lixos" no gráfico.

    Args:
        ax (mpl_toolkits.mplot3d.axes3d.Axes3D): O eixo tridimensional onde os "lixos" serão desenhados.
        coord_lixos (numpy.ndarray): As coordenadas dos "lixos".

    """
    ax.scatter(coord_lixos[:, 0], coord_lixos[:, 1], coord_lixos[:, 2], color='gray', alpha=0.5)

def verificar_lixo_encontrado(num_sensores, num_lixos, coord_sensores, coord_lixos, raio):
    """
    Verifica quantos "lixos" foram encontrados por cada sensor.

    Args:
        num_sensores (int): O número de sensores.
        num_lixos (int): O número de "lixos".
        coord_sensores (numpy.ndarray): As coordenadas dos sensores.
        coord_lixos (numpy.ndarray): As coordenadas dos "lixos".
        raio (float): O raio de alcance dos sensores.

    Returns:
        lixo_encontrado (numpy.ndarray): Um array contendo o número de "lixos" encontrados por cada sensor.

    """
    # Contabilizando o "lixo" encontrado por cada sensor
    lixo_encontrado = np.zeros(num_sensores, dtype=int)
    for i in range(num_sensores):
        for j in range(num_lixos):
            distancia = np.sqrt(np.sum((coord_sensores[i] - coord_lixos[j])**2))
            if distancia <= raio:
                lixo_encontrado[i] += 1

    return lixo_encontrado

def adicionar_total_lixo_encontrado(lixo_encontrado):
    """
    Adiciona o total de "lixo" encontrado ao gráfico.

    Args:
        lixo_encontrado (numpy.ndarray): Um array contendo o número de "lixos" encontrados por cada sensor.

    """
    # Adicionando o total de "lixo" encontrado ao gráfico
    total_lixo = np.sum(lixo_encontrado)
    plt.figtext(0.2, 0.02, 'Total de "lixo" encontrado: {}'.format(total_lixo), ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})

def ajustar_grafico(ax, limite):
    """
    Ajusta os limites e etiquetas dos eixos do gráfico.

    Args:
        ax (mpl_toolkits.mplot3d.axes3d.Axes3D): O eixo tridimensional do gráfico.
        limite (float): O tamanho do lado do cubo que define os limites do gráfico.

    """
    # Ajustando os limites dos eixos
    ax.set_xlim(0, limite)
    ax.set_ylim(0, limite)
    ax.set_zlim(0, limite)

    # Etiquetas dos eixos
    ax.set_xlabel('X (metros)')
    ax.set_ylabel('Y (metros)')
    ax.set_zlabel('Z (metros)')

    # Título do gráfico
    ax.set_title('Gráfico tridimensional de distribuição de sensores no mar')

def main():
    """
    Função principal que executa o programa.

    Solicita ao usuário se deseja inserir valores personalizados ou usar os valores padrão.
    Em seguida, cria o gráfico tridimensional com os sensores, "lixos" e suas interações.

    """
    op = input("Deseja colocar valores personalizados? (y/n): ")
    if op == "y":
        limite_usuario = int(input("Digite o alcance máximo da área do gráfico em km: "))
        limite = limite_usuario * 1000
        num_sensores = int(input("Digite a quantidade de sensores que deseja usar: "))
        raio_usuario = int(input("Digite o alcance do raio em km de cada sensor: "))
        raio = raio_usuario * 1000
        num_lixos = int(input("Digite a quantidade total de lixos presentes: "))
    else:
        # Usando os valores padrão
        limite = 50000  # 50 km em metros
        num_sensores = 10
        raio = 5000  # raio de alcance do sensor em metros
        num_lixos = 100  # número de "lixos"

    # Criando a figura e o eixo tridimensional
    fig, ax = criar_grafico()

    # Desenhando o cubo que representa a área de atuação
    desenhar_cubo(ax, limite)

    # Criando e desenhando os sensores
    coord_sensores = criar_sensores(raio, num_sensores, limite)
    desenhar_sensores(num_sensores, ax, coord_sensores, raio)

    # Gerando e desenhando os "lixos"
    coord_lixos = gerar_lixo(num_lixos, limite)
    desenhar_lixo(ax, coord_lixos)

    # Verificando quantos "lixos" foram encontrados por cada sensor
    lixo_encontrado = verificar_lixo_encontrado(num_sensores, num_lixos, coord_sensores, coord_lixos, raio)

    # Adicionando o total de "lixo" encontrado ao gráfico
    adicionar_total_lixo_encontrado(lixo_encontrado)

    # Ajustando os limites e etiquetas dos eixos do gráfico
    ajustar_grafico(ax, limite)

    # Exibindo o gráfico
    plt.show()


if __name__ == "__main__":
    main()
