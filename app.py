import streamlit as st
import chess
import chess.svg
import random

st.set_page_config(
    page_title="Chess960 Generator",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🎲 Chess960 Position Generator")
st.markdown("Instantly generate legal starting positions for *Fischer Random Chess*. Copy the FEN string and start playing!")
st.markdown("---")

if 'fischer_id' not in st.session_state:
    st.session_state.fischer_id = random.randint(0, 959)

col1, col2 = st.columns([1.2, 1], gap="large")

board = chess.Board.from_chess960_pos(st.session_state.fischer_id)

with col1:
    st.subheader("🖥️ The Board")
    boardsvg = chess.svg.board(
        board=board,
        size=450,
        colors={
            "square light": "#dee3e6",
            "square dark": "#8ca2ad",
            "margin": "#262730",
            "coord": "#dee3e6"
        }
    )
    st.image(boardsvg)

with col2:
    st.subheader("📊 Position Details")
    st.info(f"**Current Chess960 Variation:** #{st.session_state.fischer_id:03d}")
    
    if st.button("🔄 Generate New Position", type="primary", use_container_width=True):
        st.session_state.fischer_id = random.randint(0, 959)
        st.rerun()
        
    st.markdown("---")
    st.markdown("**Position FEN String:**")
    st.code(board.fen(), language="text")
    
    st.markdown(
        """
        💡 **How to use it:**
        1. Copy the FEN string above.
        2. Go to [Lichess.org/analysis](https://lichess.org/analysis) or [Chess.com/analysis](https://www.chess.com/analysis).
        3. Paste it into the **FEN** input field to start playing or analyzing the setup!
        """
    )

st.markdown("---")
st.caption("Built with ❤️ using Python, Streamlit, and python-chess.")