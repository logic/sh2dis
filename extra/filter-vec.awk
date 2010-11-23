BEGIN {
    print "vectors = {";
}

/^v_/ {
    print "    " $2 ": {";
    print "        'name': '" $1 "',";
    print "        'size': " $3 ",";
    print "        'comment': '" substr($4, 0, length($4)-1) "',";
    print "    },";
}

END {
    print "}";
}
