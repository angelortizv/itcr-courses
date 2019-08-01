#-------------------------------------------------
#
# Project created by QtCreator 2019-07-01T22:20:41
#
#-------------------------------------------------

QT       += core gui
QT       += multimedia

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = pacman
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += \
        main.cpp \
        src/mainwindow.cpp \
        src/highscores.cpp \
        src/game.cpp \
        src/gameover.cpp \
        src/game/entities/ghost.cpp \
        src/game/compass.cpp \
        src/game/entities/blinky.cpp \
        src/game/entities/clyde.cpp \
        src/game/entities/inky.cpp \
        src/game/entities/pacman.cpp \
        src/game/entities/pinky.cpp \
        src/game/animaterect.cpp \
        src/game/dashboard.cpp \
        src/game/entities/pellet.cpp \
        src/game/entities/dot.cpp \
        src/winner.cpp

HEADERS += \
        src/mainwindow.h \
        src/highscores.h \
        src/game.h \
        src/gameover.h \
        src/game/entities/character.h \
        src/game/entities/ghost.h \
        src/game/compass.h \
        src/game/entities/blinky.h \
        src/game/entities/clyde.h \
        src/game/entities/inky.h \
        src/game/entities/pacman.h \
        src/game/entities/pinky.h \
        src/game/animaterect.h \
        src/game/dashboard.h \
        src/game/entities/pellet.h \
        src/game/entities/item.h \
        src/game/entities/dot.h \
        src/winner.h

FORMS += \
        src/mainwindow.ui \
        src/highscores.ui \
        src/gameover.ui \
        src/winner.ui

RESOURCES += \
        imgresources.qrc \
        audioresources.qrc \
        fontresources.qrc
