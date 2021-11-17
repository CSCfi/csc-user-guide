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
    "policy": 'Cookie Preferences',
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
            cscfi_domain=`${window.location.hostname}`.split(".").slice(-2).join('.');
            document.cookie = `_gat= ; expires= Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain= ${cscfi_domain};`;
            document.cookie = `_ga= ; expires= Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain= ${cscfi_domain};`;
            document.cookie = `_gid= ; expires= Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain= ${cscfi_domain};`;
            location.reload(); 

        }
    },

    "type": "opt-in"
});
