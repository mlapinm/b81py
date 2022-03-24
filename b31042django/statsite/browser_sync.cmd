@REM browser-sync start --server

browser-sync start -s -f "*.html, *.css, *.php, css/*.css"

@REM -s - browser-sync работает в режиме сервера
@REM -f - отслеживает изменения в файлах
@REM - *.html, *.php - изменения в файлах html и php
@REM - изменения в файлах css в папке css
