[![Download](https://api.bintray.com/packages/bincrafters/public-conan/sdl2_image%3Abincrafters/images/download.svg) ](https://bintray.com/bincrafters/public-conan/sdl2_image%3Abincrafters/_latestVersion)
[![Build Status](https://travis-ci.org/bincrafters/conan-sdl2_image.svg?branch=stable%2F2.0.3)](https://travis-ci.org/bincrafters/conan-sdl2_image)
[![Build status](https://ci.appveyor.com/api/projects/status/github/bincrafters/conan-sdl2_image?branch=stable%2F2.0.3&svg=true)](https://ci.appveyor.com/project/bincrafters/conan-sdl2_image)

[Conan.io](https://conan.io) package recipe for [*sdl2_image*](https://www.libsdl.org/projects/SDL_image/).

SDL_image is an image file loading library

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/bincrafters/public-conan/sdl2_image%3Abincrafters).

## For Users: Use this package

### Basic setup

    $ conan install sdl2_image/2.0.3@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    sdl2_image/2.0.3@bincrafters/stable

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create bincrafters/stable


### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |
| fPIC      | True |  [True, False] |
| bmp      | True |  [True, False] |
| gif      | True |  [True, False] |
| lbm      | True |  [True, False] |
| pcx      | True |  [True, False] |
| pnm      | True |  [True, False] |
| svg      | True |  [True, False] |
| tga      | True |  [True, False] |
| xcf      | True |  [True, False] |
| xpm      | True |  [True, False] |
| xv      | True |  [True, False] |
| jpg      | libjpeg-turbo |  ['libjpeg', 'libjpeg-turbo', False] |
| tif      | True |  [True, False] |
| png      | True |  [True, False] |
| webp      | True |  [True, False] |
| imageio      | False |  [True, False] |

## Add Remote

    $ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload

    $ conan upload sdl2_image/2.0.3@bincrafters/stable --all -r bincrafters


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package sdl2_image.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](https://github.com/bincrafters/conan-sdl2_image.git/blob/testing/2.0.3/LICENSE.md)
