#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, CMake
import os


class SDL2ImageConan(ConanFile):
    name = "sdl2_image"
    version = "2.0.3"
    description = "SDL_image is an image file loading library"
    url = "https://github.com/bincrafters/conan-sdl2_image"
    homepage = "https://www.libsdl.org/projects/SDL_image/"
    license = "MIT"
    exports = ["LICENSE.md"]
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False],
               "fPIC": [True, False],
               "bmp": [True, False],
               "gif": [True, False],
               "lbm": [True, False],
               "pcx": [True, False],
               "pnm": [True, False],
               "svg": [True, False],
               "tga": [True, False],
               "xcf": [True, False],
               "xpm": [True, False],
               "xv": [True, False],
               "jpg": [True, False],
               "tif": [True, False],
               "png": [True, False],
               "webp": [True, False],
               "imageio": [True, False]}
    default_options = "shared=False", \
                      "fPIC=True", \
                      "bmp=True", \
                      "gif=True", \
                      "lbm=True", \
                      "pcx=True", \
                      "pnm=True", \
                      "svg=True", \
                      "tga=True", \
                      "xcf=True", \
                      "xpm=True", \
                      "xv=True", \
                      "jpg=True", \
                      "tif=True", \
                      "png=True", \
                      "webp=True", \
                      "imageio=False"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"
    exports_sources = ["CMakeLists.txt"]
    generators = ['cmake']

    def config_options(self):
        del self.settings.compiler.libcxx
        if self.settings.os == 'Windows':
            del self.options.fPIC
        if self.settings.os != 'Macos':
            del self.options.imageio

    def requirements(self):
        self.requires.add('sdl2/2.0.8@bincrafters/stable')
        if self.options.tif:
            self.requires.add('libtiff/4.0.9@bincrafters/stable')
        if self.options.jpg:
            self.requires.add('libjpeg/9c@bincrafters/stable')
        if self.options.png:
            self.requires.add('libpng/1.6.34@bincrafters/stable')
        if self.options.webp:
            self.requires.add('libwebp/1.0.0@bincrafters/stable')
        self.requires.add('zlib/1.2.11@conan/stable')

    def source(self):
        source_url = "https://www.libsdl.org/projects/SDL_image/release/SDL2_image-%s.tar.gz" % self.version
        tools.get(source_url)
        extracted_dir = "SDL2_image-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def build(self):
        cmake = CMake(self)
        if self.settings.os != 'Windows':
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC
        cmake.definitions['BMP'] = self.options.bmp
        cmake.definitions['GIF'] = self.options.gif
        cmake.definitions['JPG'] = self.options.jpg
        cmake.definitions['LBM'] = self.options.lbm
        cmake.definitions['PCX'] = self.options.pcx
        cmake.definitions['PNG'] = self.options.png
        cmake.definitions['PNM'] = self.options.pnm
        cmake.definitions['SVG'] = self.options.svg
        cmake.definitions['TGA'] = self.options.tga
        cmake.definitions['TIF'] = self.options.tif
        cmake.definitions['WEBP'] = self.options.webp
        cmake.definitions['XCF'] = self.options.xcf
        cmake.definitions['XPM'] = self.options.xpm
        cmake.definitions['XV'] = self.options.xv
        cmake.definitions['TIF_DYNAMIC'] = self.options['libtiff'].shared if self.options.tif else False
        cmake.definitions['JPG_DYNAMIC'] = self.options['libjpeg'].shared if self.options.jpg else False
        cmake.definitions['PNG_DYNAMIC'] = self.options['libpng'].shared  if self.options.png else False
        cmake.definitions['WEBP_DYNAMIC'] = self.options['libwebp'].shared if self.options.webp else False
        if self.settings.os == 'Macos':
            cmake.definitions['IMAGEIO'] = self.options.imageio
        else:
            cmake.definitions['IMAGEIO'] = False
        cmake.configure(build_dir='build')
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)

    def package_info(self):
        self.cpp_info.libs = ['SDL2_image']
        self.cpp_info.includedirs.append(os.path.join('include', 'SDL2'))
