rem Windows batch scripts feel like Bizzaro bash scripts.
rem Strange, yet strangely familiar.

SETLOCAL
SET MY_BOT=MyBot.py
SET PYTHON=python

rem if hash python3 2>/dev/null; then
rem     %%PYTHON=python3
rem fi

for %%SOME_BOT in (*Bot.py) do ^
    .\halite.exe -d "30 30" "%%PYTHON %%MY_BOT" "%%PYTHON %%SOME_BOT"
