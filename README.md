# Discord Chess Bot

An interactive Discord bot for playing chess and solving training puzzles directly in chat. Users can play against a built-in Stockfish engine, solve curated checkmate puzzles, and interact with a visual chessboard rendered after every move. Built with Python, discord.py, and the Stockfish engine for a complete, engaging chess experience.

---

## Features

- **Play against Stockfish**  
  Challenge a powerful chess engine with customizable difficulty.

- **Puzzle training mode**  
  Solve curated checkmate-in-N puzzles with instant feedback.

- **Visual board rendering**  
  Every move and puzzle update is sent as an image using SVG → PNG conversion.

- **User-specific sessions**  
  Tracks separate active games and puzzles for each user.

- **Resign and quit support**  
  Cleanly exit engine games or training sessions with commands.

---

## 💬 Commands

| Command         | Description                                      |
|-----------------|--------------------------------------------------|
| `!chess`        | Start a new game against the Stockfish engine    |
| `!move <move>`  | Make a move in algebraic notation (e.g., `e4`)   |
| `!resign`       | Resign your current game                         |
| `!board`        | Show your current game board                     |
| `!puzzle`       | Start a new training puzzle                      |
| `!check <move>` | Submit a move for your active puzzle             |
| `!help`         | DM list of commands with categories              |

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/discord-chess-bot.git
cd discord-chess-bot
```

## 3 Setup Discord Token/Bot
Guide website: https://www.writebots.com/discord-bot-token/


## 4 Configure Environment Variables

Create a `.env` file in the root of your project and add:

```env
DISCORD_API_TOKEN=your_discord_bot_token
GUILD_ID=your_discord_server_id
```

## 5. Download and configure Stockfish
  - Download Stockfish from: https://stockfishchess.org/download/
  - Place the binary in `resources/`
  - Update the filename in ChessGameWithEngine if needed.

## Notes
- Make sure you download the correct Stockfish binary for your OS (macOS, Windows, or Linux).
- Each user can only have one active puzzle or engine game at a time.
- Temporary PNG files are deleted when puzzles or games end.

## Future Features?
- PvP Discord chess support
- Player stats and Elo-based leaderboards
- PGN import/export for games and puzzles
- Natural language input (e.g., "pawn to e4")
- **Feel  to contribute!**

## Credits
Created by Connor Buckley

## Liscense
MIT Liscense
