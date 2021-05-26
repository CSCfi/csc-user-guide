window.cookieconsent.initialise({
    "palette": {
        "popup": {
            "background": "#237afc"
        },
        "button": {
            "background": "#fff",
            "text": "#237afc"
        }
    },
    "content": {
    "message": "Our website uses cookies to ensure you get the best experience on our website. Our website may also include third party cookies. ",
    "link": "Read more",
    "href": "https://www.csc.fi/en/use-of-cookies",
    "policy": 'Cookie Policy',
    'allow': 'Approve',
    'deny': 'Refuse'    
    }
    ,
    onStatusChange: function(status) {
        if(this.hasConsented()){
            cookieconsent.status = "allow";
            window[`ga-disable-${window._csc_ga_id}`] = false
            location.reload(); 
        }
        else{
            cookieconsent.status = "deny";
            window[`ga-disable-${window._csc_ga_id}`] = true
            document.cookie = `_gat= ; expires= Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain= ${window.location.hostname};`;
            document.cookie = `_ga= ; expires= Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain= ${window.location.hostname};`;
            document.cookie = `_gid= ; expires= Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain= ${window.location.hostname};`;
            location.reload(); 

        }
    },

    "type": "opt-in"
});
