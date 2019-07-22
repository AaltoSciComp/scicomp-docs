// javascript redirect http: to https:
// It is NOT preferred to do this client-side, but since readthedocs.org
// doesn't support automatic redirection server-side yet, we do what we can.
// General discussion: https://stackoverflow.com/q/4723213/
if (window.location.protocol == "http:" && window.location.hostname != "localhost" && window.location.port == "") {
    window.location.replace('https:' + window.location.href.substring(window.location.protocol.length));
}
