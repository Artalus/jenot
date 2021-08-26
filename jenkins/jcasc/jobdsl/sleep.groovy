job('sleep') {
    properties {
        concurrentBuild()
    }
    parameters {
        stringParam('UID', '', 'uniq id to search builds from')
        stringParam('SLEEP', '60', 'seconds to sleep')
    }
    steps {
        shell('sleep ${SLEEP}')
    }
}
