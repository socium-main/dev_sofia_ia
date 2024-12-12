from IPython.display import Image
from misc import get_current_time

def save_graph_as_jpeg(graph):
    # # Salva o grapho em formato de jpeg na raiz da chain
    img = Image(graph.get_graph(xray=True).draw_mermaid_png())
    time = get_current_time()
    img_file_path = f"/home/aka_nio/socium/Sofia_IA/chain/graph_{time}.jpeg"
    with open(img_file_path, "wb") as f:
        f.write(img.data)

    print(f"Graph saved as {img_file_path}")