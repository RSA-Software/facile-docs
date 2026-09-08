@echo off
setlocal

rem ---------------------------------------------------------------------
rem  start.bat - Manuale Facile
rem
rem  Verifica Python e i pacchetti necessari (mkdocs, mkdocs-material),
rem  li installa se mancano o non sono compatibili, poi avvia il server
rem  locale di anteprima su http://127.0.0.1:8000
rem
rem  Uso:
rem    start.bat                  avvio normale
rem    start.bat --update         forza l'aggiornamento dei pacchetti
rem    start.bat -a 0.0.0.0:8000  gli altri parametri passano a mkdocs
rem ---------------------------------------------------------------------

cd /d "%~dp0"

echo.
echo === Manuale Facile - anteprima locale ===
echo.

rem --- Lettura dei parametri --------------------------------------------
set "FORCE="
set "SERVEARGS="

:parse
if "%~1"=="" goto :parsed
if /i "%~1"=="--update" goto :arg_force
if /i "%~1"=="-u" goto :arg_force
set "SERVEARGS=%SERVEARGS% %1"
goto :arg_next
:arg_force
set "FORCE=1"
:arg_next
shift
goto :parse
:parsed

rem --- 1. Python --------------------------------------------------------
py --version >nul 2>&1
if errorlevel 1 (
    echo [ERRORE] Il launcher "py" non e' disponibile.
    echo          Installare Python da https://www.python.org/downloads/
    echo          spuntando l'opzione "Add python.exe to PATH".
    echo.
    pause
    exit /b 1
)
for /f "delims=" %%v in ('py --version 2^>^&1') do echo [OK] %%v

rem --- 2. pip -----------------------------------------------------------
py -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [..] pip non trovato, installazione in corso...
    py -m ensurepip --upgrade
    if errorlevel 1 (
        echo [ERRORE] Impossibile installare pip.
        echo.
        pause
        exit /b 1
    )
)

rem --- 3. File del progetto ---------------------------------------------
if not exist "mkdocs.yml" (
    echo [ERRORE] mkdocs.yml non trovato in "%CD%".
    echo          Lo script va tenuto nella cartella del manuale.
    echo.
    pause
    exit /b 1
)
if not exist "requirements.txt" (
    echo [ERRORE] requirements.txt non trovato in "%CD%".
    echo.
    pause
    exit /b 1
)

rem --- 4. Pacchetti Python ----------------------------------------------
if defined FORCE (
    echo [..] Aggiornamento dei pacchetti da requirements.txt...
    py -m pip install --upgrade -r requirements.txt
    if errorlevel 1 goto :pip_error
    goto :deps_ok
)

rem  Verifica che mkdocs e mkdocs-material siano importabili e che mkdocs
rem  sia ancora della serie 1.x: la 2.0 non supporta il tema Material.
py -c "import sys, mkdocs, material; sys.exit(0 if mkdocs.__version__.split('.')[0] == '1' else 1)" >nul 2>&1
if errorlevel 1 (
    echo [..] Pacchetti mancanti o non compatibili, installazione da requirements.txt...
    py -m pip install -r requirements.txt
    if errorlevel 1 goto :pip_error
) else (
    echo [OK] mkdocs e mkdocs-material gia' installati.
)

:deps_ok
for /f "delims=" %%v in ('py -m mkdocs --version 2^>^&1') do echo [OK] %%v

rem --- 5. Avvio del server ----------------------------------------------
echo.
echo Il manuale sara' raggiungibile su http://127.0.0.1:8000
echo Premere CTRL+C per fermare il server.
echo.

py -m mkdocs serve%SERVEARGS%
if errorlevel 1 (
    echo.
    echo [ERRORE] mkdocs serve e' terminato con un errore.
    echo.
    pause
    exit /b 1
)

endlocal
exit /b 0

:pip_error
echo.
echo [ERRORE] Installazione dei pacchetti non riuscita.
echo          Provare manualmente con: py -m pip install -r requirements.txt
echo.
pause
exit /b 1
