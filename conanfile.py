#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, MSBuild, tools
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
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    requires = (
        "sdl2/2.0.8@bincrafters/stable"
    )

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

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
        with tools.chdir(os.path.join(self.source_subfolder, 'VisualC')):
            msbuild = MSBuild(self)
            msbuild.build_env.link_flags = ['/lib', 'winmm.lib']
            msbuild.build('SDL_image.sln')

    def build_configure(self):
        raise Exception('TODO')

    def package(self):
        raise Exception('TODO')
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        # If the CMakeLists.txt has a proper install method, the steps below may be redundant
        # If so, you can just remove the lines below
        include_folder = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="*", dst="include", src=include_folder)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
