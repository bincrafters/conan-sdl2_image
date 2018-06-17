#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, MSBuild, AutoToolsBuildEnvironment, tools
import os


class SDL2ImageConan(ConanFile):
    name = "sdl2_image"
    version = "2.0.3"
    description = "SDL_image is an image file loading library"
    url = "https://github.com/bincrafters/conan-sdl2_image"
    homepage = "https://www.libsdl.org/projects/SDL_image/"

    # Indicates License type of the packaged library
    license = "MIT"

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Options may need to change depending on the packaged library.
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], \
               "fPIC": [True, False], \
               "bmp": [True, False], \
               "gif": [True, False], \
               "lbm": [True, False], \
               "pcx": [True, False], \
               "pnm": [True, False], \
               "svg": [True, False], \
               "tga": [True, False], \
               "xcf": [True, False], \
               "xpm": [True, False], \
               "xv": [True, False], \
               "jpeg": [True, False], \
               "tiff": [True, False], \
               "png": [True, False], \
               "webp": [True, False]}
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
                      "jpeg=True", \
                      "tiff=True", \
                      "png=True", \
                      "webp=True"

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    requires = (
        "sdl2/2.0.8@bincrafters/stable"
    )

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def requirements(self):
        if self.options.tiff:
            self.requires.add('libtiff/4.0.9@bincrafters/stable')
        if self.options.jpeg:
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
        if self.settings.compiler == 'Visual Studio':
            self.build_msvc()
        else:
            self.build_configure()

    def build_msvc(self):
        def handle_option(option, name):
            if not option:
                tools.replace_in_file('SDL_image.vcxproj', name + ';', '')

        with tools.chdir(os.path.join(self.source_subfolder, 'VisualC')):
            tools.replace_in_file('SDL_image.vcxproj',
                                  '<AdditionalDependencies>',
                                  '<AdditionalDependencies>winmm.lib;version.lib;imm32.lib;')
            tools.replace_in_file('SDL_image.vcxproj',
                                  '<PreprocessorDefinitions>',
                                  '<PreprocessorDefinitions>LOAD_XCF;')
            if self.settings.build_type == 'Debug':
                tools.replace_in_file('SDL_image.vcxproj',
                                      'SDL2.lib',
                                      'SDL2d.lib')
            handle_option(self.options.bmp, 'LOAD_BMP')
            handle_option(self.options.gif, 'LOAD_GIF')
            handle_option(self.options.jpeg, 'LOAD_JPG')
            handle_option(self.options.lbm, 'LOAD_LBM')
            handle_option(self.options.pcx, 'LOAD_PCX')
            handle_option(self.options.png, 'LOAD_PNG')
            handle_option(self.options.pnm, 'LOAD_PNM')
            handle_option(self.options.svg, 'LOAD_SVG')
            handle_option(self.options.tga, 'LOAD_TGA')
            handle_option(self.options.tiff, 'LOAD_TIF')
            handle_option(self.options.webp, 'LOAD_WEBP')
            handle_option(self.options.xcf, 'LOAD_XCF')
            handle_option(self.options.xpm, 'LOAD_XPM')
            handle_option(self.options.xv, 'LOAD_XV')
            msbuild = MSBuild(self)
            msbuild.build('SDL_image.sln', targets=['SDL2_image'], platforms={"x86": "Win32"})

    def build_configure(self):
        with tools.chdir(self.source_subfolder):
            env_build = AutoToolsBuildEnvironment(self)
            args = ['--prefix=%s' % os.path.abspath(self.package_folder)]

            args.append('--enable-bmp' if self.options.bmp else '--disable-bmp')
            args.append('--enable-gif' if self.options.gif else '--disable-gif')
            args.append('--enable-lbm' if self.options.lbm else '--disable-lbm')
            args.append('--enable-pcx' if self.options.pcx else '--disable-pcx')
            args.append('--enable-pnm' if self.options.pnm else '--disable-pnm')
            args.append('--enable-svg' if self.options.svg else '--disable-svg')
            args.append('--enable-tga' if self.options.tga else '--disable-tga')
            args.append('--enable-xcf' if self.options.xcf else '--disable-xcf')
            args.append('--enable-xpm' if self.options.xpm else '--disable-xpm')
            args.append('--enable-xv' if self.options.xv else '--disable-xv')
            args.append('--enable-jpg' if self.options.jpeg else '--disable-jpg')
            args.append('--enable-tif' if self.options.tiff else '--disable-tif')
            args.append('--enable-png' if self.options.png else '--disable-png')
            args.append('--enable-webp' if self.options.webp else '--disable-webp')
            if self.options.shared:
                args.extend(['--disable-static', '--enable-shared'])
            else:
                args.extend(['--disable-shared', '--enable-static'])
            if self.settings.os != 'Windows' and self.options.fPIC:
                args.append('--with-pic')
            env_build.configure(args=args)
            env_build.make()
            env_build.make(args=['install'])

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        if self.settings.compiler == 'Visual Studio':
            self.copy(pattern="SDL_image.h", dst=os.path.join('include', 'SDL2'), src=self.source_subfolder)
            arch = 'x64' if self.settings.arch == 'x86_64' else 'Win32'
            libdir = os.path.join(self.source_subfolder, 'VisualC', arch, str(self.settings.build_type))
            self.copy(pattern="SDL2_image.lib", dst='lib', src=libdir)
            self.copy(pattern="SDL2_image.dll", dst='bin', src=libdir)

    def package_info(self):
        self.cpp_info.libs = ['SDL2_image']
        self.cpp_info.includedirs.append(os.path.join('include', 'SDL2'))
