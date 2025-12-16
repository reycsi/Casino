echo off
color 2
chcp 65001
cls
cd dep\save
set /p mon="Введите желаемое количество денег: "
echo %mon% > money.txt