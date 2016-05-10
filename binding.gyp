{
    'targets': [{
        'target_name': 'addon',
        'cflags': [
            '-DNO_ALONE',
            '-DDEBUG',
            '-fno-inline',
            '-O0',
            '-fstrict-aliasing', {
    'conditions': [
        ['OS=="win"', {
            'variables': {
                'THIRD_PATH%': 'C:/projects/node-pngquant-native/gyp/third-party'
            }
        }]
    ],
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
        "dependencies": [
            "./gyp/gyp/libpng.gyp:libpng"
        ],
        "include_dirs": [
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
