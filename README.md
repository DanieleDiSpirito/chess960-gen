# 🎲 Chess960 Position Generator

A minimal and modern web application built in Python using **Streamlit** to instantly generate legal starting positions for **Chess960** (Fischer Random Chess).

The app randomly generates one of the 960 possible starting layouts, renders a clean, modern chessboard, and provides the FEN string ready to be copied and pasted into platforms like Lichess or Chess.com.


## 🚀 Features

- **Instant Generation:** Click a single button to cycle through all 960 legal variations.
- **Modern UI:** Clean two-column layout optimized for both desktop and mobile screens.
- **Custom Themes:** Chessboard rendered with a sleek, modern blue-gray color palette (Lichess style).
- **FEN Export:** Copy the FEN string with one click to study or play the position immediately.
- **Cloud Ready:** Fully configured for instant, free deployment on Streamlit Community Cloud.

## 🛠️ Tech Stack

- [Python](https://www.python.org/) (Core logic)
- [Streamlit](https://streamlit.io/) (UI and Web Server)
- [python-chess](https://github.com/niklasf/python-chess) (Chess variant rules and SVG rendering)


## 💻 Local Installation

If you want to clone this repository and run the application locally on your machine, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/DanieleDiSpirito/chess960-gen.git](https://github.com/DanieleDiSpirito/chess960-gen.git)
   cd YOUR_REPO_NAME
   ```
2. **Install dependencies**
    ```
    python install -r requirements.txt
    ```
3. **Launch the app**
    ```
    streamlit run app.py
    ```

## 📄 License

This project is open-source and available under the MIT License.

Built with ❤️ using Python and Streamlit.