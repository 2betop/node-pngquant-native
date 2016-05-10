{
    'targets': [{
        'target_name': 'addon',
        'cflags': [
            '-g',
            '-DNO_ALONE',
            '-fno-inline',
            '-O0',
            '-fstrict-aliasing',
            '-ffast-math',
            '-funroll-loops',
            '-fomit-frame-pointer',
            '-ffinite-math-only',
            '-std=c99'

        ],
        'sources': [
            'src/Compress.cpp',
            'src/binding.cpp',
            'src/pngquant/pngquant.cpp',
            'src/pngquant/getopt.c',
            'src/pngquant/rwpng.cpp',
            'src/pngquant/pam.cpp',
            'src/pngquant/mediancut.cpp',
            'src/pngquant/blur.cpp',
            'src/pngquant/mempool.cpp',
            'src/pngquant/viter.cpp',
            'src/pngquant/nearest.cpp',
        ],
        'include_dirs': [
        ],
        'dependencies': [
            './gyp/gyp/libpng.gyp:libpng',
            './gyp/gyp/zlib.gyp:zlib'
        ],
        'conditions': [
            ['OS == "win"', {
            }, {
                'libraries': [
                    '-lm'
                ]
            }]
        ],
    }]
}
