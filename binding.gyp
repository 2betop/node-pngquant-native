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
            'src/pngquant/pngquant.c',
            'src/pngquant/getopt.c',
            'src/pngquant/rwpng.c',
            'src/pngquant/pam.c',
            'src/pngquant/mediancut.c',
            'src/pngquant/blur.c',
            'src/pngquant/mempool.c',
            'src/pngquant/viter.c',
            'src/pngquant/nearest.c',
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
