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
            'src/binding.cpp',
            'src/Compress.cpp',
            'src/pngquant/pngquant.c',
            'src/pngquant/rwpng.c',
            'src/pngquant/lib/pam.c',
            'src/pngquant/lib/mediancut.c',
            'src/pngquant/lib/blur.c',
            'src/pngquant/lib/mempool.c',
            'src/pngquant/lib/viter.c',
            'src/pngquant/lib/nearest.c',
            'src/pngquant/lib/libimagequant.c',
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
