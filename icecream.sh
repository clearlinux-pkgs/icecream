#!/bin/sh
# Install icecc in PATH, but disable it by default
case ":${PATH:-}:" in
    *:/usr/libexec/icecc/bin:*) ;;
    *) PATH="/usr/libexec/icecc/bin${PATH:+:$PATH}" ;;
esac
if [ -z "$ICECC" ]; then
    ICECC=disable
fi
