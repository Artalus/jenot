job('sleep') {
    parameters {
        stringParam('UID', '', 'uniq id to search builds from')
    }
    steps {
        shell('sleep 60')
    }
}
