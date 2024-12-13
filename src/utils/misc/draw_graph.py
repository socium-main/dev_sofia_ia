from IPython.display import Image
from src.utils.misc.time_formatter import get_current_time
import os

def save_graph_as_jpeg(graph, folder_name: str):
    # Diretório onde este arquivo está localizado
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Caminho completo para o diretório desejado
    parent_dir  = os.path.join(current_dir, '..', '..', '..')
    target_folder = os.path.join(parent_dir , folder_name)
    
    # Certifique-se de que o diretório existe (cria se não existir)
    os.makedirs(target_folder, exist_ok=True)

    # Caminho completo para salvar a imagem
    time = get_current_time()
    image_path = os.path.join(target_folder, time)
    # # Salva o grapho em formato de jpeg na raiz da chain
    img = Image(graph.get_graph(xray=True).draw_mermaid_png())
    img_file_path = image_path + ".jpeg"
    with open(img_file_path, "wb") as f:
        f.write(img.data)

    print(f"Graph saved as {img_file_path}")