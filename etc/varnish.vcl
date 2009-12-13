backend backend0 {
    .host = "127.0.0.1";
    .port = "8005";
}

acl purge {
        "localhost";
        "121.0.0.1";
        "85.214.26.83";
        "87.230.26.151";
}

 
sub vcl_recv {
    set req.backend = backend0;

    if (req.request == "PURGE") {
                if (!client.ip ~ purge) {
                        error 405 "Not allowed.";
                }
                purge("req.url == " req.url);
    }
 

    if (req.request == "POST") {
         pass;
    }
    if (req.request != "GET" && req.request != "HEAD" &&
        req.request != "PUT" && req.request != "POST" &&
        req.request != "TRACE" && req.request != "OPTIONS" &&
        req.request != "DELETE") {

        # Non-RFC2616 or CONNECT which is weird. #
        pass;
    }
    if (req.http.Authorization) {
        # Not cacheable by default #
        pass;
    }
   
    lookup;
}

sub vcl_fetch {
    #if (req.request == "GET" && req.url ~ "^/static" ) {
    #    unset obj.http.Set-Cookie;
    #    set obj.ttl = 30m;
    #    deliver;
    #}
    if (req.url ~ "(gif$|css$|jpg$|jpeg$|png$|js$)") {
        unset obj.http.Set-Cookie;
        deliver;
    }
    if (req.url ~ "list/$") {
        set obj.ttl = 1m;
        deliver;
    } 
    if (obj.status >= 300) {
         pass;
    }
    if (!obj.cacheable) {
         pass;
    }
    if (obj.http.Set-Cookie) {
         pass;
    }
    if (obj.http.Cache-Control ~ "max-age") {
         unset obj.http.Set-Cookie;
        deliver;
    }   
    set obj.ttl = 60m;
    deliver;
}




    
