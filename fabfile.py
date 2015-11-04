from fabric.api import local


def deploy():
    # copy project to /temp folder
    local('rm -rf /tmp/markdown-core')
    local('cp -r ../markdown-core /tmp/')

    # remove unneeded folders / files
    local('rm -rf /tmp/markdown-core/.bowerrc')
    local('rm -rf /tmp/markdown-core/.git')
    local('rm -rf /tmp/markdown-core/.gitignore')
    local('rm -rf /tmp/markdown-core/bower.json')
    local('rm -rf /tmp/markdown-core/fabfile.py')
    local('rm -rf /tmp/markdown-core/fabfile.pyc')
    local('rm -rf /tmp/markdown-core/index.js')
    local('rm -rf /tmp/markdown-core/README.md')
    local('rm -rf /tmp/markdown-core/sample.md')

    # compress and mangle
    local('mv /tmp/markdown-core/markdown-core.js /tmp/markdown-core/markdown-core.js.temp')
    local('uglifyjs /tmp/markdown-core/markdown-core.js.temp -m -c --screw-ie8 -o /tmp/markdown-core/markdown-core.js')
    local('rm -rf /tmp/markdown-core/markdown-core.js.temp')
    local('mv /tmp/markdown-core/markdown-it-emoji-plus.js /tmp/markdown-core/markdown-it-emoji-plus.js.temp')
    local('uglifyjs /tmp/markdown-core/markdown-it-emoji-plus.js.temp -m -c --screw-ie8 -o /tmp/markdown-core/markdown-it-emoji-plus.js')
    local('rm -rf /tmp/markdown-core/markdown-it-emoji-plus.js.temp')

    # copy file to Markdown Mate project
    local('cp -r /tmp/markdown-core ~/src/swift/Markdown\ Mate/Markdown\ Mate/')


def dist():
    local('cp markdown-core.css dist/')
    local('uglifyjs markdown-core.js -o dist/markdown-core.min.js')