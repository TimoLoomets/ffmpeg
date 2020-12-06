import mama

##
# Explore Mama docs at https://github.com/RedFox20/Mama
#
class ffmpeg(mama.BuildTarget):

    # this defines where to build all the dependencies
    # for project-local workspace: workspace = 'build'
    # for system-wide workspace: global_workspace = 'mycompany'
    workspace = 'build'

    # grab dependencies straight from git repositories
    # if the projects are trivial or support mama, then no extra configuration is needed
    # for others you will need to supply your own mamafile
    def dependencies(self):
        #self.add_git('ReCpp', 'https://github.com/RedFox20/ReCpp.git')
        #self.nothing_to_build() # if you have a header only library
        pass

    # customize CMake options in this step
    def configure(self):
        pass
        #self.enable_cxx17()
        #self.add_cmake_options('BUILD_TESTS=ON', 'USE_SSE2=ON')

    ## optional: customize package exports if repository doesn't have `include` or `src`
    ##           default include and lib export works for most common static libs
    #def package(self):
    #    self.export_libs('.', ['.lib', '.a']) # export any .lib or .a from build folder
    #    self.export_includes(['include'])     # export 'include' path from source folder

    # run your custom testing steps here
    #def test(self, args):
    #    self.gdb('bin/ffmpeg', src_dir=True)
    def package(self):
        if self.windows:
          if self.config.is_target_arch_x86():
              self.export_include('include')
              #self.export_libs('x86/bin', ['.lib','.dll'], src_dir=True)
          elif self.config.is_target_arch_x64():
              self.export_include('include')
              #self.export_libs('x64/bin', ['.lib','.dll'], src_dir=True)
        elif self.linux:
            self.export_libs('.', ['.a'])
            #self.export_syslib('libavcodec', 'ffmpeg')
            #self.export_syslib('libavformat', 'ffmpeg')
            #self.export_syslib('libavutil', 'ffmpeg')

