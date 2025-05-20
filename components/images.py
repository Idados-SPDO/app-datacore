from pathlib import Path
import streamlit as st

# caminho relativo ao cwd; garanta que ./assets/imgs exista no deploy
IMG_DIR = Path("./assets/imgs")

@st.cache_data
def list_imgs():
    """Retorna todos os arquivos de imagem na pasta assets/imgs."""
    if not IMG_DIR.exists():
        return []
    # aqui você pode ajustar as extensões que quiser suportar
    exts = (".png", ".jpg", ".jpeg", ".gif")
    return [p for p in IMG_DIR.iterdir() if p.suffix.lower() in exts]

def render_imgs(selected_base: str):
    # título igual ao seu exemplo
    demo_imgs = []
    desc_imgs = []

    # percorre todos os arquivos e filtra por prefixo + suffix
    for img_path in list_imgs():
        # img_path.name = "<prefixo>_<sufixo>.<ext>"
        parts = img_path.stem.split("_", 1)
        if len(parts) != 2:
            continue
        prefixo, sufixo = parts
        if prefixo != selected_base:
            continue

        sufixo = sufixo.lower()
        if sufixo.startswith("demonstrativo"):
            demo_imgs.append(img_path)
        elif sufixo.startswith("descritiva"):
            desc_imgs.append(img_path)

    # seção de demonstração
    if demo_imgs:
        st.markdown("### 6.1 Demonstração dos Dados")
        for img in demo_imgs:
            st.image(str(img), use_container_width=True)

    # seção de estatísticas
    if desc_imgs:
        st.markdown("### 6.2 Estatísticas Descritivas")
        for img in desc_imgs:
            st.image(str(img), use_container_width=True)
